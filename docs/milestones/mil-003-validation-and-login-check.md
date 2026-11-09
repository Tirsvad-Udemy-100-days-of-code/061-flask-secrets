# MIL-003 Validation and login check

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version for the Day 61 Flask Secrets project | [1c70baa] |

---

## Purpose

Decide that the form validates input and decides between the success and denied pages, matching lecture steps 4 to 6.

## Deliverable

Validators (DataRequired, Email, Length min 8), `novalidate` form, credential check against the demo account, success and denied pages, tests, screenshots 4 to 6.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Empty submission shows required-field errors | pytest passes | Test fails |
| 2 | Invalid email or password shorter than 8 characters shows an error | pytest passes | Test fails |
| 3 | Correct demo credentials show the success page; others show the denied page | pytest passes | Test fails |
| 4 | Screenshots for steps 4 to 6 in `docs/images/` and the README | Three images linked | Missing |
| 5 | Code passes review against `QC-PROG-PY` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The form must exist |

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
| 1 | Step 4: add DataRequired validation and novalidate | Add DataRequired validators, show `form.<field>.errors` in the template, accept POST and call `validate_on_submit()`; disable browser validation with `novalidate`. | No | |
| 2 | Step 5: add Email and Length validators | Add the Email validator (needs the email-validator package) and Length(min=8) for the password. Test one valid and several invalid inputs. | No | |
| 3 | Step 6: check credentials and show success or denied | Compare the submitted values with the demo account kept in `constants.py` and render `success.html` or `denied.html`. | No | |
| 4 | Capture screenshots for steps 4 to 6 | Capture the error states and both result pages in Docker; add them to the README. | No | |

---

[BC-001]: ../business-case.md
[1c70baa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/commit/1c70baa4fb513f9e44d476b27cc62631251ab0d3
