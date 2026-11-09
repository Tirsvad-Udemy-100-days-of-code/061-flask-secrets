# Review of the project wiki (docs/wiki)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Review of the project wiki | [733a36b] |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Recorded the check of the published wiki (criterion 14) | [bfce620] |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Recorded S01 language confirmation (criteria 3, 5, 9) | pending |

---

## Artifact Under Review

- Instance reviewed: the project wiki in `docs/wiki/` (a wiki page set has no artifact ID)
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en, da, ms / it
- Language reviewer: S01 (confirmed in chat on 2026-11-09)
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
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English is the PO language; Danish and Bahasa Malaysia are added on top. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 11 English pages, 11 Danish pages (-da) and 11 Bahasa Malaysia pages (-ms). |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line with the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Suffixes -da and -ms (BCP 47); English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code blocks, commands, file names are English in all languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | After the merge the workflow publish-wiki-pages succeeded; on 2026-11-09 all 33 wiki pages answered HTTP 200 on the host, the sidebar and Home list the pages and the Languages section, and the step screenshots load. Recorded by the AI as a tool check. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No generator is used. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 34 files are directly in docs/wiki/, no subfolder. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | N-A | Wiki pages have no Metadata table; the language is told by the file suffix. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Codes en, da, ms are BCP 47. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | S01 read the Danish and Bahasa Malaysia pages and confirmed in chat on 2026-11-09: "pages are fine". |
| 4 | The register matches the one the registry gives for the artifact type | Pass | IT Professional English register in English; the same register in translation. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary exists; terms follow the Flask and WTForms documentation. S01 confirmed the pages in chat on 2026-11-09. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | N-A | No Metadata, headings are page content in the page language by design. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | Translations are separate wiki pages by design (the wiki rule), not translated twins of an artifact. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 confirmed in chat on 2026-11-09 ("pages are fine"). The confirmation was given for all language pages; no separate Malay reader was named. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations such as CSRF are explained in context. |

## Overall Verdict

Go: all Mandatory structure criteria pass. Criterion 14 was checked on the published wiki after the merge and passes. S01 confirmed the Danish and Bahasa Malaysia wording in chat on 2026-11-09, so QC-LANG-001 criteria 3, 5 and 9 pass. The wiki is not an artifact with a Version History, so no status changes.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None (S01 confirmed the language pages on 2026-11-09) | S01 | - |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[733a36b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/commit/733a36b1aceaf0574be7062bba541a75c7677c2b
[bfce620]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/061-flask-secrets/commit/bfce620034c5b0a279343ef81de33b4c819e0787
