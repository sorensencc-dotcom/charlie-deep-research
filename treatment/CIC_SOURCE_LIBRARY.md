# CIC Source Library

STATUS: ACTIVE (2026-07-17). Central index of every source located, read, or targeted across all
sourcing packets, the transcript sweep, and the BFRC box request. Not a source itself — a pointer
table. When you add a source anywhere else in this repo (packet work log, sweep file, box request),
add a row here in the same commit. Grep this file by V-item ID, source type, or status instead of
re-reading four separate work logs.

## How to use

- **By V-item:** `grep "V-5.3" CIC_SOURCE_LIBRARY.md`
- **By status:** `grep "TARGET-UNLOCATED" CIC_SOURCE_LIBRARY.md` — everything still needing a follow-up action
- **By type:** `grep "^| PRIMARY" CIC_SOURCE_LIBRARY.md`

## Status legend

| Code | Meaning |
|---|---|
| READ | Full text/content reviewed, findings extracted |
| HEADLINE-ONLY | Located (date/image/headline confirmed), full text not yet pulled |
| LOCATED-UNREAD | Physical box/folder confirmed via finding aid, contents not yet reviewed |
| TARGET-UNLOCATED | Named as a target in a packet's §2, not yet found or confirmed to exist |
| CONFIRMED | Independently verified, corroboration/contestation established |

## Type legend

PRIMARY (contemporary record, not authored by Sorensen or Bennett) · SECONDARY (later account, named
independent author) · TERTIARY (encyclopedic/aggregator, no cited primary) · SORENSEN-AUTHORED (memoir
or dictated transcript, same witness) · BENNETT-AUTHORED (opposing interested witness) · FAMILY-TREATMENT
(the two treatment drafts themselves — never corroboration, only a lead pointer)

## Source Table

