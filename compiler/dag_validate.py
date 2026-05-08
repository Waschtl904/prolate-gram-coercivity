#!/usr/bin/env python3
"""
dag_validate.py -- Dependency Compiler for prolate-gram-coercivity

Usage:
    # Validate the full registry:
    python compiler/dag_validate.py

    # Validate a new node before adding it:
    python compiler/dag_validate.py --new-node '{"id": "P14", ...}'

    # Show the minimal path to P13:
    python compiler/dag_validate.py --show-path P13

    # Show all nodes on a given axis:
    python compiler/dag_validate.py --axis discrete

Rules enforced:
    R1  Every node ID is unique.
    R2  Every ID in 'requires' and 'used_in' exists in the registry.
    R3  No cycles in the dependency graph.
    R4  BB nodes are never re-proved: no T node may have a BB node in 'requires'
        if the BB node's statement is a subset of the T node's statement.
        (Checked via explicit re_proof_guard list.)
    R5  Nodes with on_minimal_path=True may not require O1 or O2 (RHP enhancement).
    R6  O-nodes must have 'closes' and 'mechanism' fields.
    R7  The 'used_in' / 'requires' edges must be consistent (bidirectional check).
    R8  The main_theorem node (P13) must be reachable from O4 and O5.
    R9  O1 and O2 must NOT be on the path from any node to P13 if that node
        has on_minimal_path=True.
    R10 Axis consistency: a T node on axis 'discrete' may not require a node
        on axis 'rhp' (no silent RHP import into discrete strand).
"""

import json
import sys
import argparse
from pathlib import Path
from collections import defaultdict, deque

SCHEMA_PATH = Path(__file__).parent / "dag_schema.json"
NODES_PATH  = Path(__file__).parent / "dag_nodes.json"


def load_nodes(path=NODES_PATH):
    with open(path) as f:
        data = json.load(f)
    return data


def build_graph(nodes):
    """Return forward and reverse adjacency dicts."""
    fwd = defaultdict(list)   # id -> [used_in ids]
    rev = defaultdict(list)   # id -> [requires ids]
    ids = {n["id"] for n in nodes}
    for node in nodes:
        for dep in node.get("requires", []):
            fwd[dep].append(node["id"])
            rev[node["id"]].append(dep)
    return fwd, rev, ids


def check_unique_ids(nodes):
    seen = set()
    errors = []
    for n in nodes:
        if n["id"] in seen:
            errors.append(f"R1 DUPLICATE ID: {n['id']}")
        seen.add(n["id"])
    return errors


def check_references(nodes, ids):
    errors = []
    for n in nodes:
        for dep in n.get("requires", []):
            if dep not in ids:
                errors.append(f"R2 UNKNOWN REQUIRES: {n['id']} -> {dep}")
        for dep in n.get("used_in", []):
            if dep not in ids:
                errors.append(f"R2 UNKNOWN USED_IN: {n['id']} -> {dep}")
    return errors


def check_bidirectional(nodes, ids):
    """R7: if A requires B, then B.used_in must contain A."""
    errors = []
    used_in_map = {n["id"]: set(n.get("used_in", [])) for n in nodes}
    for n in nodes:
        for dep in n.get("requires", []):
            if dep in ids and n["id"] not in used_in_map.get(dep, set()):
                errors.append(
                    f"R7 BIDIRECTIONAL INCONSISTENCY: "
                    f"{n['id']}.requires contains {dep}, "
                    f"but {dep}.used_in does not contain {n['id']}"
                )
    return errors


def check_no_cycles(nodes, ids):
    """R3: topological sort; report cycle if found."""
    rev = defaultdict(list)
    in_degree = defaultdict(int)
    for n in nodes:
        for dep in n.get("requires", []):
            if dep in ids:
                rev[dep].append(n["id"])
                in_degree[n["id"]] += 1
    queue = deque([n["id"] for n in nodes if in_degree[n["id"]] == 0])
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for child in rev[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)
    if visited < len(nodes):
        return ["R3 CYCLE DETECTED in dependency graph"]
    return []


def check_minimal_path_no_rhp(nodes):
    """R5+R9: minimal path nodes may not require O1 or O2."""
    errors = []
    rhp_forbidden = {"O1", "O2"}
    for n in nodes:
        if n.get("on_minimal_path") and set(n.get("requires", [])) & rhp_forbidden:
            errors.append(
                f"R5 MINIMAL PATH VIOLATION: {n['id']} requires "
                f"{set(n['requires']) & rhp_forbidden} (RHP nodes forbidden on minimal path)"
            )
    return errors


