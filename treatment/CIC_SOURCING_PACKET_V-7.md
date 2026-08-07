# CIC_SOURCING_PACKET_V-7 — Willow Run New-Source Intake (trm-vault `charlie/willow-run`)

STATUS: OPEN
Tagged to: TREATMENT_DRAFT_v1.3.md Section 5 (THE ARSENAL) · cross-links V-5.2a, V-5.2b, V-5.3 (KEYSTONE, BLOCKED), V-5.4a, V-5.5
Source batch: trm-vault `charlie/willow-run`, 589 files ingested (commit `c05b3a2`), extract→score→crosslink→report run 2026-08-07 (trm-vault commit `0ec0cbc`). 126 facts extracted (all text sources; 589 image sources skipped — no OCR text path), 54 promoted (score ≥80). All 126 came back `unmatched` against the current dependency map — no beat in Section 5 currently cites these sources, hence this packet.
Sources: SRC-001 = "Michigan Flight Museum — Sorensen Photo Archive Log" (catalog/finding aid, Julie Osborne, Curatorial Director). SRC-473 = "Sorensen Research - 2026-04-22 - Willow Run.docx" (intake compilation, no further origin metadata). SRC-474 = "Sorensen Research - 2026-05-01 - Willow Run.docx" (intake compilation, no further origin metadata). SRC-473/474 are internal research compilations, not named published works — their own within-document citations (if any) still need pulling before either can be treated as more than a secondary/tertiary lead. This is more acute than "secondary source": the packet cannot yet confirm these docs cite anything at all.

## 1. Priority Item — KEYSTONE CONFLICT with V-5.3

Beat 5.3 (the film's literal midpoint) is currently **BLOCKED, SINGLE_SOURCE_RISK, KEYSTONE**: the hotel-room sketch account (San Diego, January 1941, insomnia, sketches Willow Run's layout overnight after touring Consolidated) rests solely on Sorensen's own memoir.

**FCT-093** (SRC-474, confidence 0.95, promotion_score 80, promoted): *"Sorensen conceived the initial layout for the Willow Run bomber plant while aboard his personal yacht, the M/Y Helene, in early 1941."*

This is a **different origin story** — yacht, not hotel room — from a source independent of the memoir. It does not corroborate V-5.3's existing account; it contradicts its setting. Two readings:

- If SRC-474 is itself just repeating a garbled/conflated version of the memoir story (popular secondary accounts do this), it's not independent corroboration — it's noise, and should be CONTESTED-TAG at most.
- If SRC-474 has its own sourcing for the yacht claim, this is a second, materially different candidate origin scene, and the packet's BLOCKED status can't resolve until Tier 1 decides which (or both, or neither) is admissible.

Also relevant: **FCT-041** (SRC-473, confidence 0.95, promoted) confirms the San Diego/Consolidated trip itself ("In late 1940 or early January 1941, Charles Sorensen and Edsel Ford traveled to San Diego to tour Consolidated Aircraft's B-24 production facility") and **FCT-042** (SRC-473, promoted) corroborates the craft-friction detail already in Draft v1.3 beat 5.3/5.2 ("assembly conducted outdoors under the California sun on structural steel fixtures distorted by heat, making it impossible to produce two planes alike"). These two support the *existing* hotel-room framing's setup (the San Diego trip happened, the craft-culture collision was real) without resolving where the sketch itself was actually drawn.

**Action required before any prose change to 5.3:** identify SRC-474's underlying source for the yacht claim. Do not silently fold FCT-093 into the beat — this is a genuine fork in the keystone scene, not a confirmation. Recommend Tier 1 review alongside the existing BFRC Box 47/2673/106/165 plan.

## 2. Corroboration Candidates for Existing VERIFY Tags

| Beat tag | Current status | New fact | Assessment |
|---|---|---|---|
| V-5.2a (largest building superlative) | UNCITED_ASSERTION | FCT-100 (SRC-474, promoted): "Willow Run was the largest enclosed factory in the world." FCT-081 (SRC-473, promoted): exact dimensions, 3.5M sq ft, 3,200+ ft long, 1,279 ft wide. | Two independent secondary sources now state the superlative with matching scale figures. Still secondary, not primary — moves toward CONTESTED-TAG, not ADMITTED. |
| V-5.2b (parts count) | UNCITED_ASSERTION | FCT-086 (SRC-473, not promoted, conf 0.92): "450,000 parts, 360,000 rivets." FCT-046 (SRC-473, not promoted, conf 0.9): "488,193 parts, 30,000 components." | The two new figures **conflict with each other** (450K vs 488K parts) as well as with Draft v1.3's own "over four hundred thousand." Do not resolve by picking one — flag the range as itself the finding; needs a primary aircraft-spec source, not another secondary count. |
| V-5.4a ("Willit Run" coinage) | UNCITED_ASSERTION | FCT-054 (SRC-473, conf 0.92): "Critics in Washington mockingly called the Willow Run plant 'Will It Run.'" FCT-107 (SRC-474, promoted, conf 0.98): "...critics derisively call the facility 'Will-It-Run.'" | Two independent sources confirm the phrase existed and was contemporary. Neither gives a first-print citation or byline — coinage/attribution still open, but the phrase itself is now CONTESTED-TAG corroborated (2+ secondary sources, no primary yet). |
| V-5.5 (63-minute production rate, flagged as 1944 forward-reference) | TEMPORAL_INTEGRITY note, not a blocking defect | FCT-056 (SRC-473, promoted, conf 0.95): "By 1944, the Willow Run line was producing one B-24 every 55–63 minutes." FCT-103 (SRC-474, promoted, conf 0.98): "At peak production in 1944, Willow Run completed one B-24 Liberator every 63 minutes." | Both new sources confirm the 63-minute figure is specifically a 1944 peak number — matches and reinforces the existing on-screen framing that this is a forward reference, not a fact-in-period for the 1941–43 section. No prose change needed; this is confirmation the current caveat is correctly worded. |

