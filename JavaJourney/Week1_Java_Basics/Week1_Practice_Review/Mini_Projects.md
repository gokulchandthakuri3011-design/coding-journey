#+ Mini-Projects — Week 1 (Java Basics)

This file lists compact mini-projects that cover all Week 1 topics (setup, variables, input, operators, conditionals, loops, arrays, and methods). Each project includes required topics, guiding questions, suggested extensions, and expected deliverables.

---

Project A — Personal Profile App
- Objectives: practice input, variables, conditionals, methods, and simple output formatting.
- Requirements:
  - Read user's name, age, city, and favorite letter.
  - Validate age (non-negative) and handle empty name input.
  - Print a formatted profile and a short message (e.g., birthday or age-based category).
- Guiding questions (covering all topics):
  - How do you compile and run the program from the command line?
  - Which types did you choose for each input and why?
  - How do you validate input and handle invalid values?
  - Which helper methods did you create and what do they return?
- Extensions: save profile to a simple text file; allow multiple profiles in an array and print a summary.
- Deliverables: `ProfileApp.java`, optional `profiles.txt`, small README describing usage.

---

Project B — Basic Number Toolbox
- Objectives: arithmetic operators, input parsing, conditionals, exception/edge-case handling, methods.
- Requirements:
  - Read two numbers (support integer and decimal input).
  - Print sum, difference, product, quotient, and remainder when applicable.
  - Indicate which numbers are even/odd (for integers) and compare magnitudes.
- Guiding questions (covering all topics):
  - How did you handle integer vs. floating-point division?
  - How do you prevent or handle division by zero?
  - Which methods did you create to organize calculations?
  - How would you adapt input reading to avoid `nextInt()`/`nextLine()` pitfalls?
- Extensions: add a menu loop so the user can repeat operations until they choose to exit; add parity and sign checks.
- Deliverables: `NumberToolbox.java`, README with sample runs.

---

Project C — Quiz & Decision Maker
- Objectives: arrays, loops, input, conditionals, methods, basic scoring or branching logic.
- Requirements:
  - Represent 3–5 questions and accepted answers in arrays.
  - Ask the user questions, collect answers, compute a score or choose a result based on responses.
  - Print a final result with feedback.
- Guiding questions (covering all topics):
  - How are questions and answers stored and accessed in arrays?
  - Which loop did you use to iterate questions and why?
  - How do you compare `String` answers correctly?
  - Which methods encapsulate asking a question, validating an answer, and scoring?
- Extensions: load questions from a file; randomize questions; add timed answers.
- Deliverables: `QuizApp.java`, optional `questions.txt`, README.

---

Project D — Student Scores Analyzer
- Objectives: arrays, loops, methods, aggregation (sum/avg/max/min), input validation.
- Requirements:
  - Read N student names and scores (N from user), store in parallel arrays or a simple `Student` class.
  - Compute average, highest, lowest, and count of passing/failing students using methods.
  - Print a formatted report.
- Guiding questions (covering all topics):
  - How do you allocate and iterate arrays for dynamic N?
  - Which methods did you write for calculations and why?
  - How do you handle invalid numeric input and re-prompt the user?
  - How would you refactor to use a `Student` class instead of parallel arrays?
- Extensions: sort students by score; save report to a file; compute grade distribution.
- Deliverables: `StudentAnalyzer.java`, optional `Student.java`, README.

---

Notes
- Keep each program concise and focused; use small helper methods to separate concerns.
- Include comments and a short README describing how to compile and run each program.
- Example compile/run commands to include in READMEs:

```bash
javac ProfileApp.java
java ProfileApp
```

---

Quick checklist (for each mini-project)
- [ ] Program compiles and runs from command line
- [ ] Inputs validated and edge cases handled
- [ ] At least one helper method implemented
- [ ] README with usage examples

---

Pick one project to implement this week; reopen for feedback or to add sample solutions.
