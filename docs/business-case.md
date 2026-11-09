# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version for the Day 61 Flask Secrets project | pending |

---

## Executive Summary

Day 61 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" teaches advanced forms with Flask-WTF. This project builds the "Secrets" website: a Flask application with a login form (email and password) that shows a secret page only for the right credentials. The project is delivered as a readable, runnable, tested repository with a README and a three-language wiki (English, Danish, Bahasa Malaysia) that explains what each lecture step taught, with a screenshot per step.

## Methodological and Standards Foundation

The work follows the SQA and QC framework mounted at `framework/` (plan-first gate, one reviewed artifact per step) and ISO/IEC 25010:2023 for the quality characteristics of every QC criterion. Source code follows the Python conventions of the `coding-conventions` skill and Clean Architecture; tests use pytest; source comments use Doxygen.

## Problem Statement

A course participant who copies a lecture solution gets code that is hard to compare, run and learn from later: there are no tests, no run instructions, no explanation of why each step exists and no visual proof of what each step should look like. Other course participants and repository visitors face the same gap.

## Business Opportunity

A clean reference solution lets S01 keep a portfolio of the course, lets S02 compare solutions against runnable code with the assignment's function names, and lets S03 find ideas through a clear description, topics and README.

## Objectives

1. Deliver a Flask application that follows every lecture step of Day 61: login route, Flask-WTF form, validation, credential check with success and denied pages, template inheritance, Bootstrap-Flask and `render_form`.
2. Deliver pytest tests for each behaviour of the application.
3. Deliver a README with run and test instructions and one screenshot per lecture step.
4. Deliver a wiki in English, Danish and Bahasa Malaysia that explains what was gained in each lecture step, with the same screenshots.
5. Publish the repository with a description and topics on the git host.

## Scope

### In Scope

- The Flask application under `src/`, tests under `tests/`, documents under `docs/`.
- `pyproject.toml`, a Python `.gitignore`, a Doxyfile, `constants.py`, local `.venv` instructions.
- README from the framework template; wiki in three languages; screenshots of every lecture step.
- Repository description and topics on the git host.

### Out of Scope

- A real user database, password hashing or registration (the course uses one fixed demo account).
- Production deployment and hosting.
- Day 62 and later lectures.
- Importing or testing the personal `.env` file in the project; it is used only to read git host tokens for tooling.

## Expected Benefits

### Tangible Benefits

- A runnable repository with a passing automated test suite.
- A README and a three-language wiki with ten step screenshots.
- A described, topic-tagged repository that others can find.

### Intangible Benefits

- A durable record of what each lecture step taught.
- Practice of the plan-first, reviewed workflow.

## Strategic Alignment

The project supports S01's goal of completing the course with traceable, reviewed work, and the course's aim that participants share and compare code.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Automated tests pass | 100 % of tests pass on Python 3.13 | `python -m pytest` exit code 0 |
| 2 | Lecture steps documented with a screenshot | 10 of 10 steps in README and in each wiki language | Count of step sections with an image |
| 3 | Wiki languages | 3 of 3 (en, da, ms) | Count of wiki language pages |
| 4 | Runtime dependencies | Only Flask, Flask-WTF, email-validator, Bootstrap-Flask | `pyproject.toml` dependencies list |
| 5 | Milestones delivered through reviewed pull requests | 5 of 5 merged | Merged pull request count |
| 6 | Repository metadata | Description and at least 5 topics set | Git host repository settings |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Screenshot capture would take over the host desktop | Interrupts the user, breaks the GUI testing rule | Capture in a Docker container with a headless browser (`framework/process/gui-testing.md`) |
| Git host token is missing or lacks scope | Cannot set topics or open pull requests | Stop and report; the user supplies the token |
| Machine translation of the wiki contains errors | Misleading explanations | Keep sentences short and plain; S01 reviews the final text |
| A token is leaked into the repository | Security defect | `.env` is ignored, never read into output or committed |
| Demo credentials mistaken for real security practice | Poor habits copied by S02 | State clearly in README and wiki that the fixed account is a lecture demo |

## Assumptions

- S01 is the Product Owner, developer and reviewer; in autonomous mode the AI acts as recorded stand-in reviewer.
- Python 3.13 or newer and Docker are available on the development machine.
- The personal `.env` file at the parent folder holds the git host tokens.
- The people in S02 and S03 are not contacted; they are served by the repository itself.

## Constraints

- Python 3.13 or newer, venv, pytest, `pyproject.toml`, `constants.py` for constants.
- Folders `src/`, `tests/`, `docs/`; branch plus pull request per milestone.
- Product Owner domain language is English, domain IT.
- Avoid runtime dependencies beyond what the lecture needs.
- Repository: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets.

## Cost–Benefit Assessment

Qualitative, justified because this is a personal learning project with no revenue; cost is S01's time and a small AI effort.

| Costs | Benefits |
| --- | --- |
| Time to plan, build, review and document five milestones | Reusable reference solution and portfolio entry |
| Time to produce and check three wiki languages | Accessible learning record for English, Danish and Malay readers |
| Docker image pull for screenshots | Reproducible screenshots without touching the desktop |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Complete the course with traceable, reviewed work |
| S02 | Compare solutions against readable, runnable code |
| S03 | Find ideas through description, topics and README |

## Recommendation

Proceed — the scope is small, the quality gates are defined and the outcome serves all three stakeholders.
