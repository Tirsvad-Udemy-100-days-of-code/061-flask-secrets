# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version for the Day 61 Flask Secrets project | [1c70baa] |

---

## Purpose

Identifies who is affected by the Day 61 Flask Secrets project and what each stakeholder needs, so that every later artifact can cite stable stakeholder IDs. The method is a power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the lecture with correct, reviewed, well-documented work |
| S02 | Udemy coursists | Course participants who share and compare code | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and clear run instructions |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Monitor | A clear description, topics and README, and no heavy runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts the plan and owns every review.
- **Keep Informed (S02):** cannot change the project but depends on its README and code quality.
- **Monitor (S03):** casual visitors with no influence; served by repository metadata.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step is implemented and reviewed | Functionality |
| CN-002 | S01 | Work is traceable from plan to pull request | Supportability |
| CN-003 | S02 | Code is readable and runs with the documented commands | Usability |
| CN-004 | S02 | Function names match the assignment | Functionality |
| CN-005 | S03 | Description, topics and README explain the project at a glance | Usability |
| CN-006 | S03 | Few runtime dependencies | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| COM-001 | Chat with S01 | Plan acceptance and run summary | Plan dry run, final summary | All milestones |
| COM-002 | README and wiki | Updated per milestone | Run instructions, step screenshots | MIL-002 to MIL-005 |
| COM-003 | Repository description and topics | Once | Git host metadata | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the assignment's simple code; good practice asks for layers and tests | S02, S01 | Keep the assignment's function names (`home`, `login`) and put the layers in small modules; explain in the wiki |
| S03 wants no dependencies; the lecture requires Flask-WTF and Bootstrap-Flask | S03, S01 | Declare only the four packages the lecture needs; dev tools are optional extras |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1, 2 and 5 |
| S02 | CN-003, CN-004 | [BC-001] objectives 1, 3 and 4 |
| S03 | CN-005, CN-006 | [BC-001] objectives 3 and 5 |

## Sign-Off

Author and Product Owner: S01. Reviewed in autonomous mode by the AI as stand-in for S01; recorded in the review record.

---

[BC-001]: ./business-case.md
[1c70baa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/commit/1c70baa4fb513f9e44d476b27cc62631251ab0d3
