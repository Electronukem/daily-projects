# Daily Projects

Small, self-contained Python practice programs: classic algorithms (N-Queens, edit
distance, LRU cache, word ladder), data structures (Bloom filter, custom hash table)
and simulations (cellular automata, Langton's ant, L-system fractals). Each dated
folder holds the programs added that day.

The programs are committed by a scheduled script, so the commit history reflects
that schedule. Earlier runs re-committed identical copies of the same programs on
different days; those duplicates were removed, so each program now appears once, in
the folder where it first appeared.

Each file runs on its own. All but the three earliest (April 2026 pattern printers)
check themselves with `assert`s:

```
python 2026-09-22/elementary_cellular_automaton.py
```
