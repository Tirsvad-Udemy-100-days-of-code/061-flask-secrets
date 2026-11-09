# MIL-002 Login route and Flask-WTF form

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version for the Day 61 Flask Secrets project | [1c70baa] |

---

## Purpose

Decide that the application serves a login page built from a Flask-WTF form, matching lecture steps 1 to 3.

## Deliverable

Flask application with `home` and `login` routes, a `LoginForm` with email, password and submit fields, CSRF protection, tests, and step screenshots 1 to 3 in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /login` returns 200 and renders the form with email and password inputs of size 30 | pytest passes | Test fails |
| 2 | The form contains a CSRF token field | pytest passes | Test fails |
| 3 | Screenshots for steps 1 to 3 exist in `docs/images/` and the README | Three images linked | Missing |
| 4 | Code passes review against `QC-PROG-PY` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Project tooling must exist |

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
| 1 | Step 1: create the login route | Create the Flask app with `home` and `login` functions; `login` renders `login.html`, as in the lecture challenge. Test that the route answers 200. | No | |
| 2 | Step 2: build LoginForm with Flask-WTF | Create `LoginForm` with StringFields for email and password (size 30), a secret key from `constants.py` and `form.csrf_token` in the template. Test the fields and the token. | No | |
| 3 | Step 3: apply the five code improvements | Use PasswordField, label keywords, `url_for` for the form action, a table layout and a SubmitField. Test that the password input is of type password. | No | |
| 4 | Capture screenshots for steps 1 to 3 | Take headless-browser screenshots inside a Docker container (no host desktop) and add them to the README with a short caption each. | No | |

---

[BC-001]: ../business-case.md
[1c70baa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/commit/1c70baa4fb513f9e44d476b27cc62631251ab0d3
