# MOD2 — Basics 3

Learn-by-doing scaffold. Each `exNN/` has a **NOTES.md** explaining the concepts
and a skeleton file with the function signatures, hints, and `TODO`s for you to
fill in. The given test harnesses (`main`, `doom_printer`, `CoffeeMachine`, ...)
are kept intact so you can run as you go.

| Exercise | Topic | Files to turn in | Read first |
|----------|-------|------------------|-----------|
| ex00 | map / filter / reduce, generators | ft_map.py, ft_filter.py, ft_reduce.py | ex00/NOTES.md |
| ex01 | *args / **kwargs, getattr/setattr | main.py | ex01/NOTES.md |
| ex02 | decorators | logger.py | ex02/NOTES.md |
| ex03 | context manager class | csvreader.py | ex03/NOTES.md |
| ex04 | building a pip package | build.sh, *.py, *.md, *.cfg, *.txt | ex04/NOTES.md |
| ex05 | basic statistics by hand | TinyStatistician.py | ex05/NOTES.md |

## Suggested order
Do them in order — ex04 reuses your ex02 logger (and your MOD0 ex10 progress bar).

## How to work an exercise
1. Open `exNN/NOTES.md`, read the concept + hints.
2. Fill the `TODO`s in the skeleton.
3. Run it: `cd exNN && python <file>.py` and compare against the subject's
   expected output.
