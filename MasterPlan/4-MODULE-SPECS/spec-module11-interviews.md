# Spec — Module 11: Interview Gauntlet (weeks X, Y, Z)

> Closes Gap 4: interview readiness is a separate skill from competence. Runs as a Track-C drip (X from
> M4, Y from M9, Z peaks M12), NOT a terminal block. Artifacts in `Career/` subfolders.
> Prompts for every drill are in `5-AI-WORKFLOW.md` §6.

## Week X — DSA drip (30 min/day, M4→M12) → `Career/dsa/`

**The set:** 75 curated problems (the "Blind 75"-class list — enumerate the actual 75 in
`Career/dsa/PLAN.md` when starting). Python-first (the program's Python is strong; algorithmic reps are
zero). Order by pattern, not difficulty-shuffle.

**Pattern schedule (one pattern per ~1.5 weeks, ~10 weeks total):**
1. Arrays & hashing · 2. Two pointers · 3. Sliding window · 4. Stack · 5. Binary search ·
6. Linked list · 7. Trees (BFS/DFS) · 8. Heaps / top-k · 9. Graphs (traversal, union-find) ·
10. Dynamic programming (1-D only — depth beyond this is low-ROI for ML roles).

**Method per problem:** 25 min attempt cold → if stuck, read approach not code, re-attempt → log in
`Career/dsa/log.md` (problem, pattern, solved-cold?/hint/failed, the one insight) → any miss becomes an
SRS card (the pattern, not the problem). Re-attempt logged misses after 1 week.

**Goals:** medium in ≤25 min consistently by M11 · explain time/space aloud while coding · handle the
edge-case follow-up. **Not the goal:** hard-DP speed, contest tricks.

**Mistakes:** memorizing solutions (learn the pattern trigger — "seeing "k-th/top" → heap") · silent
coding (interviewers score narration) · skipping edge cases (the actual differentiator at the ML bar).

## Week Y — ML breadth + system design (M9→M12) → `Career/system-design/`

### Y.1 Breadth drill (10 min/day, from M9)
Rapid-fire 5 questions/day across classical ML, DL, transformers/LLMs, evals/MLOps, stats/experiments —
calibrated to this repo (everything in it is fair game). Answer aloud in ≤3 sentences; grade 0–2; 0s/1s
become SRS cards. The Addendum question banks + this repo ARE the content; the drill adds pressure and
recall-without-notes. Prompt: `5-AI-WORKFLOW.md` §6.

### Y.2 ML system design (1/week from M10, → `Career/system-design/`)
The 2026 core round — "evaluation methodology is the new system design". Ten canonical prompts, one
per week, EACH practiced against the 2026 rubric (eval methodology 30% · data/features 20% · modeling
15% · serving cost+latency 20% · monitoring/guardrails 15%):

1. Recommendation system (weekU IS your answer — start here) · 2. Search ranking · 3. Fraud/anomaly
detection (weekC-7 hook) · 4. News/social feed ranking · 5. Autocomplete/typeahead · 6. Ads CTR
prediction · 7. RAG assistant (Flagship 1 IS your answer) · 8. Content moderation · 9. Demand/energy
forecasting (weekH hook) · 10. Recommendation cold-start / two-sided marketplace.

**Method:** 45-min timed, structured template (requirements & scale → data & features → offline eval →
model → serving/cost/latency → monitoring/guardrails → iterate). Write each as a 1-page note in
`Career/system-design/`. Two of the ten (recsys, RAG) you've actually BUILT — lead interviews with those.

**The insight to internalize:** the model-defense ritual you've done every week IS 70% of system design.
This module adds the whiteboard format, the scale/cost dimension, and thinking aloud under interruption.

## Week Z — Mocks, story bank, negotiation (M11→M12) → `Career/`

### Z.1 Behavioral story bank (build M11, `Career/story-bank.md`)
Extract 10 STAR stories from the journey (prompt §6). The material is unusually strong: career-switcher
discipline, a 20-week self-built curriculum, honest negative results (Week 12's baseline-beat-the-CNN),
shipped+deployed flagships, self-directed debugging (chaos days). Each story: 90-sec + 30-sec versions +
which question families it answers (failure / conflict / ambiguity / learning / impact / leadership).
Flag weak stories needing real reinforcement before interviews.

### Z.2 Mock loops (from M11, ≥4 total before applying)
- AI mocks weekly (system design §6 prompt; behavioral; coding-with-narration) — cheap, unlimited reps.
- ≥2 human mocks (community from weekW, or paid platform) — the irreplaceable part: real interruption,
  real silence, real follow-up pressure. Record, review, log the 2 worst moments + fixes.

### Z.3 Negotiation & logistics (M12, brief)
- Comp research for the target role/level/geo (the 2026 bands are in `7-APPENDIX-GAP-ANALYSIS.md`
  Part B as a starting reference — verify live at application time, they move).
- Basic negotiation posture: never the first number, competing offers create leverage, total-comp not
  base. One page in `Career/`, then stop over-preparing this and start applying.

## Definition of done (M12)
- [ ] 75 DSA problems done; mediums ≤25 min; log complete
- [ ] 10 system-design notes written; recsys + RAG lead-ready
- [ ] Breadth drill: consistent 2s across all 5 domains
- [ ] 10-story bank, road-tested in ≥4 mocks (≥2 human)
- [ ] Comp/negotiation one-pager · applications submitted