## 3. New Material — Not Currently in Any Beat

**Distinguished-visitor material (SRC-001, Michigan Flight Museum photo catalog).** None of these visits currently appear anywhere in Draft v1.3. Confidence is high (photo-catalog metadata, several independently corrected from prior miscataloging by this same research effort — FCT-006/007/008/010/011 document the correction work itself). Candidates for 5.1–5.6 enrichment, roughly chronological:

- Oct 13, 1941 — Sperry Gyroscope / bombsight visit (FCT-016)
- Apr 13, 1942 — Sen. Harry Truman, Truman Committee inspection, plant still under construction (FCT-017, FCT-018)
- May 29, 1942 — Maj. Gen. George H. Brett, William S. Knudsen, Edsel Ford (FCT-019, FCT-020)
- Jul 16, 1942 — Sorensen, Harlow Curtice, Doolittle examine Pratt & Whitney R-1830 at Buick Melrose Park (FCT-021, FCT-022, FCT-024)
- Jul 24, 1942 — Crown Prince Olaf of Norway (later King Olav V) (FCT-026)
- Jul 31, 1942 — Charles Lindbergh visits Ford/GPD Inc. with an RAF officer present (FCT-027) — supplements the existing 5.4 Lindbergh diary reference with a dated appearance and Allied-coordination angle
- Sep 1942 — FDR visits, B-24s lined up on tarmac (FCT-029)
- Oct 17, 1942 — Chinese Military Mission, Gen. and Madame Hsiung Shih-hui (FCT-030, FCT-031, FCT-032)
- Nov 20, 1942 — Lt. Gen. Knudson, Maj. Gen. Echa line inspection (FCT-033)
- Jul 1943 — Joseph C. Grew (former Ambassador to Japan) tours Buffalo production facility with Sorensen (FCT-034, FCT-035)
- Apr/Sep 1943 — Henry Ford I + Treasury Secretary Morgenthau Jr. at Willow Run tarmac (FCT-036, FCT-037)

None of these are individually load-bearing to the film's spine, but several (FDR, Truman, Olaf, Chinese Mission) are strong visual/B-roll candidates for 5.1/5.4/5.6 and corroborate the "government men enter the story and stay" framing already in 5.1 prose. Recommend a follow-up editorial pass (not sourcing) to select 2–3 for beat inclusion.

**Willow Run Village / postwar labor material (SRC-473).** Not touched anywhere in current draft:

- FCT-058/059/060 — Stonorov's rejected communal-housing proposal for Willow Run workers
- FCT-061/062 — Willow Run Village scale (2,641 acres) and inadequate wartime housing despite $200M federal contribution
- FCT-064/065 — postwar: UAW Local 50 workers denied seniority when Kaiser-Frazer took over; employment collapsed 45,000 → 8,000 by 1953
- FCT-063 — Henry Ford II quoted: "Willow Run is as expendable as a battleship"

This is potential material for 5.4's existing "labor ledger stays open and honest" beat, or as a coda note on what happened to the plant/workforce after the war (currently outside the film's scope, which moves to Section 6 in 1943–44). Flagging for Tier 1 to decide relevance, not recommending insertion.

## 4. New Archival Leads

- **Bentley Historical Library, University of Michigan** — Willow Run photograph collection, call number 0030 UCCl, ca. 1941–1945, finding aid dated March 2020, open with no restrictions (FCT-089). Independent of BFRC — worth a research pass separate from the 2026-07-24 BFRC visit.
- **Mike Kroll Research Archive** — 400+ items of press/trade/archival material including "the rarest known Ford executive group portrait" per catalog description (FCT-090). Provenance and access terms unconfirmed — needs a scoping call before treating as a usable source.

## 5. Status Transition Rules

- §1 (yacht/hotel-room conflict): remains BLOCKED. Resolves only when SRC-474's own sourcing for the yacht claim is identified and evaluated — this packet cannot self-resolve it from the fact text alone.
- §2 rows: UNCITED_ASSERTION → CONTESTED-TAG once 2+ independent secondary sources agree (V-5.2a, V-5.4a now qualify). CONTESTED-TAG → ADMITTED still requires a primary source per the framework's general rule — none of §2's items clear that bar yet.
- §3/§4: informational, no registry status change. Editorial/archival follow-up, not sourcing-packet business.

## 6. Work Log

| Date | Action | Result |
|---|---|---|
| 2026-08-07 | trm-vault `charlie/willow-run` extract→score→crosslink→report run (126 facts, 54 promoted); `sync-treatment willow-run` executed against this repo (dry-run then real) | All 126 facts unmatched against dependency map — no existing V-x.y item targets willow-run sources. Packet opened to triage. |
| 2026-08-07 | Cross-referenced all 126 facts against Draft v1.3 Section 5 beats and existing VERIFY/V-x.y tags | Found one keystone-level conflict (§1, FCT-093 vs. V-5.3), four corroboration candidates for existing UNCITED_ASSERTION tags (§2), 20+ facts of new visitor/housing material not yet represented in any beat (§3), two new archival leads (§4). No prose changes made — packet is triage only, per scope decision. Next: Tier 1 review of §1 before any 5.3 edit; identify SRC-473/SRC-474 full citations (currently only source IDs, not titles, are on hand — pull from `trm-vault/topics/charlie/willow-run/sources/`). |
