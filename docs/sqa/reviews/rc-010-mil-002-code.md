# Code review of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Code review of MIL-002 | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review of the source and tests delivered by the milestone
- Language and domain: n/a
- Language reviewer: none (S01 reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | PEP 8 names: snake_case, PascalCase, UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` passes; all signatures annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except and no swallowed exception. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults, no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | No files or connections opened. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Docstrings with Doxygen tags on public items. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print; no secret or personal data logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; the tasks are plain technical tasks (milestone Tasks column says No). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | pytest tests exist, are named for the behaviour and use no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy strict passes. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dependencies declared in pyproject.toml; none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each constant is defined once in constants.py. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Imports point inward. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Modules have one reason to change. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers and test folders follow the clean-architecture structure. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English snake_case names without spaces. |

## Overall Verdict

Go — All Mandatory criteria pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-002]: ../../milestones/mil-002-login-form.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
