# MIL-005 Wiki in three languages

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version for the Day 61 Flask Secrets project | pending |

---

## Purpose

Decide that the project is explained for S02 and S03 in English, Danish and Bahasa Malaysia and is ready to release.

## Deliverable

Wiki pages for each of the ten lecture steps in en, da and ms, each with its screenshot and a section on what was gained, plus the final summary.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Wiki has an English, Danish and Bahasa Malaysia page for each of the ten steps | Three complete language sets | Any missing |
| 2 | Each page has its screenshot and a "What we gained" section | All present | Any missing |
| 3 | Wiki passes `check-languages.sh` and `QC-WIKI` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | All ten steps and screenshots must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4 | [BC-001] |

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
| 1 | Write the English wiki | One page per lecture step with screenshot and what was gained, following `framework/process/wiki.md`. | No | |
| 2 | Write the Danish wiki | Translate the English pages to Danish with the same structure and screenshots. | No | |
| 3 | Write the Bahasa Malaysia wiki | Translate the English pages to Bahasa Malaysia with the same structure and screenshots. | No | |
| 4 | Publish the wiki to the git host | Push the wiki using the wiki token from the personal `.env` (never printed) and link it from the README. | No | |
| 5 | Write the final run summary | Summarise merged pull requests, each RC with its verdict and every stand-in decision for S01. | No | |

---

[BC-001]: ../business-case.md
