# CIC_GOVERNANCE_INHERITANCE_MAP_V1.1

## 1. GOVERNANCE HEADER

Downstream governance inheritance generated under Spec v1.1 semantics.
Source: CIC_ARCHIVAL_VERIFICATION_CONSOLIDATED_V1.1_FINAL (39 units).

## 2. GOVERNANCE CHANNELS

- INGESTION_GOVERNANCE — controls asset registration into CIC store. Admission requires PASS.
- LINEAGE_GOVERNANCE — controls instantiation of provenance/timeline nodes. Admission requires verified node.
- SCRIPT_GOVERNANCE — controls claim propagation into script/VO. Admission requires cleared, cited, script-facing evidence.
- AUDIT_GOVERNANCE — controls audit-clean certification. Admission requires no evidence gap.

## 3. INHERITANCE RULES (GLOBAL)

- PASS → admissible; no gating; inherit as primary-capture asset across all four channels.
- FAIL → blocked; cannot enter any governance channel until corrected.
- NEEDS_REVISION → gated; cannot enter registry; cannot propagate claims; cannot instantiate timeline nodes; cannot be used as script-facing evidence.

## 4. CHANNEL-SPECIFIC INHERITANCE MAP

| ITEM_ID | INGESTION_INHERITANCE | LINEAGE_INHERITANCE | SCRIPT_INHERITANCE | AUDIT_INHERITANCE |
|---|---|---|---|---|
| V-1.2a | NON-INGESTIBLE until correction (asset unregisterable pre-inventory). | NODE-BLOCKED (no provenance chain to originator). | SCRIPT-BLOCKED (no script-facing claim until registered). | AUDIT-DEFECT (holdings gap pending inventory). |
| V-1.2b | NON-INGESTIBLE until correction (unregisterable pre-manifest). | NODE-BLOCKED (no custody/date metadata chain). | SCRIPT-BLOCKED (no script use until manifest). | AUDIT-DEFECT (uncounted-holdings gap). |
| V-1.2c | NON-INGESTIBLE until correction (asset gated on rights). | NODE-BLOCKED (citation chain to edition/page absent). | SCRIPT-BLOCKED (quoted text uncleared into script/VO). | AUDIT-DEFECT (rights-clearance gap). |
| V-1.3 | NON-INGESTIBLE until correction (ledger asset gated on retrieval). | NODE-BLOCKED (Denmark→America loop, S1 geo, unsupported). | SCRIPT-BLOCKED (specific-entry claim withheld until cited). | AUDIT-DEFECT (primary-record gap). |
| V-2.1 | NON-INGESTIBLE until correction (manifest asset gated on retrieval). | NODE-BLOCKED (origin timeline node unverified; S2 dates inherit uncertainty). | SCRIPT-BLOCKED (departure-year claim provisional). | AUDIT-DEFECT (primary-record gap). |
| V-2.4 | NON-INGESTIBLE until correction (employment-record asset gated). | NODE-BLOCKED (partnership-start node imprecise). | SCRIPT-BLOCKED ("circa 1905" blocked until exact date). | AUDIT-DEFECT (timeline-imprecision flag). |
| V-3.2 | NON-INGESTIBLE until correction (memoir-derived claim tagged contested). | NODE-BLOCKED (chassis-drag node single-source). | SCRIPT-BLOCKED (primacy risk R2 if unqualified). | AUDIT-DEFECT (single-source contested claim). |
| V-3.4a | INGESTIBLE (flag reworded + re-verified 2026-07-14; conformant with §2/S3-A1). | NODE-ADMISSIBLE (geo-scope drift cleared; domestic-only scope confirmed). | SCRIPT-ADMISSIBLE (domestic-scoped wording matches locked clause verbatim). | AUDIT-CLEAN (conformant with locked spec v1.1; prior non-conformance resolved). |
| V-3.5 | NON-INGESTIBLE until correction (press-clipping assets pending pull). | NODE-BLOCKED (first-theft thesis node uncited). | SCRIPT-BLOCKED (uncited attribution). | AUDIT-DEFECT (thesis-beat unsupported). |
| V-4.2 | NON-INGESTIBLE until correction (financial-record asset gated). | NODE-BLOCKED ($50M keystone propagates to logline/§4 table unverified). | SCRIPT-BLOCKED (figure inherited unverified). | AUDIT-DEFECT (financial-claim gap). |
| V-4.3 | NON-INGESTIBLE until correction (foundry-record assets pending). | NODE-BLOCKED (throughput node uncited). | SCRIPT-BLOCKED (drumbeat #2 numbers uncited). | AUDIT-DEFECT (production-data gap). |
| V-4.4 | NON-INGESTIBLE until correction (claim tagged memoir-derived). | NODE-BLOCKED (labor-counterweight §5 evidence gap). | SCRIPT-BLOCKED (antagonist-seed single-source tag). | AUDIT-DEFECT (antagonist-seed R3 single-source). |
| V-4.5a | NON-INGESTIBLE until correction (Ford-of-Europe records gated). | NODE-BLOCKED (export-logic §5 origin node unverified). | SCRIPT-BLOCKED (oversight scope/dates provisional). | AUDIT-DEFECT (primary-record gap). |
| V-4.5b | NON-INGESTIBLE until correction (Soviet/German citation assets pending). | NODE-BLOCKED (export-reach node uncited). | SCRIPT-BLOCKED (geopolitics risk R4 if unsourced). | AUDIT-DEFECT (export-reach claim uncited). |
| V-5.2a | NON-INGESTIBLE until correction (construction-record asset gated). | NODE-BLOCKED (superlative node unverified). | SCRIPT-BLOCKED (absolute "largest" claim propagates). | AUDIT-DEFECT (superlative-claim gap). |
| V-5.2b | NON-INGESTIBLE until correction (parts-count source pending). | NODE-BLOCKED (parts-count variance unresolved). | SCRIPT-BLOCKED (contested figure inherited as fixed). | AUDIT-DEFECT (uncited/variant-figure gap). |
| V-5.3 | NON-INGESTIBLE until correction (claim tagged memoir-attributed). | NODE-BLOCKED (highest-weight uncorroborated node, midpoint). | SCRIPT-BLOCKED (midpoint memoir-attributed tag R2). | AUDIT-DEFECT (midpoint keystone single-source). |
| V-5.4a | NON-INGESTIBLE until correction (coinage source pending). | NODE-BLOCKED ("Willit Run?" node uncited). | SCRIPT-BLOCKED (coinage propagates unattributed). | AUDIT-DEFECT (attribution gap). |
| V-5.4b | NON-INGESTIBLE until correction (diary asset gated on rights). | NODE-BLOCKED (diary-passage citation absent). | SCRIPT-BLOCKED (uncleared quotation). | AUDIT-DEFECT (rights + citation gap). |
| V-5.5 | NON-INGESTIBLE until correction (63-min figure tagged temporal-conflict). | NODE-BLOCKED (temporal metadata mismatch inherited by §4 table/logline). | SCRIPT-BLOCKED (63-min risks false 1943 attribution). | AUDIT-DEFECT (date-integrity defect). |
| V-6.1 | NON-INGESTIBLE until correction (non-memoir episode sources pending). | NODE-BLOCKED (culpability node single-source). | SCRIPT-BLOCKED (culpability beat R2 single-source tag). | AUDIT-DEFECT (culpability thesis single-source). |
| V-6.2a | NON-INGESTIBLE until correction (medical/biographical records gated). | NODE-BLOCKED (decline node unverified). | SCRIPT-BLOCKED (medical claim propagates unverified). | AUDIT-DEFECT (primary-record gap). |
| V-6.2b | NON-INGESTIBLE until correction (dismissal-episode sources pending). | NODE-BLOCKED (antagonist-realization node single-source). | SCRIPT-BLOCKED (dismissal claims unsourced tag). | AUDIT-DEFECT (antagonist-realization R3 evidence gap). |
| V-6.3 | NON-INGESTIBLE until correction (War Dept correspondence gated). | NODE-BLOCKED (national-security altitude §5 claim unverified). | SCRIPT-BLOCKED (federal-intervention claim provisional). | AUDIT-DEFECT (contested-claim gap). |
| V-6.4 | NON-INGESTIBLE until correction (HFII Navy-release records gated). | NODE-BLOCKED (succession-pivot node unverified). | SCRIPT-BLOCKED (HFII release fact unverified). | AUDIT-DEFECT (primary-record gap). |
| V-6.5 | NON-INGESTIBLE until correction (exit-mechanics corroboration pending). | NODE-BLOCKED (open-question node must not lock). | SCRIPT-BLOCKED (exit sequence open-question/memoir tag R2). | AUDIT-DEFECT (false-belief-shatter keystone single-source). |
| V-6.6 | NON-INGESTIBLE until correction (participant-recollection source pending). | NODE-BLOCKED ("You're through" node recollection-based). | SCRIPT-BLOCKED (quoted line verbatim — tag recollected). | AUDIT-DEFECT (recollection-source gap). |
| V-7.1 | NON-INGESTIBLE until correction (Willys corporate records gated). | NODE-BLOCKED (second-life timeline nodes imprecise). | SCRIPT-BLOCKED (titles/dates provisional). | AUDIT-DEFECT (timeline-imprecision flag). |
| V-7.2 | NON-INGESTIBLE until correction (CESOR exclusive asset unregistered). | NODE-BLOCKED (no custody chain for exclusive). | SCRIPT-BLOCKED (exclusive claim withheld until registered). | AUDIT-DEFECT (holdings-verification gap). |
| V-7.3a | NON-INGESTIBLE until correction (vessel registry gated). | NODE-BLOCKED (private-empire asset node Helene unverified). | SCRIPT-BLOCKED (ownership dates provisional). | AUDIT-DEFECT (primary-record gap). |
| V-7.3b | NON-INGESTIBLE until correction (land/estate records gated). | NODE-BLOCKED (expropriation setup §5 unsupported). | SCRIPT-BLOCKED (holdings scale/operations provisional). | AUDIT-DEFECT (property-record gap). |
| V-7.4 | NON-INGESTIBLE until correction (expropriation records gated). | NODE-BLOCKED (highest-weight geo node §5 keystone open). | SCRIPT-BLOCKED (specific property fate withheld). | AUDIT-DEFECT (keystone unverified). |
| V-7.5 | NON-INGESTIBLE until correction (edition record gated). | NODE-BLOCKED (memoir bibliographic node propagates to S1/S8). | SCRIPT-BLOCKED (pub date/Williamson credit inherited unverified). | AUDIT-DEFECT (bibliographic-record gap). |
| V-8.1a | NON-INGESTIBLE until correction (death record gated). | NODE-BLOCKED (terminal-timeline node asserted-but-unverified). | SCRIPT-BLOCKED (date/place provisional). | AUDIT-DEFECT (vital-record gap). |
| V-8.1b | NON-INGESTIBLE until correction (obituary clippings pending pull). | NODE-BLOCKED ("brevity is evidence" node uncited). | SCRIPT-BLOCKED (aide/lieutenant characterization propagates). | AUDIT-DEFECT (uncited-thesis gap). |
| V-8.1c | NON-INGESTIBLE until correction (claim gated on located instance). | NODE-BLOCKED (assumption would inherit downstream as fact). | SCRIPT-BLOCKED (misspelling claim must convert to conditional). | AUDIT-DEFECT (speculative assertion in locked prose). |
| V-8.2 | NON-INGESTIBLE until correction (TPS-lineage sources pending). | NODE-BLOCKED (legacy-verdict node uncited). | SCRIPT-BLOCKED (causal Toyota→Ford lineage propagates). | AUDIT-DEFECT (legacy-verdict claim uncited). |
| V-8.3 | NON-INGESTIBLE until correction (2026-shoot capture pending). | NODE-BLOCKED (commemoration-state node pre-asserted). | SCRIPT-BLOCKED (null finding would lock prematurely). | AUDIT-DEFECT (pre-asserted unverified outcome). |
| V-8.4 | INGESTIBLE (primary-capture asset; register post-shoot). | NODE-ADMISSIBLE (clean — no inherited claim). | SCRIPT-ADMISSIBLE (no pre-asserted claim; conformant). | AUDIT-CLEAN (conformant). |

## 5. GOVERNANCE BLOCKS (AGGREGATED)

### A. INGESTION_GOVERNANCE_BLOCK

**NON-INGESTIBLE (NEEDS_REVISION — 37):**
V-1.2a, V-1.2b, V-1.2c, V-1.3, V-2.1, V-2.4, V-3.2, V-3.5, V-4.2, V-4.3, V-4.4, V-4.5a, V-4.5b, V-5.2a, V-5.2b, V-5.3, V-5.4a, V-5.4b, V-5.5, V-6.1, V-6.2a, V-6.2b, V-6.3, V-6.4, V-6.5, V-6.6, V-7.1, V-7.2, V-7.3a, V-7.3b, V-7.4, V-7.5, V-8.1a, V-8.1b, V-8.1c, V-8.2, V-8.3

**INGESTIBLE (PASS — 2):**
V-3.4a (re-verified 2026-07-14), V-8.4

### B. LINEAGE_GOVERNANCE_BLOCK

**NODE-BLOCKED (37):**
V-1.2a, V-1.2b, V-1.2c, V-1.3, V-2.1, V-2.4, V-3.2, V-3.5, V-4.2, V-4.3, V-4.4, V-4.5a, V-4.5b, V-5.2a, V-5.2b, V-5.3, V-5.4a, V-5.4b, V-5.5, V-6.1, V-6.2a, V-6.2b, V-6.3, V-6.4, V-6.5, V-6.6, V-7.1, V-7.2, V-7.3a, V-7.3b, V-7.4, V-7.5, V-8.1a, V-8.1b, V-8.1c, V-8.2, V-8.3

**NODE-ADMISSIBLE (2):**
V-3.4a (re-verified 2026-07-14), V-8.4

### C. SCRIPT_GOVERNANCE_BLOCK

**SCRIPT-BLOCKED (37):**
V-1.2a, V-1.2b, V-1.2c, V-1.3, V-2.1, V-2.4, V-3.2, V-3.5, V-4.2, V-4.3, V-4.4, V-4.5a, V-4.5b, V-5.2a, V-5.2b, V-5.3, V-5.4a, V-5.4b, V-5.5, V-6.1, V-6.2a, V-6.2b, V-6.3, V-6.4, V-6.5, V-6.6, V-7.1, V-7.2, V-7.3a, V-7.3b, V-7.4, V-7.5, V-8.1a, V-8.1b, V-8.1c, V-8.2, V-8.3

**SCRIPT-ADMISSIBLE (2):**
V-3.4a (re-verified 2026-07-14), V-8.4

### D. AUDIT_GOVERNANCE_BLOCK

**AUDIT-DEFECT (37):**
V-1.2a, V-1.2b, V-1.2c, V-1.3, V-2.1, V-2.4, V-3.2, V-3.5, V-4.2, V-4.3, V-4.4, V-4.5a, V-4.5b, V-5.2a, V-5.2b, V-5.3, V-5.4a, V-5.4b, V-5.5, V-6.1, V-6.2a, V-6.2b, V-6.3, V-6.4, V-6.5, V-6.6, V-7.1, V-7.2, V-7.3a, V-7.3b, V-7.4, V-7.5, V-8.1a, V-8.1b, V-8.1c, V-8.2, V-8.3

**AUDIT-CLEAN (2):**
V-3.4a (re-verified 2026-07-14), V-8.4

## 6. CIC_GOVERNANCE_INTEGRITY_V1.1

| CHECK | RESULT | EVIDENCE |
|---|---|---|
| FAIL units remain blocked | PASS | No FAIL units remain; V-3.4a corrected and re-verified to PASS 2026-07-14 — no unit currently in FAIL state. |
| NEEDS_REVISION units remain gated | PASS | All 37 NEEDS_REVISION units gated on all four channels; none admitted. |
| PASS units remain admissible | PASS | V-3.4a and V-8.4 both INGESTIBLE + NODE-ADMISSIBLE + SCRIPT-ADMISSIBLE + AUDIT-CLEAN. |
| No unit crosses channels without correction | PASS | V-3.4a's cross to admissible is backed by a documented correction + independent re-verification (source: CIC_ARCHIVAL_VERIFICATION_CONSOLIDATED_V1.1_FINAL §8). No other unit crosses without equivalent evidence. |
| No semantic drift vs Spec v1.1 / amendment §2/S3-A1 | PASS | Channel marks derived solely from DOWNSTREAM_IMPACT / re-verification record; V-3.4a's admissible marks trace to confirmed domestic-only wording match against locked clause. |

GOVERNANCE_INTEGRITY_STATUS: CLEAN (5/5 checks PASS) — updated 2026-07-14 post re-verification

## 7. CIC_GOVERNANCE_STATUS_V1.1

- 2 admissible (PASS): V-3.4a, V-8.4.
- 0 blocked (FAIL).
- 37 gated (NEEDS_REVISION).
- Governance inheritance complete — updated 2026-07-14 (V-3.4a re-verified FAIL→PASS).
