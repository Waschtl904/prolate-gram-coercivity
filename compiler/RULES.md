# Dependency Compiler Rules

These rules are enforced by `dag_validate.py`.
Every new node added to `dag_nodes.json` must pass all rules.

---

## Node Types

| Type | Meaning | Special rules |
|---|---|---|
| `T` | Proved theorem within XXII | Must have explicit `requires`; may not re-prove BB content |
| `I` | Exact identity (no asymptotics, no limit) | May be used freely; axis = `infrastructure` |
| `BB` | Black box (imported, never re-proved) | `requires` must be empty or reference only other BBs |
| `H` | Hypothesis / open assumption | Cannot appear in `on_minimal_path: true` nodes' `requires` if it is P5 or P7 |
| `C` | Conjecture (stated, not proved) | Same restriction as H |
| `O` | Open problem | Must have `closes` and `mechanism`; `on_minimal_path` must be `false` |

---

## The 10 Validation Rules

### R1 — Unique IDs
Every node `id` must be unique in `dag_nodes.json`.

### R2 — Reference integrity
Every ID appearing in `requires` or `used_in` must exist in the registry.

### R3 — No cycles
The dependency graph must be a DAG (directed acyclic graph).
A cycle means a circular proof dependency and is forbidden.

### R4 — No BB re-proof *(structural, not yet automated)*
No `T` node may re-derive the content of a `BB` node.
This is currently checked by the author; future versions will use
statement embedding similarity.

### R5 — Minimal path purity
Nodes with `on_minimal_path: true` may not have `O1` or `O2` in their
`requires` list (directly or via transitive closure).
Reason: O1/O2 (RHP enhancement) are not on the minimal path to P13.

### R6 — Open problem completeness
Every node of type `O` must have both `closes` and `mechanism` fields.
An open problem without an explicit resolution mechanism is not
admissible in this program.

### R7 — Bidirectional consistency
If `A.requires` contains `B`, then `B.used_in` must contain `A`.
This prevents silent one-way dependencies.

### R8 — Reachability of Main Theorem
The main theorem node (`P13`) must be reachable from both `O4` and `O5`
in the forward direction.
This guarantees the product structure `F_Gram × F_Airy` is maintained.

### R9 — No RHP on minimal path (transitive)
No node on the minimal path may have O1 or O2 as a transitive dependency.
This enforces the separation: RHP enhancement is optional, not foundational.

### R10 — Axis consistency
A `T` node on axis `discrete` may not require a node on axis `rhp`.
Reason: the two research strands (O4 = discrete, O5 = spectral, O1/O2 = rhp)
must remain methodologically independent.
Silent axis crossings are a common source of structural corruption in
long research programs.

---

## How to Add a New Node

1. Write the node as JSON conforming to `dag_schema.json`.
2. Run: `python compiler/dag_validate.py --new-node '<your JSON>'`
3. If all rules pass, add the node to `dag_nodes.json`.
4. Re-run: `python compiler/dag_validate.py` (full registry check).
5. Update `paper22_dag.tex` to include the new node in the appropriate layer.

## How to Check the Minimal Path

```bash
python compiler/dag_validate.py --show-path P13
```

## How to List All Nodes on an Axis

```bash
python compiler/dag_validate.py --axis discrete
python compiler/dag_validate.py --axis spectral
python compiler/dag_validate.py --axis rhp
```
