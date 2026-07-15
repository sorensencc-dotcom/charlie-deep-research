# CIC_ARCHIVAL_VERIFICATION_CONSOLIDATED_V1.1_FINAL

## 1. HEADER

Independent archival verification complete.
39 provenance units validated under Spec v1.1 semantics.

## 2. SUMMARY COUNTS

- PASS: 1
- FAIL: 1
- NEEDS_REVISION: 37

## 3. DEFECT CLASS SUMMARY

| DEFECT_CLASS | ITEM_IDS | COUNT |
|---|---|---|
| SPEC_NONCONFORMANCE | V-3.4a (secondary: GEO_SCOPE_DRIFT) | 1 |
| PRIMARY_RECORD_GAP | V-1.3, V-2.1, V-4.2, V-4.5a, V-6.2a, V-6.3, V-6.4, V-7.3a, V-7.3b, V-7.4, V-7.5, V-8.1a | 12 |
| UNCITED_ASSERTION | V-3.5, V-4.3, V-4.5b, V-5.2a, V-5.2b, V-5.4a, V-8.1b, V-8.1c, V-8.2 | 9 |
| SINGLE_SOURCE_RISK | V-3.2, V-4.4, V-5.3, V-6.1, V-6.2b, V-6.5, V-6.6 | 7 |
| HOLDINGS_VERIFICATION_GAP | V-1.2a, V-1.2b, V-7.2 | 3 |
| RIGHTS_CLEARANCE | V-1.2c, V-5.4b | 2 |
| TIMELINE_NODE_IMPRECISION | V-2.4, V-7.1 | 2 |
| TEMPORAL_INTEGRITY | V-5.5 | 1 |
| PROVENANCE_GAP | V-8.3 | 1 |
| GEO_SCOPE_DRIFT | (secondary of V-3.4a) | 0 primary |

## 4. CONSOLIDATED TABLE

