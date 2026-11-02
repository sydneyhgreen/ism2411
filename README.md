# ISM2411 — Python for Business

**Name:** Sydney Green
**Semester:** Fall 2026
**Instructor:** Markum Reed, Ph.D.

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week07/` — Functions: calculate_tax, apply_discount, final_price

## How to Run

Each script is standalone. Open a terminal and run:

```
python week07/functions.py
```

## Reflection

### 1. Commit history

```
ce9e6c3 ignore Office lock files in .gitignore
3cfe1a7 add README with module listing and run instructions
a70bb1a add module 7 functions: calculate_tax, apply_discount, final_price
0b06369 add .gitignore for Python and OS files
c734823 Delete .gitignore
3500ac5 Clean up .gitignore entries
75f0359 Add .gitignore for Python and OS files
f322e95 Create .gitignore
8e1caef Initial commit
```

My commit messages each describe one specific change, like adding the .gitignore, the Module 7 functions, or the README. If I were hiring someone and saw this history, it would tell me they work in small, deliberate steps and can explain what they did. The early .gitignore commits and deletions also show I was still figuring out the workflow, which is honest.

### 2. How Git changes my approach to editing

Before this module, I would edit a working script directly and hope I could undo a mistake. Now I can commit a version that works first and then experiment, knowing I can always get back to it. I would also make smaller changes and commit after each one, so that if something breaks I know exactly which change caused it.

### 3. Something specific to my machine

I added `~$*` to my .gitignore. Microsoft Office creates these temporary lock files (like `~$Academic Success Plan.xlsx` on my Desktop) whenever a document is open. They only exist on my computer while I am working, they change constantly, and they have no value to anyone else, so tracking them would just add clutter to the repository.
