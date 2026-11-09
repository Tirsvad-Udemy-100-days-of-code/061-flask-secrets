# MIL-001 Project baseline and repository

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version for the Day 61 Flask Secrets project | [1c70baa] |

---

## Purpose

Decide that the repository, tooling and documentation baseline are ready so that code can start.

## Deliverable

Repository with description and topics, `pyproject.toml`, Python `.gitignore`, `Doxyfile`, `constants.py` skeleton, README from the framework template with venv instructions, accepted BC, SA, PP and milestones, prompt log.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Business Case, Stakeholder Analysis, Project Plan and milestones are Accepted with Go reviews | All reviews Go | Any review No-Go |
| 2 | Repository has a description and at least 5 topics on the git host | Visible in repository settings | Missing |
| 3 | `python -m pip install -e .[dev]` and `python -m pytest` work in a fresh `.venv` | Both exit 0 | Either fails |
| 4 | README follows the framework template and passes `check-readme.sh` | Script exits 0 | Script fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4 and 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-09 — the Business Case sets no deadline; one pull request is delivered per milestone, in order.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Use the git host API with the repo token read from the personal `.env` (never printed or committed) to set a description and topics such as flask, flask-wtf, wtforms, bootstrap-flask, udemy, 100-days-of-code, python. Serves S03. | No | |
| 2 | Create project configuration | Add `pyproject.toml` (Python >=3.13, runtime dependencies Flask, Flask-WTF, email-validator, Bootstrap-Flask; optional `dev` extra with pytest), a Python `.gitignore` that also ignores `.env` and `.venv`, and package folders under `src/` and `tests/`. | No | |
| 3 | Add Doxyfile and constants module | Add a `Doxyfile` configured for `src/` and a `constants.py` skeleton so later milestones keep every constant in one module, as the Product Owner requires. | No | |
| 4 | Write README with venv instructions | Fill the framework README template: what the project is, how to create and use a local `.venv`, `python -m pip install --upgrade pip`, install, run and test commands. | No | |
| 5 | Install git hooks and record the prompt log | Run the framework hook installer and start `docs/ai-prompts/session-001/` as the prompt-log process requires. | No | |

---

[BC-001]: ../business-case.md
[1c70baa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/commit/1c70baa4fb513f9e44d476b27cc62631251ab0d3