| ITEM_ID | STATUS | SPEC_REF | PROVENANCE_NOTES | REQUIRED_CORRECTION | DOWNSTREAM_IMPACT |
|---|---|---|---|---|---|
| V-1.2a | NEEDS_REVISION | §2·S1 Archival opportunities | Beat 1.2. Claim: condition/marginalia of family-held memoir copies. Source basis: family-held, unconfirmed. No archival evidence in hand; physical inventory not performed. | Gather custody record + condition survey of family copies; label as family-held primary artifact pending inspection. | Ingestion: asset cannot be registered until inventoried. Lineage: no provenance chain to originator. |
| V-1.2b | NEEDS_REVISION | §2·S1 Archival opportunities | Beat 1.2. Claim: family photographs/ephemera between memoir pages. Source basis: family-held, "to be inventoried." No manifest exists. | Produce itemized ephemera inventory with custody + date metadata before any on-screen use. | Ingestion: unregisterable assets. Audit: uncounted holdings gap. |
| V-1.2c | NEEDS_REVISION | §2·S1 Archival opportunities; §8 R6 | Beat 1.2. Claim: memoir passage read aloud. Source basis: rights not confirmed; passage unselected. | Confirm memoir reproduction rights + lock passage citation to edition/page before scripting. | Script inheritance: quoted text propagates uncleared into script/VO. Audit: rights-clearance gap. |
| V-1.3 | NEEDS_REVISION | §2·S1 Archival opportunities; §2·S1 Geopolitical relevance | Beat 1.3. Claim: Sorensen family entries in 1880s Danish emigration ledgers. Source basis: presence "to be confirmed." No archival citation. | Retrieve exact ledger entry (archive name, folio, date); cite. If absent, restate as representative not specific. | Lineage: Denmark→America loop (S1 geo function) unsupported. Audit: primary-record gap. |
| V-2.1 | NEEDS_REVISION | §2·S2 Archival opportunities; §2·S2 Geopolitical relevance | Beat 2.1. Claim: emigration records, ship manifest, exact departure year (1881 birth context). Source basis: unconfirmed. | Source manifest + departure year from Danish/immigration archives; cite record ID. | Lineage: origin timeline node unverified; all S2 dates inherit uncertainty. |
| V-2.4 | NEEDS_REVISION | §2·S2 Purpose; §2·S2 Archival opportunities | Beat 2.4. Claim: Ford hire "circa 1905," patternmaker role. Source basis: approximate, unconfirmed. | Confirm exact hiring date + initial title from Ford/Piquette employment records; replace "circa." | Script inheritance: approximate date propagates as fact. Lineage: partnership-start node imprecise. |
| V-3.2 | NEEDS_REVISION | §2·S3 Narrative risks; §8 R2 | Beat 3.2. Claim: 1908 Piquette chassis-drag experiment. Source basis: Sorensen memoir; date + primacy disputed by historians. Interested-witness source. | Present as contested; cite memoir AND ≥1 dissenting historian per R2 skepticism rule; do not assert as settled. | Audit: single-source contested claim. Script inheritance: primacy risk (R2 over-heroization) if unqualified. |
| V-3.4a | FAIL | Amendment §2/S3-A1; §2·S3 Geopolitical relevance | Beat 3.4. Flag reads "foreign press and doctrinal citations of Fordism." Approved amendment §2/S3-A1 scopes S3.4 [VERIFY] to DOMESTIC contemporary evidence only; global/export reserved to 4.5/7.3/7.4/8.2. Flag wording contradicts locked v1.1 spec. Residual drift beyond prior validation-report FAIL. | Reword flag to domestic contemporary evidence (wages/consumption/company-control/social reception); remove "foreign press/doctrinal." Align to §2/S3-A1. | Lineage: semantic drift inherited by all downstream scripts/audit docs. Audit: direct non-conformance with locked spec v1.1. |
| V-3.5 | NEEDS_REVISION | §2·S3 Archival opportunities; §2·S3 Emotional function | Beat 3.5. Claim: 1913–14 press crediting Ford alone. Source basis: "to be pulled." No clippings sourced. | Pull dated 1913–14 press items; cite publication + date to substantiate "first theft." | Audit: thesis-beat (first theft) unsupported. Script inheritance: uncited attribution. |
| V-4.2 | NEEDS_REVISION | §2·S4 Purpose; §4 milestone table | Beat 4.2. Claim: ~$50M V-8 retooling bet. Source basis: memoir + secondary; primary financials unconfirmed. Figure recurs in logline + §4 table. | Confirm $50M against primary Ford financial records; cite. Flag as memoir-derived until then. | Lineage: keystone figure propagates to logline/§4 table unverified. Audit: financial-claim gap. |
| V-4.3 | NEEDS_REVISION | §2·S4 Archival opportunities | Beat 4.3. Claim: scrap rates, failure timeline, "3,000/day." Source basis: to be sourced from Rouge foundry records + memoir. | Source scrap/failure data + production rate from foundry records; cite. | Script inheritance: throughput drumbeat #2 numbers uncited. Audit: production-data gap. |
| V-4.4 | NEEDS_REVISION | §2·S4 Narrative risks; §8 R3; §5 Labor dynamics | Beat 4.4. Claim: Service Dept scale/composition (ex-boxers/convicts/informers). Source basis: memoir literature; "beyond memoir" corroboration absent. | Source Service Dept scale from non-memoir record; retain as antagonist seed per R3, cited. | Audit: antagonist-seed (R3) single-source. Lineage: labor-counterweight (§5) evidence gap. |
| V-4.5a | NEEDS_REVISION | §2·S4 Geopolitical relevance; §5 Export logic | Beat 4.5. Claim: Sorensen Ford-of-Europe oversight scope/dates (Dagenham, Cologne). Source basis: unconfirmed scope/dates. | Confirm oversight role scope + dates from Ford-of-Europe records; cite. | Lineage: export-logic thread (§5) origin node unverified. |
| V-4.5b | NEEDS_REVISION | §5 Export logic; §8 R4 | Beat 4.5. Claim: Soviet technical-assistance contracts; German industrial adoption. Source basis: citations to be sourced. Per §5, acknowledge "briefly, factually." | Source specific Soviet contract + German adoption citations; keep brief/factual per §5, avoid R4 over-tangent. | Audit: export-reach claim uncited. Script inheritance: geopolitics risk if unsourced. |
| V-5.2a | NEEDS_REVISION | §2·S5 Purpose; §2·S5 Archival opportunities | Beat 5.2. Claim: Willow Run "largest single industrial building under one roof." Source basis: superlative unconfirmed. | Confirm superlative against wartime construction records; else restate as "among the largest." | Audit: superlative-claim gap. Script inheritance: absolute claim propagates. |
| V-5.2b | NEEDS_REVISION | §2·S5 Industrial function; §8 R1 | Beat 5.2. Claim: B-24 ">400,000 parts." Source basis: figure varies across sources. | Adopt one sourced parts-count with citation; note variance range. | Script inheritance: contested figure inherited as fixed. |
| V-5.3 | NEEDS_REVISION | §2·S5 Industrial function; §8 R2 | Beat 5.3 (MIDPOINT). Claim: overnight San Diego hotel-room Willow Run sketch. Source basis: principally memoir; corroboration absent. Interested-witness, film's centerpiece. | Seek corroboration; if none, present as memoir-attributed per R2 visible-skepticism rule; do not assert as fact. | Audit: midpoint keystone single-source. Lineage: highest-weight uncorroborated node. |
| V-5.4a | NEEDS_REVISION | §2·S5 Narrative risks | Beat 5.4. Claim: press coinage "Willit Run?". Source basis: attribution + first-print unconfirmed. | Source coinage attribution + first print appearance; cite. | Audit: attribution gap. |
| V-5.4b | NEEDS_REVISION | §2·S5 Archival opportunities | Beat 5.4. Claim: Lindbergh diary passages on Willow Run dysfunction. Source basis: passages to be cleared + cited. | Clear rights + cite specific diary passages (date/page). | Script inheritance: uncleared quotation. Audit: rights + citation gap. |
| V-5.5 | NEEDS_REVISION | §2·S5 Purpose; §4 milestone table | Beat 5.5. Claim: "B-24 every 63 min." Flag concedes sustained one-per-hour documented at PEAK 1944 — after S5's 1943 close. Temporal-scope conflict: apex figure dated outside section span; logline + §4 table carry 63-min as S5 apex. | Add on-screen date qualifier (1944 peak) OR rescope S5 boundary note; prevent false 1943 attribution. Handle timeline honestly per flag. | Lineage: temporal metadata mismatch inherited by §4 table + logline. Audit: date-integrity defect. |
| V-6.1 | NEEDS_REVISION | §2·S6 Narrative risks; §3 Edsel spine; §8 R2 | Beat 6.1. Claim: Sorensen acted against Edsel's programs. Source basis: "beyond memoir self-defense" absent. Required for culpability per R2. | Document specific episodes from non-memoir sources; cite to support culpability (not martyrdom). | Audit: culpability thesis (R2/S6 risk) single-source. |
| V-6.2a | NEEDS_REVISION | §2·S6 Purpose | Beat 6.2. Claim: Henry Ford cognitive decline (strokes, extent, dating). Source basis: to be sourced from medical/biographical records. | Source decline extent + dating from medical/biographical record; cite. | Script inheritance: medical claim propagates unverified. |
| V-6.2b | NEEDS_REVISION | §2·S6 Purpose; §8 R3 | Beat 6.2. Claim: Service Dept dismissals "by men with pistols." Source basis: specific episodes unsourced. | Source specific dismissal episodes; cite per R3 realized-antagonist requirement. | Audit: antagonist-realization (R3) evidence gap. |
| V-6.3 | NEEDS_REVISION | §2·S6 Geopolitical relevance; §5 WWII mobilization | Beat 6.3. Claim: federal intervention/takeover contemplation; War Dept correspondence. Source basis: "secondary literature varies." | Source precise federal options + correspondence; cite; note where literature diverges. | Lineage: national-security altitude (§5) claim unverified. Audit: contested-claim gap. |
| V-6.4 | NEEDS_REVISION | §2·S6 Purpose | Beat 6.4. Claim: HFII 1943 Navy release + lobbying. Source basis: to be documented. | Document HFII release circumstances + lobbying; cite. | Script inheritance: succession-pivot fact unverified. |
| V-6.5 | NEEDS_REVISION | §2·S6 Emotional function; §8 R2 | Beat 6.5. Claim: 1944 forced-exit mechanics (Florida phone call). Source basis: heavily Sorensen's own account; self-flagged open research question. | Corroborate exit sequence/causes from non-memoir sources; present as open per R2 until resolved. | Audit: false-belief-shatter keystone single-source. Lineage: open-question node must not lock. |
| V-6.6 | NEEDS_REVISION | §2·S6 Archival opportunities; §3 Bennett spine | Beat 6.6. Claim: HFII "You're through" wording to Bennett, Sept 1945. Source basis: participant recollections. | Source wording + attribution; present as recollected, cite participants. | Script inheritance: quoted line propagates as verbatim. Audit: recollection-source gap. |
| V-7.1 | NEEDS_REVISION | §2·S7 Purpose; §4 milestone table | Beat 7.1. Claim: Willys titles/dates (1944 presidency → later vice-chairmanship). Source basis: unconfirmed sequence. | Confirm exact Willys titles + dates; cite corporate records. | Lineage: second-life timeline nodes imprecise. |
| V-7.2 | NEEDS_REVISION | §2·S7 Archival opportunities; §6 register map | Beat 7.2. Claim: CESOR Farm demonstration footage/photos. Source basis: family-held, extent/condition unconfirmed; "likely archival exclusive." | Inventory + condition-survey CESOR assets; register custody before exclusive claim. | Ingestion: exclusive asset unregistered. Audit: holdings-verification gap. |
| V-7.3a | NEEDS_REVISION | §2·S7 Purpose; §6 register map | Beat 7.3. Claim: yacht *Helene* ownership/dates. Source basis: vessel records to be confirmed. | Confirm vessel registry + ownership dates; cite. | Lineage: private-empire asset node unverified. |
| V-7.3b | NEEDS_REVISION | §5 Caribbean capital strategy; §2·S7 Geopolitical relevance | Beat 7.3. Claim: Cuban + Virgin Islands holdings acquisition/scale/operations. Source basis: to be documented from estate/land records. | Source acquisition dates + scale + operations from land/estate records; cite. Frame as systemic per §5. | Lineage: expropriation setup (§5) unsupported. Audit: property-record gap. |
| V-7.4 | NEEDS_REVISION | §5 Expropriation; §2·S7 Emotional function | Beat 7.4. Claim: 1959 Castro expropriation of Sorensen Cuban estate. Source basis: records + specific property fate "open research question." Film's emotional keystone (§5). | Source expropriation records + specific property fate; cite. Do not assert specific fate until confirmed. | Audit: keystone (§5 emotional keystone) unverified. Lineage: highest-weight geo node open. |
| V-7.5 | NEEDS_REVISION | §8 R2; §2·S1/S8 memoir | Beat 7.5. Claim: *My Forty Years with Ford* pub 1956; Samuel T. Williamson collaboration. Source basis: to confirm vs edition record. | Confirm pub date + Williamson credit against edition; cite. Retain source+exhibit framing per R2. | Script inheritance: bibliographic fact propagates to S1/S8 memoir references. |
| V-8.1a | NEEDS_REVISION | §2·S8 Purpose | Beat 8.1. Claim: death "August 1968, Bethesda, Maryland." Source basis: specific, to be confirmed vs death records. Prose asserts specifics inside flag. | Confirm date + place against death record; cite. Hold specifics as provisional until confirmed. | Lineage: terminal-timeline node asserted-but-unverified. Audit: vital-record gap. |
| V-8.1b | NEEDS_REVISION | §2·S8 Archival opportunities | Beat 8.1. Claim: obituary brevity/framing ("aide/lieutenant"). Source basis: clippings to be pulled; brevity claim must rest on actual clippings. | Pull actual obituaries; cite lengths/framings. Brevity thesis unsupported until clippings in hand. | Audit: "brevity is evidence" thesis uncited. Script inheritance: characterization propagates. |
| V-8.1c | NEEDS_REVISION | §2·S8 Archival opportunities | Beat 8.1. Prose asserts "a name misspelled somewhere"; flag mandates instance be "found, not assumed." Prose pre-asserts unverified specific — violates retrieval-safe/no-assumption discipline. | Convert prose to conditional; assert misspelling only after a located, cited instance; else remove. | Audit: speculative assertion in locked prose. Lineage: assumption would inherit downstream as fact. |
| V-8.2 | NEEDS_REVISION | §5 Post-war industrial geopolitics; §2·S8 Geopolitical relevance | Beat 8.2. Claim: Toyota Production System lineage to Ford methods. Source basis: to be sourced precisely. | Source TPS→Ford-method lineage precisely; cite. Avoid over-claim of direct derivation. | Audit: legacy-verdict claim uncited. Script inheritance: causal lineage propagates. |
| V-8.3 | NEEDS_REVISION | §2·S8 Purpose; §8 R5 | Beat 8.3. Prose asserts absence of Danish commemoration ("no square, no bust, no schoolbook page"); flag states actual state "to be established by 2026 shoot — report what it finds." Prose pre-commits negative outcome before capture. | Restate as pending 2026-shoot finding; report what is found, not the structure's preferred null result (§8 R5 false-resolution guard). | Audit: pre-asserted unverified outcome. Script inheritance: null finding would lock prematurely. |
| V-8.4 | PASS | §3 Family spine; §2·S8 Emotional function | Beat 8.4. Verité custodian moment. Flag correctly scoped: explicitly contingent on 2026 shoot, "staged nothing, directed nothing — uses what occurs." No unverified fact pre-asserted; retrieval-safe primary-capture directive, spec-conformant. | — | Ingestion: primary-capture asset, register post-shoot. Lineage: clean — no inherited claim. Audit: conformant. |

