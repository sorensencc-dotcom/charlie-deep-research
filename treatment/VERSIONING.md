# Treatment Versioning Process

STATUS: ACTIVE (2026-07-17). Governs `TREATMENT_DRAFT_v*.md` and any file that revises it.

## 1. One numbering scheme

`TREATMENT_DRAFT_v{major}.{minor}.md` is the only valid version identifier for the treatment.
No other scheme ("v13", "Act Four," "v14," etc.) may be used in any doc in this repo.

- **Major** bump: beat count, section order, or spine changes.
- **Minor** bump: prose/language changes within the locked spine (VERIFY-tag resolution, chronology tightening, contested-tag additions — the kind of pass `CIC_REMEDIATION_PLAN_v1.md` drives).

Any citation of the form "Treatment vN" in a sourcing packet, checklist, or box request MUST resolve
to an actual `TREATMENT_DRAFT_vN.md` file in this directory. If the file doesn't exist, the citation
is wrong — fix it, don't propagate it. Before citing a version, `ls TREATMENT_DRAFT_v*.md` and confirm.

## 2. Changelog is mandatory, same commit as the bump

Every new `TREATMENT_DRAFT_v{X.Y}.md` ships with a `CHANGELOG_v{X.Y}.md` in the same commit. No
exceptions — a version bump without a changelog is an incomplete commit, not a fast one.

Changelog contents, minimum:
- Base version it derives from.
- Scope line: spine touched or not; sections touched.
- Per-change entry: what changed, which beat/line, why (link the governing doc — remediation plan
  item ID, spec amendment ID, sourcing packet).
- Governed-by line matching the draft's own header.

## 3. Revision drafts (pre-integration)

A standalone revision pass (e.g. "Section 5–6 revision") that hasn't been merged into a numbered
draft yet is named for the version it targets once integrated:
`SECTION_{N}_{M}_REVISION_for_v{X.Y}_draft.md` — never a bare version number of its own ("v14").
It is untracked/WIP until integrated; integrating it is what triggers the changelog + version bump
in Rule 2.

## 4. Enforcement

Before committing any treatment doc: grep this directory for `Treatment v[0-9]` and confirm every
hit matches an existing `TREATMENT_DRAFT_v*.md` filename. Before bumping a version, confirm the
matching `CHANGELOG_v*.md` exists in the same commit.

## 5. Backfill note

`CHANGELOG_v1.md` does not exist (v1 was the first draft — nothing to log against). `CHANGELOG_v1.1.md`
was missing until 2026-07-17; reconstructed from `TREATMENT_VALIDATION_REPORT_v1.1.md` and
`SPEC_AMENDMENT_2_S3_A1.md` — see that file for scope of the reconstruction.
