# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [1c70baa] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | MIL-001 to MIL-005 | [RC-003] |
| [MIL-001] | Milestone | en | it | [PP-001] | tasks of MIL-001 | [RC-004], [RC-009] |
| [MIL-002] | Milestone | en | it | [PP-001] | tasks of MIL-002 | [RC-005], [RC-010] |
| [MIL-003] | Milestone | en | it | [PP-001] | tasks of MIL-003 | [RC-006], [RC-011] |
| [MIL-004] | Milestone | en | it | [PP-001] | tasks of MIL-004 | [RC-007] |
| [MIL-005] | Milestone | en | it | [PP-001] | tasks of MIL-005 | [RC-008] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] | - | - | Covered |
| CN-002 | [MIL-001] | - | - | Covered |
| CN-003 | [MIL-001] | - | - | Covered |
| CN-004 | [MIL-002] | - | - | Covered |
| CN-005 | [MIL-001] | - | - | Covered |
| CN-006 | [MIL-001] | - | - | Covered |

## Open Inconsistencies

None.

## Coverage Notes

No use cases, design artifacts or test plans exist: the lecture tasks are plain technical tasks. `-` in Upstream means foundational; `-` in Decisions or Quality check means none exists.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-baseline.md
[MIL-002]: ../milestones/mil-002-login-form.md
[MIL-003]: ../milestones/mil-003-validation-and-login-check.md
[MIL-004]: ../milestones/mil-004-templates-and-bootstrap.md
[MIL-005]: ../milestones/mil-005-wiki-and-release.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-project-baseline.md
[RC-005]: ./reviews/rc-005-mil-002-login-form.md
[RC-006]: ./reviews/rc-006-mil-003-validation-and-login-check.md
[RC-007]: ./reviews/rc-007-mil-004-templates-and-bootstrap.md
[RC-008]: ./reviews/rc-008-mil-005-wiki-and-release.md
[1c70baa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/commit/1c70baa4fb513f9e44d476b27cc62631251ab0d3
[RC-009]: ./reviews/rc-009-mil-001-code.md
[RC-010]: ./reviews/rc-010-mil-002-code.md
[RC-011]: ./reviews/rc-011-mil-003-code.md
