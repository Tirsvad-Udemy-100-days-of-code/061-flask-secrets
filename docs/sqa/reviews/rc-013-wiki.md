# Review of the project wiki (docs/wiki)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | <author> | AI as stand-in for S01 | Review of the project wiki | pending |

---

## Artifact Under Review

- Instance reviewed: the project wiki in `docs/wiki/` (a wiki page set has no artifact ID)
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en, da, ms / it
- Language reviewer: none named; see the Pending criteria below
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, then one English list with Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Home and the ten step pages are listed; every link has a file. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wikis, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is the last section: English, Dansk, Bahasa Malaysia, each linking to its Home page. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | N-A | Wiki pages have no Metadata table; the language is told by the file suffix. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Codes en, da, ms are BCP 47. |
| 3 | The content (prose and table cells) is written in the stated language | Pending | The AI wrote the Danish and Bahasa Malaysia text as translations of the English. Only S01 (Danish) and a Malay reader can confirm it; a stand-in cannot. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | IT Professional English register in English; the same register in translation. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pending | No dictionary exists; terms follow the Flask and WTForms documentation. Needs a native reader to confirm the Danish and Malay terms. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | N-A | No Metadata, headings are page content in the page language by design. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | Translations are separate wiki pages by design (the wiki rule), not translated twins of an artifact. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pending | No reviewer who reads Bahasa Malaysia is named in the Stakeholder Analysis. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations such as CSRF are explained in context. |

## Overall Verdict

Go-with-conditions: all Mandatory structure criteria pass. Criterion 14 and QC-LANG-001 criteria 3, 5 and 9 are Pending because only a person can confirm them (the published wiki after the merge, and the Danish and Bahasa Malaysia wording). The wiki is not an artifact with a Version History, so no status changes.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the published wiki sidebar and every link after the merge (criterion 14) | S01 | 2026-11-16 |
| Read the Danish pages and confirm the wording (QC-LANG-001 criteria 3, 5, 9) | S01 | 2026-11-16 |
| Find a reader of Bahasa Malaysia to confirm the Malay pages | S01 | 2026-11-16 |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