## 5. DOWNSTREAM INHERITANCE MAP

| ITEM_ID | INGESTION_IMPACT | LINEAGE_IMPACT | SCRIPT_INHERITANCE_IMPACT | AUDIT_IMPACT |
|---|---|---|---|---|
| V-1.2a | Asset unregisterable until inventory performed. | No provenance chain to originator. | No script-facing claim until asset registered. | Holdings gap logged pending inventory. |
| V-1.2b | Ephemera assets unregisterable pre-manifest. | No custody/date metadata chain. | No script use until manifest exists. | Uncounted-holdings gap. |
| V-1.2c | Memoir-excerpt asset gated on rights. | Citation chain to edition/page absent. | Quoted text propagates uncleared into script/VO. | Rights-clearance gap. |
| V-1.3 | Ledger asset gated on archival retrieval. | Denmark→America loop (S1 geo) unsupported. | Specific-entry claim withheld until cited. | Primary-record gap. |
| V-2.1 | Manifest asset gated on retrieval. | Origin timeline node unverified; S2 dates inherit uncertainty. | Departure-year claim held provisional. | Primary-record gap. |
| V-2.4 | Employment-record asset gated. | Partnership-start node imprecise. | "Circa 1905" propagates as fact — block until exact date. | Timeline-imprecision flag. |
| V-3.2 | Memoir-derived claim tagged contested. | Chassis-drag node single-source. | Primacy risk (R2) if unqualified — carry contested tag. | Single-source contested claim. |
| V-3.4a | Flag blocked from registry until reworded. | Geo-scope semantic drift inherited by all downstream scripts/audit docs. | Foreign-scope wording propagates against §2/S3-A1 — halt. | Direct non-conformance with locked spec v1.1. |
| V-3.5 | Press-clipping assets pending pull. | First-theft thesis node uncited. | Uncited attribution propagates. | Thesis-beat unsupported. |
| V-4.2 | Financial-record asset gated. | $50M keystone propagates to logline + §4 table unverified. | Figure inherited across script unverified. | Financial-claim gap. |
| V-4.3 | Foundry-record assets pending. | Throughput node uncited. | Drumbeat #2 numbers propagate uncited. | Production-data gap. |
| V-4.4 | Service-Dept claim tagged memoir-derived. | Labor-counterweight (§5) evidence gap. | Antagonist-seed carries single-source tag. | Antagonist-seed (R3) single-source. |
| V-4.5a | Ford-of-Europe records gated. | Export-logic (§5) origin node unverified. | Oversight scope/dates held provisional. | Primary-record gap. |
| V-4.5b | Soviet/German citation assets pending. | Export-reach node uncited. | Geopolitics risk (R4) if unsourced. | Export-reach claim uncited. |
| V-5.2a | Construction-record asset gated. | Superlative node unverified. | Absolute "largest" claim propagates. | Superlative-claim gap. |
| V-5.2b | Parts-count source pending selection. | Parts-count node variance unresolved. | Contested figure inherited as fixed. | Uncited/variant-figure gap. |
| V-5.3 | Hotel-sketch claim tagged memoir-attributed. | Highest-weight uncorroborated node (midpoint). | Midpoint carries memoir-attributed tag (R2). | Midpoint keystone single-source. |
| V-5.4a | Coinage source pending. | "Willit Run?" node uncited. | Coinage propagates unattributed. | Attribution gap. |
| V-5.4b | Lindbergh diary asset gated on rights. | Diary-passage citation absent. | Uncleared quotation propagates. | Rights + citation gap. |
| V-5.5 | 63-min figure tagged temporal-conflict. | Temporal metadata mismatch inherited by §4 table + logline. | 63-min risks false 1943 attribution — require date qualifier. | Date-integrity defect. |
| V-6.1 | Non-memoir episode sources pending. | Culpability node single-source. | Culpability beat (R2) carries single-source tag. | Culpability thesis single-source. |
| V-6.2a | Medical/biographical records gated. | Decline node unverified. | Medical claim propagates unverified. | Primary-record gap. |
| V-6.2b | Dismissal-episode sources pending. | Antagonist-realization node single-source. | Dismissal claims carry unsourced tag. | Antagonist-realization (R3) evidence gap. |
| V-6.3 | War Dept correspondence gated. | National-security altitude (§5) claim unverified. | Federal-intervention claim provisional; note literature divergence. | Contested-claim gap. |
| V-6.4 | HFII Navy-release records gated. | Succession-pivot node unverified. | HFII release fact propagates unverified. | Primary-record gap. |
| V-6.5 | Exit-mechanics corroboration pending. | Open-question node must not lock. | Exit sequence carries open-question/memoir tag (R2). | False-belief-shatter keystone single-source. |
| V-6.6 | Participant-recollection source pending. | "You're through" node recollection-based. | Quoted line propagates as verbatim — tag recollected. | Recollection-source gap. |
| V-7.1 | Willys corporate records gated. | Second-life timeline nodes imprecise. | Titles/dates held provisional. | Timeline-imprecision flag. |
| V-7.2 | CESOR exclusive asset unregistered pending survey. | No custody chain for exclusive. | Exclusive claim withheld until registered. | Holdings-verification gap. |
| V-7.3a | Vessel registry gated. | Private-empire asset node (Helene) unverified. | Ownership dates held provisional. | Primary-record gap. |
| V-7.3b | Land/estate records gated. | Expropriation setup (§5) unsupported. | Holdings scale/operations provisional; frame systemic per §5. | Property-record gap. |
| V-7.4 | Expropriation records gated. | Highest-weight geo node (§5 keystone) open. | Specific property fate withheld until confirmed. | Keystone unverified. |
| V-7.5 | Edition record gated. | Memoir bibliographic node propagates to S1/S8. | Pub date/Williamson credit inherited across memoir refs. | Bibliographic-record gap. |
| V-8.1a | Death record gated. | Terminal-timeline node asserted-but-unverified. | Date/place held provisional. | Vital-record gap. |
| V-8.1b | Obituary clippings pending pull. | "Brevity is evidence" node uncited. | Aide/lieutenant characterization propagates. | Uncited-thesis gap. |
| V-8.1c | No asset; claim gated on located instance. | Assumption would inherit downstream as fact. | Misspelling claim must convert to conditional. | Speculative assertion in locked prose. |
| V-8.2 | TPS-lineage sources pending. | Legacy-verdict node uncited. | Causal Toyota→Ford lineage propagates. | Legacy-verdict claim uncited. |
| V-8.3 | 2026-shoot capture pending. | Commemoration-state node pre-asserted. | Null finding would lock prematurely — restate pending. | Pre-asserted unverified outcome. |
| V-8.4 | Primary-capture asset; register post-shoot. | Clean — no inherited claim. | No pre-asserted claim; conformant. | Conformant. |

