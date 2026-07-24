# 🤖 5 — AI Workflow: how any model extends this program

> Paste these into a session with any strong model (Sonnet, Opus, Fable, GPT, …). If the model has repo
> access (Claude Code / Cowork), it can read the specs directly; otherwise paste the CONTEXT block plus
> the relevant spec section. Every prompt assumes the model will obey `3-CONVENTIONS.md` and run its §8
> quality gate before returning.

---

## §1 The CONTEXT block (prepend when the model lacks repo access)

```text
CONTEXT — you are extending "aijourney_python", a self-study AI curriculum with a strict format law.
Governing plan: the MasterPlan/ folder is the single source of truth. Obey it over any other file.

FORMAT LAW (from MasterPlan/3-CONVENTIONS.md):
1. Every lesson is a PAIR: `N.0.<slug>.md` (theory/plan, written up-front) + `N.1.<slug>.py`
   (practice scaffold: header docstring + numbered TODO exercises copied verbatim from the md's Build list).
2. Every lesson .md has EXACTLY these sections, this order, nothing else:
   `# Week <X> — Day N: <Title>` · one-line pairing/orientation note ·
   `## 📚 Topics` (prose, 2–4 lines, no bullets) ·
   `## 🎯 Learning Goals` (3–6 numbered, MEASURABLE — "compute by hand", "derive", "explain why
      (mechanism)", "match library output"; the word "understand" is BANNED) ·
   `## 🛠️ Build in the paired .py` (3–5 numbered, each produces a number/plot/table/assertion; ≥1
      verifies from-scratch == library) ·
   `## ⚠️ Common Mistakes` (2–4, terse, " · "-separated, real traps) ·
   `## 🔗 Connects To` (names specific prior lessons, e.g. "Week D-4 (dot products)") ·
   `## 📖 References` (1–3, minimal, primary sources).
3. MECHANICS FIRST: from-scratch math (hand/NumPy) BEFORE any framework call; then match the library.
4. Every week's FINAL day is a mini-project + written defense (choices→evidence→risks→next steps).
5. Evaluation honesty: baselines first; holdout used once; negative results are valid.
6. Public by default: capstone/flagship weeks meet the "public bar" in MasterPlan/2-EXECUTION-PLAN.md §5.

LEARNER PROFILE: completed classical ML from scratch (logistic/linear regression, full CV discipline,
leakage-safe pipelines), PyTorch CNNs, and — by the time new modules run — transformers incl.
attention-by-hand, a tiny GPT, HF fine-tuning with LoRA, FastAPI+Docker+MLflow. Curious, wants
mechanism not recipes, studies solo with an AI tutor. Tone: direct, dry humor, no fluff. You write
lesson PLANS (the .md), not textbook chapters — the learner fills the .py while studying.

BEFORE RETURNING: run the quality gate (MasterPlan/3-CONVENTIONS.md §8). Grep your own output for
"understand"; fix every hit. Verify every "Connects To" reference names a real lesson.
```

## §2 Build a week (the workhorse prompt)

```text
{{CONTEXT block, unless you have repo access}}
TASK: Build Week {{X}} — {{title}} — into {{target folder from MasterPlan/1-PROGRAM-MAP.md §2}}.
SPEC: follow MasterPlan/4-MODULE-SPECS/{{spec file}}, the Week {{X}} section, day by day.
DELIVER, in order:
  1. Every `N.0.<slug>.md` in FULL (all 8 sections), one per day in the spec.
  2. Every `N.1.<slug>.py` as a scaffold (header docstring + the Build exercises copied in as
     numbered TODOs; `Status: NOT STARTED`).
  3. The week `README.md` (module-README template: gap-closed paragraph, Day|Lesson|Output table,
     status checkboxes, new-packages line).
Do NOT invent scope beyond the spec. Do NOT write solutions in the .py (they're for the learner).
Where the spec says "provide the task set / attack list / dataset in the lesson", actually enumerate it.
After building, output the §8 quality-gate checklist with each box ticked and a one-line justification.
```

Build order (respect dependencies, `1-PROGRAM-MAP.md` §3): E-revision → F-revision → N → O → P → Q → R
→ S → T → U. Modules 10–11 are process (use §5/§6 prompts, not §2).

## §3 Revise weeks E–F against completed Week 13

```text
{{CONTEXT}}
TASK: Weeks E–F were drafted before main-course Week 13 was finished. Here is the ACTUAL completed
Week 13 content: {{paste docs/curriculum/5-AppliedAI/13.week13.md}}.
Walk every lesson in weekE and weekF. For each, output a verdict:
  KEEP (pure gap) / TRIM (partial overlap — list which learning goals survive) / DROP (duplicate).
Then rewrite both week READMEs with the verdicts and updated day counts. Preserve the mechanics-first
law while trimming (a TRIM becomes a fast-review day, not a deletion of the hand-computation).
Output: one verdict table per week + the two rewritten READMEs. (Detail: MasterPlan/4-MODULE-SPECS/
spec-module4-5-revision.md R2.)
```

## §4 Generate question bank + SRS cards for a week

```text
{{CONTEXT}}
TASK: From the attached lesson mds of Week {{X}}, produce, in the exact formats of
MasterPlan/3-CONVENTIONS.md §6 and §7 (canonical example:
Addendum/1-ConsolidationPack/questionbanks/qb-week10.md):
  1. `qb-week{{X}}.md` — 🟢 Easy (10) · 🟡 Medium (10) · 🔴 Tricky (5) · 🧪 Coding Challenges (5).
     Each question references a specific lesson/day. Append `⏱️` to any question plausible in a
     screening call.
  2. `qb-week{{X}}_challenges.py` — 5 challenges: docstring spec each + reference solution below a
     `# ── reference ──` rule.
  3. `srs-week{{X}}.txt` — `Q;A` lines from every Learning Goal (inverted to a question) and every
     Common Mistake ("What breaks if …?"). Back ≤ 2 sentences.
```

## §5 Flagship review (act as a hostile staff engineer)

```text
{{CONTEXT}}
TASK: Review my Flagship {{1|2|3}} (spec: MasterPlan/2-EXECUTION-PLAN.md §5) at {{path/URL}}. Order:
  1. README-as-case-study: is problem → approach → eval number → cost → limits on the FIRST screen?
  2. Eval story: is the set versioned? one headline number? would a quality regression actually be caught?
  3. Honesty audit: flag EVERY claim not backed by an artifact in the repo.
  4. Production posture: what breaks first? logging, secrets, cost ledger, error handling?
  5. Interview surface: the 10 hardest questions an interviewer asks about THIS project, with the answers
     the repo currently supports — plus the 3 it CAN'T answer yet (my TODO list).
Be blunt. "Looks good" is a failed review. End with the single highest-ROI fix.
```

## §6 Interview drills

**System design mock (weekly, M10+):**
```text
Run a 45-min ML system design interview: "Design {{rotate: recommendations · search ranking · fraud ·
feed · autocomplete · ads CTR · RAG assistant · moderation · demand forecast · marketplace cold-start}}".
2026 rubric — eval methodology 30 · data/features 20 · modeling 15 · serving cost+latency 20 ·
monitoring/guardrails 15. Interrupt me with follow-ups; push on trade-offs I gloss. End: score per rubric
line + the 2 worst moments transcribed + model answers for them. (I've built recsys + RAG — hold me to a
higher bar on those.)
```

**Breadth drill (daily 10 min, M9+):**
```text
Fire 5 rapid ML questions across classical ML · DL · transformers/LLMs · evals/MLOps · stats/experiments,
calibrated to aijourney_python (all of it is fair game). I answer ≤3 sentences each. Grade each 0–2
(0 wrong / 1 incomplete / 2 hire-signal), correct me tersely, then emit any 0s/1s as SRS cards (§4 format).
```

**Behavioral story bank (once, M11):**
```text
Interview me to extract 10 STAR stories from my AI journey (career switcher; 20-week self-built
curriculum; honest negative results like Week-12's baseline-beat-the-CNN; deployed flagships; self-debugged
chaos days). Per story: 90-sec + 30-sec versions + which question families it answers (failure/conflict/
ambiguity/learning/impact/leadership). Flag weak stories needing real-world reinforcement before interviews.
```

## §7 Weekly review (Track-C ritual, same weekday, 30 min)

```text
Weekly review. Inputs: this repo's git log (last 7 days) + MasterPlan/2-EXECUTION-PLAN.md §3 (this month's
row) + MasterPlan/6-MASTER-CHECKLIST.md. Answer:
  1. What shipped vs the month's named outcome?
  2. What slipped — cut or carry? (apply the §3 cut-lines; don't move the deadline.)
  3. Track C intact? (SRS streak, DSA count this week, publishing on pace?)
  4. One thing to do differently next week.
Then update the checklist boxes. REFUSE to let me add scope without cutting equivalent scope.
```

## §8 Golden rules for AI sessions in this repo
- One week per build session; don't batch-generate modules (quality drops, cross-refs rot).
- Never write solutions into `N.1.py` — the learning is in the filling.
- Every generated week ends with the quality gate ticked, or it's not delivered.
- When a spec and a lesson disagree, the spec wins; when the spec and MasterPlan disagree, MasterPlan wins;
  flag the contradiction rather than silently choosing.
- Prefer small, seeded, cacheable datasets (Week-8 reproducibility discipline) unless the spec's public bar
  demands real/messy data (flagships).