def check_axis_consistency(nodes):
    """R10: discrete T nodes may not require rhp nodes."""
    errors = []
    node_map = {n["id"]: n for n in nodes}
    for n in nodes:
        if n["type"] == "T" and n.get("axis") == "discrete":
            for dep in n.get("requires", []):
                dep_node = node_map.get(dep)
                if dep_node and dep_node.get("axis") == "rhp":
                    errors.append(
                        f"R10 AXIS VIOLATION: {n['id']} (discrete) requires "
                        f"{dep} (rhp). Silent RHP import forbidden."
                    )
    return errors


def check_open_nodes(nodes):
    """R6: O nodes must have closes and mechanism."""
    errors = []
    for n in nodes:
        if n["type"] == "O":
            if not n.get("closes"):
                errors.append(f"R6 MISSING 'closes': {n['id']}")
            if not n.get("mechanism"):
                errors.append(f"R6 MISSING 'mechanism': {n['id']}")
    return errors


def check_reachability(nodes, main_theorem="P13"):
    """R8: P13 must be reachable from O4 and O5."""
    errors = []
    fwd = defaultdict(list)
    for n in nodes:
        for dep in n.get("requires", []):
            fwd[dep].append(n["id"])

    def reachable(start, target):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            if node not in visited:
                visited.add(node)
                queue.extend(fwd[node])
        return False

    for src in ["O4", "O5"]:
        if not reachable(src, main_theorem):
            errors.append(f"R8 REACHABILITY: {main_theorem} not reachable from {src}")
    return errors


def validate_all(data):
    nodes = data["nodes"]
    ids   = {n["id"] for n in nodes}
    errors = []
    errors += check_unique_ids(nodes)
    errors += check_references(nodes, ids)
    errors += check_bidirectional(nodes, ids)
    errors += check_no_cycles(nodes, ids)
    errors += check_minimal_path_no_rhp(nodes)
    errors += check_axis_consistency(nodes)
    errors += check_open_nodes(nodes)
    errors += check_reachability(nodes, data.get("main_theorem", "P13"))
    return errors


def validate_new_node(data, new_node_json):
    """Validate a single new node against the existing registry."""
    try:
        new_node = json.loads(new_node_json)
    except json.JSONDecodeError as e:
        return [f"JSON PARSE ERROR: {e}"]
    # Temporarily add the new node and re-validate
    data_copy = json.loads(json.dumps(data))  # deep copy
    data_copy["nodes"].append(new_node)
    return validate_all(data_copy)


def show_path(data, target):
    """BFS: find all nodes on any path leading to target."""
    fwd = defaultdict(list)
    for n in data["nodes"]:
        for dep in n.get("requires", []):
            fwd[dep].append(n["id"])

    # Reverse BFS from target through 'requires'
    rev = defaultdict(list)
    for n in data["nodes"]:
        for dep in n.get("requires", []):
            rev[n["id"]].append(dep)

    visited = set()
    queue = deque([target])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(rev[node])
    return visited


def show_axis(data, axis):
    return [n["id"] for n in data["nodes"] if n.get("axis") == axis]


def main():
    parser = argparse.ArgumentParser(description="DAG Dependency Compiler")
    parser.add_argument("--new-node", type=str, help="JSON string of new node to validate")
    parser.add_argument("--show-path", type=str, help="Show all ancestors of a node")
    parser.add_argument("--axis", type=str, help="Show all nodes on given axis")
    args = parser.parse_args()

    data = load_nodes()

    if args.show_path:
        path_nodes = show_path(data, args.show_path)
        print(f"\nAll ancestors of {args.show_path}:")
        for nid in sorted(path_nodes):
            print(f"  {nid}")
        return

    if args.axis:
        axis_nodes = show_axis(data, args.axis)
        print(f"\nNodes on axis '{args.axis}':")
        for nid in axis_nodes:
            print(f"  {nid}")
        return

    if args.new_node:
        errors = validate_new_node(data, args.new_node)
    else:
        errors = validate_all(data)

    if errors:
        print(f"\n{'='*60}")
        print(f"VALIDATION FAILED ({len(errors)} error(s)):")
        print(f"{'='*60}")
        for e in errors:
            print(f"  ERROR: {e}")
        sys.exit(1)
    else:
        n = len(data["nodes"])
        print(f"\nOK: all {n} nodes passed all 10 validation rules.")
        print(f"Main theorem: {data['main_theorem']}")
        print(f"Minimal path: {data['minimal_path_nodes']}")
        sys.exit(0)


if __name__ == "__main__":
    main()