## 6. CIC_SPEC_V1.1_INTEGRITY_CHECK

| CHECK | RESULT | EVIDENCE |
|---|---|---|
| All FAIL + NEEDS_REVISION units map to ≥1 defect class | PASS | 38 defect-bearing units (1 FAIL + 37 NEEDS_REVISION); defect-class membership sum = 2+12+9+7+3+2+2+1+1 = 38. Full coverage. |
| No PASS unit appears in any defect class | PASS | V-8.4 (sole PASS) absent from all 10 defect-class rows. |
| No item in multiple classes except explicit secondary | PASS | Only multi-class entry: V-3.4a (SPEC_NONCONFORMANCE primary; GEO_SCOPE_DRIFT secondary, explicitly listed). All other 37 units appear in exactly one class. |
| No semantic drift vs Spec v1.1 / amendment §2/S3-A1 | PASS | Statuses, SPEC_REFs, provenance notes, corrections, impacts reproduced verbatim. V-3.4a FAIL preserved (domestic-only scope enforced per §2/S3-A1). No FAIL/NEEDS_REVISION softened. |

INTEGRITY_STATUS: CLEAN (4/4 checks PASS)

## 7. CIC_REGISTRY_READY_V1.1

**REGISTRY-READY (PASS — 1):**
- V-8.4

**BLOCKED — FAIL, correction mandatory before registry (1):**
- V-3.4a

**REQUIRES CORRECTION — NEEDS_REVISION, gated from registry (37):**
- V-1.2a, V-1.2b, V-1.2c, V-1.3, V-2.1, V-2.4, V-3.2, V-3.5, V-4.2, V-4.3, V-4.4, V-4.5a, V-4.5b, V-5.2a, V-5.2b, V-5.3, V-5.4a, V-5.4b, V-5.5, V-6.1, V-6.2a, V-6.2b, V-6.3, V-6.4, V-6.5, V-6.6, V-7.1, V-7.2, V-7.3a, V-7.3b, V-7.4, V-7.5, V-8.1a, V-8.1b, V-8.1c, V-8.2, V-8.3

REGISTRY_ADMISSION: 1 admitted · 38 gated (1 FAIL + 37 NEEDS_REVISION) · total 39