| ID | Source | Type | Date | Status | V-items | Claim / relevance | Next action |
|---|---|---|---|---|---|---|---|
| S-001 | Ann Arbor Observer, "How Ford's Willow Run Assembly Plant Helped Win World War II," Don Sherman & Grace Shackman | SECONDARY | Jul 1995 | READ | V-5.3 | Independently corroborates San Diego/Consolidated trip, Edsel present, hotel-room sketch, breakfast, Reuben Fleet named as Consolidated president, "make the complete airplane or nothing" quote. Clears CONTESTED-TAG bar. | None — logged in packet 2026-07-17. Cite in beat 5.3. |
| S-002 | McAllen Daily Press, Jan 13 1941, Image 1 (Chronicling America) | PRIMARY | 1941-01-13 | HEADLINE-ONLY | V-5.3 | Caption "...H. Fleet, center, and Charles Sorenson, Ford production chief, right..." — S-001 confirms "H. Fleet" = Reuben Fleet. | Pull full article text via Chronicling America. |
| S-003 | Detroit Evening Times (Night Edition), Jan 9 1941, Image 6 | PRIMARY | 1941-01-09 | HEADLINE-ONLY | V-5.3 | "...head of Consolidated Charles E. Sorensen, Ford production manager, is traveling with the Ford party..." — third independent Jan-1941 outlet on the Consolidated trip. | Pull full text. |
| S-004 | Evening Star (Washington DC), Jan 9 1941, Image 11 | PRIMARY | 1941-01-09 | HEADLINE-ONLY | V-5.3 | Headline "Ford Studying Plan For Mass Production Of Giant Bombers" — matches the exact contemporary announcement window. | Pull full text. |
| S-005 | Evening Star (Washington DC), Aug 23 1942, Image 29 | PRIMARY | 1942-08-23 | HEADLINE-ONLY | V-5.3 | "Returning to their hotel room Mr. Ford, Mr. Sorensen and the engineer swapped ideas..." — literal hotel-room scene but wrong date (Aug 1942, not the ~1941 genesis window). Do not conflate without reading full text. | Pull full text; determine if unrelated event or memoir-scene relocation. |
| S-006 | Ypsilanti Daily Press, Sep 12 1941, Image 1 | PRIMARY | 1941-09-12 | HEADLINE-ONLY | V-5.2a, V-5.3(adjacent) | "Tool, Die Men Already Work on Bomber Parts" — construction-timeline corroboration, local paper. | Pull full text. |
| S-007 | Evening Star (Washington DC), Aug 28 1942, Image 5 | PRIMARY | 1942-08-28 | HEADLINE-ONLY | V-5.2a, V-5.5 | "...at Willow Run. Charles E. Sorenson, vice president and general manager of the Ford..." | Pull full text. |
| S-008 | BFRC Acc. 38, Box 106 — 1946 manuscript "Innovations in Aircraft Manufacturing and Assembly Procedures," William A. Simonds | SECONDARY (independent authorship) | 1946 | LOCATED-UNREAD | V-5.3 | Highest-value unread lead — independent author, on-topic subject. | Priority read at 2026-07-24 BFRC visit. |
| S-009 | BFRC Acc. 6, Box 165 — Edsel Ford Papers, Willow Run site development | PRIMARY (independent) | — | LOCATED-UNREAD | V-5.3 | Strongest independent-witness candidate for the breakfast/sketch scene (Edsel's own papers). | Priority read at 2026-07-24. |
| S-010 | BFRC Acc. 38, Box 89 — Government Work/Bomber Plant folder | SORENSEN-AUTHORED | — | LOCATED-UNREAD | V-5.3 | Background, same witness. | Read at 2026-07-24, lower priority. |
| S-011 | BFRC Acc. 65, Box 67 — "Engineering Design and Philosophy" | SORENSEN-AUTHORED | — | LOCATED-UNREAD | V-5.3 | Sorensen's own reminiscence, may have more detail than 1956 memoir. | Read at 2026-07-24, lower priority. |
| S-012 | BFRC Acc. 796, Box 1 — Sorensen's B-24 production compilation | SORENSEN-AUTHORED | — | LOCATED-UNREAD | V-5.3 | Background, same witness. | Read at 2026-07-24, lower priority. |
| S-013 | BFRC Acc. 285, Box 2607 — Willow Run Bomber Plant Property (Ford's own office files) | PRIMARY (independent) | — | LOCATED-UNREAD | V-5.3 | Independent of Sorensen. | Read at 2026-07-24. |
| S-014 | BFRC Acc. 823, Box 4 — P.E. Martin papers | PRIMARY (independent) | — | LOCATED-UNREAD | V-2.4 (adjacent) | Scope note: "In 1908, Charles Sorensen became Martin's assistant" — conflicts with treatment's "circa 1905" framing; transcript (S-020) says "middle of 1904." Three different dates now in play. | Read at 2026-07-24; reconcile with S-020. |
| S-015 | Bombard interview transcript, BFRC Acc. 64.167.65, dictated 1952-54, digitized 2023 | SORENSEN-AUTHORED (earlier record than memoir) | 1952-54 | READ | V-5.3, V-6.5, V-2.4, V-6.2a, V-3.2, V-4.2, V-4.5a/b, V-5.5 | Full-text ingested via toolforge-pdf. Sketch anecdote (pp.784, 807-820) names Reuben Fleet directly, contradicts memoir's "napkin"/hotel-room-only framing — matches S-001/S-002/S-003 (San Diego/Consolidated), not the memoir. Also: V-2.4 hire date "middle of 1904" (p.44); V-6.2a three stroke dates (1933/1938/1941); V-3.2 Piquette chassis-drag dated July 1908; V-4.2 $50M V-8 figure verbatim; V-4.5a/b Europe/Soviet/German chapter-length; V-5.5 negative result (only "one per hour," never "63 minutes," through Mar 1944 exit). | None further — fully mined. Source JSON: `C:\dev\cic-ingestion\pdf\processed\64-167-65_SorensenCharlesE.json`. |
| S-016 | *My Forty Years with Ford*, Charles E. Sorensen w/ Samuel T. Williamson (1956) | SORENSEN-AUTHORED | 1956 | READ (excerpted) | V-5.3, V-6.5 | The original memoir — single-source basis for both keystone beats as currently drafted. Superseded in detail by S-015 for the sketch scene. | None — baseline source, already fully accounted for in both packets. |
| S-017 | CastIronCharlie_Treatment_v13_20260523.md (family/production treatment) | FAMILY-TREATMENT | 2026-05-23 | READ | V-5.3, V-6.5, V-6.2a(Willys dates), V-7.1, V-7.2(CESOR Farm) | Not a corroborating source itself — a lead pointer. Confirms CESOR Farm is real (2,000-acre New Hudson MI farm, Jeep CJ launch Jul 18 1945, AP-covered). Names Logan Miller oral history + Detroit Free Press/News Palladium (see S-018/S-019). HFII/Benson Ford "initialled the sketch" claim not yet independently sourced beyond this treatment. | Confirm HFII/Benson Ford breakfast witness account independently if possible. |
| S-018 | Logan Miller oral history (Ford executive, LOC/Ford Archives interviewer) | PRIMARY (independent, named) | — | TARGET-UNLOCATED | V-6.5 | Quoted in v13 (S-017): names Bennett's role directly — "brought about by Bennett's contact with Mr. Ford." Independent witness, exactly the class §3 admission bar needs. Web search (2026-07-17) could not locate transcript online. | Pull full transcript at BFRC or Ford Archives, 2026-07-24 or sooner if accessible remotely. |
| S-019 | Detroit Free Press, Mar 6 1944 ("Dismissal of Sorensen — No Surprise to Capital") + News Palladium, Mar 6 1944 | PRIMARY | 1944-03-06 | HEADLINE-ONLY (quoted in v13, full text not independently pulled) | V-6.5 | Corroborates the Oct 1943 functional-sidelining *timeline* (Free Press) but News Palladium explicitly declines to state a *cause* — clears timeline corroboration, not causal-mechanism corroboration per §3. | Pull full original text via Chronicling America/newspapers.com to confirm v13's quotes verbatim. |
| S-020 | Henry Ford Heritage Association (hfha.org) + Wikipedia — Dec 1943 retirement request / 1941 prior agreement | TERTIARY | — | READ, unresolved | V-6.5 | States Sorensen requested retirement Dec 1943 (citing a 1941 prior agreement with Ford), Ford's answer Mar 2 1944, formal effective Mar 13 1944. Repeated verbatim by Wikipedia. Underlying primary source for the "1941 agreement" claim not identified by either. Web search 2026-07-17 confirmed the claim is widely repeated but still uncited at the primary level. | Identify HFHA's/Wikipedia's underlying primary citation, or treat as CONTESTED-TAG only per §3. |
| S-021 | BFRC Acc. SE-007, Box 47 — Frank Campsall Records ("Correspondence — C.E. Sorensen fired, 1944 / Codicil to Henry Ford's will, 1944") | PRIMARY (independent) | 1944 | LOCATED-UNREAD | V-6.5 | Best candidate on the full list — Campsall was Ford's own secretary, independent of both Sorensen and Bennett; finding aid's own scope note states it covers "Ford's firing of C.E. Sorensen." | Highest priority read, 2026-07-24. |
| S-022 | BFRC Acc. 285, Box 2673 — H.H. Bennett's Office folder, physically adjacent to Willow Run material | PRIMARY (independent) | — | LOCATED-UNREAD | V-6.5 | Independent of both interested witnesses. | Priority read, 2026-07-24. |
| S-023 | BFRC Acc. 65, Box 69 — Sorensen's "Diary Notes; 1940-1944" | SORENSEN-AUTHORED | 1940-44 | LOCATED-UNREAD | V-6.5 | Likely location of the memoir's cited "p.912" Bennett-confrontation passage. Same witness, doesn't resolve single-source-risk alone. | Read for comparison, 2026-07-24. |
| S-024 | BFRC Acc. 13, Box 20 — Engineering Library Vertical File, "Sorenson, C.E., 1942-1944" | PRIMARY (independent) | 1942-44 | LOCATED-UNREAD | V-6.5 | Ford's own engineering-library newspaper-clippings compilation — independent of Sorensen, Bennett, Campsall. Could hold press beyond what's already cited. | Read, 2026-07-24, fourth priority behind S-021/S-022/S-023. |
| S-025 | Harry Bennett memoir, *We Never Called Him Henry* (1951) | BENNETT-AUTHORED | 1951 | TARGET-UNLOCATED (found on archive.org, borrow-only, full text not pulled) | V-6.5 | Opposing interested witness — triangulation only per §3, not sufficient alone for admission. | Library/archive.org loan needed to pull Sorensen-specific passages. |
| S-026 | FDR Presidential Library, Hyde Park NY | PRIMARY (target) | — | TARGET-UNLOCATED | V-6.5 | Possible correspondence re: Willow Run concerns / the reported offer for Sorensen to run Ford for the government. | Not yet searched. |
| S-027 | National Archives RG 18 / RG 342 | PRIMARY (target) | — | TARGET-UNLOCATED | V-6.5 | AAF internal correspondence re: Ford production management concerns, 1943 — referenced obliquely by Free Press reporting. | Not yet searched. |
| S-028 | BFRC Acc. 6 / Acc. 38, HFII-era executive correspondence | PRIMARY (target) | 1943-44 | TARGET-UNLOCATED | V-6.5 | Direct HFII/Bennett correspondence; Mead Bricker appointment paperwork (Dec 1942) as corroboration. | Not yet searched. |
| S-029 | Fortune magazine, 1944 follow-up (post "Sorensen of the Rouge") | SECONDARY (target) | 1944 | TARGET-UNLOCATED | V-6.5 | Possible retrospective on the departure. | Not yet searched. |
| S-030 | Find a Grave memorial #134073056 | SECONDARY (independent) | — | READ | V-8.1a | Resolves 3-way death-date discrepancy: death 11 Aug 1968, Bethesda MD; burial Woodlawn Park North, Miami FL. Not a primary vital record — PRIMARY_RECORD_GAP classification stands. | Still want an actual death certificate/vital record for full closure. |
| S-031 | *Detroit Times*, "SORENSEN QUITS FORD" | PRIMARY | 1944 | HEADLINE-ONLY | V-6.5 | Confirmed front-page 1944 departure story exists; distinct from the 1968 death obituary (V-8.1b), which is still unlocated (NYT paywalled). | Pull full text; separately still need the 1968 obituary for V-8.1b. |
| S-032 | *Automotive News* (Detroit), Mar 13 1944, Image 1 | PRIMARY | 1944-03-13 | HEADLINE-ONLY | V-6.5 | "Sorenson, Ford production genius, who parted company last week with the Ford empire he had served..." — contemporary trade-press framing of the exit, one week out. | Pull full text. |
| S-033 | *Detroit Evening Times* (Final Ed.), Mar 5 1944, Image 1 | PRIMARY | 1944-03-05 | HEADLINE-ONLY | V-6.5 | Headline "Illness Forces Sorensen to Quit — Ford's Production Genius Ends 39 Years With Company for Rest." A **third** causal framing beyond Sorensen's own account and Bennett's — contemporary "illness" narrative, published at the resignation date itself. High-value, not yet in either packet's own work log. | Pull full text; add explicitly to `CIC_SOURCING_PACKET_V-6.5.md` work log — packet currently only has Free Press/News Palladium/v13. |
| S-034 | *Detroit Evening Times* (Night Ed.), Oct 1 1942, Image 1 | PRIMARY | 1942-10-01 | HEADLINE-ONLY | V-6.3 | Headline "ROOSEVELT SECRET VISIT TO DETROIT PLANTS TOLD," names Edsel Ford, Sorensen, Bennett. First lead found for V-6.3 (federal-government-involvement) — prior transcript sweep found nothing on this item at all. | Pull full text — this is the only lead V-6.3 has. |
| S-035 | *Automotive News* (Detroit), May 31 1943, Images 1 & 5 | PRIMARY | 1943-05-31 | HEADLINE-ONLY | V-6.1, V-6.4, V-6.5 | Names HFII, Benson Ford, Sorensen, Eleanor Ford, Bennett together — five days after Edsel's death. Full contemporary snapshot of the succession-crisis cast in one place. | Pull full text. |
| S-036 | *Automotive News* (Detroit), Oct 6 1941, Image 11 | PRIMARY | 1941-10-06 | HEADLINE-ONLY | V-6.5 | Names Logan Miller (superintendent) alongside Sorensen — confirms S-018 (Miller's oral history) is a real contemporaneous colleague, not a loose attribution. | Supports S-018; no separate action needed beyond that pull. |
| S-037 | *Evening Star* (Washington DC), Jul 15 1930, Image 11 (AP wire) | PRIMARY | 1930-07-15 | HEADLINE-ONLY | V-4.5a | "'RED' FEAR MINIMIZED BY FORD PLANT HEAD" — names Sorensen "general manager of Europe," addresses communist-organizing fears at Ford's European plants. Independent AP wire source for his European title/role. | Pull full text (partially illegible scan). |
| S-038 | *The Butler County Press* (Hamilton OH), Aug 15 1930, Image 2 | PRIMARY | 1930-08-15 | HEADLINE-ONLY | new — not in the 37-item list (labor-politics context) | Sorensen testifying before the 1930 Fish Committee (House committee on communist activity). Not previously in any treatment draft or packet. | Flag to Tier 1 — is this worth a new V-item, or fold into V-4.5a/Section 4? |
| S-039 | *The Daily Worker* (Chicago/NY, CPUSA paper), Aug 2 1930, Image 6 | PRIMARY (hostile/opposing press) | 1930-08-02 | HEADLINE-ONLY | same as S-038 | Opposing-press coverage of the same Fish Committee hearing — independent of both Sorensen and Ford's friendly press. Two politically opposed outlets on the same event strengthens it as real. | Pull full text alongside S-038. |
| S-040 | *The Washington Herald*, Apr 4 1919, Image 4 | PRIMARY | 1919-04-04 | HEADLINE-ONLY | V-4.5b | Earliest press instance found (predates the 1930 record). Tractor-plant context, general manager title — lines up with the transcript's Amtorg chapter (first Soviet Fordson sale dated Mar 20 1919). | Pull full text. |
| S-041 | *The Sun* (New York), Oct 19 1919, Image 8 | PRIMARY | 1919-10-19 | HEADLINE-ONLY | general/biographical | Direct attributed quote: "Mr. Ford and I have worked long and..." — genuine period quote, not tied to a specific V-item. | Pull full text if a biographical-voice beat needs period-quote material. |
| S-042 | Executive-compensation press disclosures (multiple outlets, 1939/1944/1945) | PRIMARY | 1939-1945 | HEADLINE-ONLY | general/biographical (Act Two salary claims) | *Washington Daily News* Apr 7 1939 ($166,071); *Evening Star* Jul 17 1944 ($220,004.96); *Automotive News* Jun 12 1944 (clarifies 1944 figure is for calendar-year 1942); *Evening Star* Jun 25 1945 ($230,000, odd — over a year after he'd left Ford for Willys, unconfirmed if back-dated). Independent corroboration for v13's Act Two salary claims (Sorensen out-earning Edsel). | Pull Jun 25 1945 figure specifically to resolve the post-Ford timing oddity. |
| S-043 | *Willow Run: Colossus of American Industry*, Warren Benjamin Kidder | SECONDARY | — | READ (per v13's own citation) | V-5.2a, V-5.5, general Willow Run | Definitive plant history; explicitly credits Sorensen as designer/builder; cites Eighth Air Force's own production assessment. ISBN 0964720534. Cited throughout v13, not yet independently pulled by either packet. | Confirm packets cite this directly rather than only via v13. |
| S-044 | *Arsenal of Democracy*, A.J. Baime (2014) | SECONDARY | 2014 | READ (per v13's own citation, p.121 quoted) | V-6.5 (Bennett/Edsel confrontation) | Primary narrative source for the kidnap-plot/Bennett-charges-Edsel scene quoted in v13 Act Two. Likely the common source behind both v13's and the Ann Arbor Observer's (S-001) near-identical breakfast-scene wording — worth checking directly rather than assuming independence between S-001 and v13. | Read directly; check whether S-001 cites Baime as its own source (would demote S-001's independence). |
| S-045 | BFRC Acc. 65, Box 66 — Sorensen interview transcripts (Bombard series) | SORENSEN-AUTHORED | 1952-54 | Likely = S-015 | all items S-015 covers | v13 cites this as "not yet digitised for public access" — but S-015 (Acc. 64.167.65) was already real-extracted and read 2026-07-16. Same accession family; likely the same material v13's author hadn't yet seen digitized. | Confirm Box 66 vs. the digitized 64.167.65 file are the same material — resolve before citing both as separate. |
| S-046 | Henry Ford Heritage Association Wikipedia entry, "Charles E. Sorensen" | TERTIARY | — | READ | V-6.5 | Web search 2026-07-17 confirms Wikipedia states the same Dec-1943/1941-agreement claim as S-020 (HFHA), doesn't cite a primary source. Same unresolved gap as S-020 — not a separate corroboration. | Same action as S-020. |

## Disambiguation warning

**Theodore C. "Ted" Sorensen** (1928-2010), JFK's speechwriter, is a completely different person who shows up in "Sorensen" searches from the late 1950s onward (papers at the JFK Presidential Library). Confirmed false-positive hits: *Evening Star* Oct 10 1963, Mar 13 1960, Nov 22 1960. Any future search for "Sorensen" + political/Washington context from 1957+ must check the person is Charles E. Sorensen (b.1881, d.1968), not Ted Sorensen — birth year (1928) is the fastest check.

## Biographical / General Sources (not tied to a specific V-item)

| ID | Source | Type | Date | Status | Relevance |
|---|---|---|---|---|---|
| S-047 | *Evening Star*, Jan 13 1960, Image 42 | PRIMARY | 1960-01-13 | HEADLINE-ONLY | Late-life retrospective profile, age-78 matches real birth year — genuine, not the Ted Sorensen trap. |
| S-048 | *Evening Star*, Jun 6 1943, Image 27 | PRIMARY | 1943-06-06 | HEADLINE-ONLY | "Mr. Sorensen, who is 61" — age matches, genuine profile piece near the exit window. |
| S-049 | *Svět* (Czech-language, Cleveland OH), Dec 10 1921, Image 1 | PRIMARY | 1921-12-10 | HEADLINE-ONLY, untranslated | Earliest non-English press coverage found. OCR too garbled to transcribe reliably. |

## Open Follow-ups, Priority Order

1. **S-021 (Campsall, Box 47)** — best single shot at clearing V-6.5 from BLOCKED. 2026-07-24.
2. **S-009 (Edsel Ford Papers, Box 165)** — best single shot at clearing V-5.3 further than CONTESTED. 2026-07-24.
3. **S-018 (Logan Miller oral history, full transcript)** — not locatable online; needs archive access, possibly same 2026-07-24 trip.
4. **S-002/S-003/S-004/S-019 (headline-only press hits)** — full text pull via Chronicling America/newspapers.com, no archive visit needed, could happen before 2026-07-24.
5. **S-020 (HFHA/Wikipedia primary citation)** — identify or downgrade to CONTESTED-TAG only.
6. **S-025 (Bennett memoir)** — needs a library/archive.org loan, no archive visit needed.

## Maintenance

Every new sourcing-packet work-log entry, sweep finding, or web search result that names a source
gets a row here in the same commit — new ID, next sequential number. Don't let this drift out of
sync with the packets; if it does, the packets are the fallback source of truth, not this file.
