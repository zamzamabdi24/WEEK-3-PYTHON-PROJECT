# Week 3 Assignment: Conditions and Loops

## Files

- `grade_reporter.py` – Reads a list of scores, assigns grades (A/B/C/F), counts passes/fails, and prints the average.
- `bug_hunt.py` – Fixed version of a broken program that sums numbers 1 to 5, with comments explaining each bug.

## Bug Hunt Reflection

The hardest bug to find was the logic bug in the `while` condition (`count < 5` instead of `count <= 5`). It did not produce any error message; the program ran fine but printed the wrong sum (10 instead of 15). I knew something was wrong because the output did not match the expected result (15), even though there were no syntax or type errors.
