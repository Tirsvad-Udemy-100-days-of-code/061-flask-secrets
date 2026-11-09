# MIL-004 Template inheritance and Bootstrap-Flask

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version for the Day 61 Flask Secrets project | [1c70baa] |

---

## Purpose

Decide that all pages share one base template and use Bootstrap-Flask, matching lecture steps 7 to 10.

## Deliverable

`base.html` with blocks, success and denied pages as child templates, super block styling, Bootstrap-Flask initialised, `render_form`, tests, screenshots 7 to 10.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Success and denied pages extend `base.html` | pytest passes | Test fails |
| 2 | Bootstrap CSS is loaded in all pages | pytest passes | Test fails |
| 3 | The login form is produced by `render_form` | pytest passes | Test fails |
| 4 | Screenshots for steps 7 to 10 in `docs/images/` and the README | Four images linked | Missing |
| 5 | Code passes review against `QC-PROG-PY` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Pages and validation must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 3 | [BC-001] |

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
| 1 | Step 7: inherit templates with base.html | Create `base.html` with title and content blocks; make success and denied pages extend it. | No | |
| 2 | Step 8: use a super block for styling | Add a `styling` block to `base.html` and extend it with `super()` on the denied page (red heading). | No | |
| 3 | Step 9: add Bootstrap-Flask | Initialise Bootstrap-Flask, load its CSS in `base.html` and convert index, login, success and denied pages. | No | |
| 4 | Step 10: render the form with render_form | Replace the hand-written form with `render_form(form)` and test the output. | No | |
| 5 | Capture screenshots for steps 7 to 10 | Capture the four steps in Docker and add them to the README. | No | |

---

[BC-001]: ../business-case.md
[1c70baa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/commit/1c70baa4fb513f9e44d476b27cc62631251ab0d3
