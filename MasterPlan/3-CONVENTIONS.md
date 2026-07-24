# 📐 3 — Conventions: the format law (exhaustive)

> Every file generated for this program — by any model, any session — MUST match these templates exactly.
> They are extracted from the repo's existing best files (weekF lessons, module-2 README, qb-week10).
> When in doubt, open those originals and imitate.

---

## §1 Naming & layout

```
Addendum/<module-number>-<ModuleName>/           e.g., 6-LLM_Engineering/
  README.md                                      ← module index (template §5)
  week<Letter>-<slug>/                           e.g., weekN-agents-tools/
    1.0.<topic-slug>.md                          ← theory/plan (template §2)
    1.1.<topic-slug>.py                          ← practice scaffold (template §3)
    2.0.<topic-slug>.md
    2.1.<topic-slug>.py
    …
    <last>.0.<capstone-slug>.md                  ← final day is ALWAYS mini-project/defense
```
- Slugs: lowercase, hyphen-separated, descriptive (`agent-loop-react`, not `day3`).
- Day numbering restarts at 1 each week. Final day of every week = mini-project + defense.
- Defense artifacts: `week<Letter>_defense.md` (or `_writeup.md` / `_retrospective.md`) inside the week folder.

## §2 Lesson `.md` anatomy (all 8 parts, this order, nothing else)

```markdown
# Week <Letter> — Day <N>: <Title, plain words, no jargon-first>
> Pairs with `<N>.1.<slug>.py` · <one-line orientation note — why this day matters / pace advice>

## 📚 Topics
<2–4 lines of prose naming every concept covered, in teaching order. No bullets.>

## 🎯 Learning Goals
<3–6 numbered goals. Each MEASURABLE: "compute X by hand", "derive Y", "explain why Z (mechanism, not
slogan)", "match library output". NEVER "understand" / "learn about" / "be familiar with".>

## 🛠️ Build in the paired .py
<3–5 numbered, concrete exercises. Each produces something checkable: a number, a plot, a table, a
match-vs-library assertion. At least one exercise verifies from-scratch == library where applicable.>

## ⚠️ Common Mistakes
<2–4 mistakes, terse, separated by " · ". Real traps, not platitudes.>

## 🔗 Connects To
<Named prior lessons with the specific concept: "Week D-4 (dot products)" — and forward refs where a
cliffhanger is being planted.>

## 📖 References — <1–3 items, minimal, primary sources preferred, inline on one line>
```

### Worked example (a NEW-module lesson, for calibration)

```markdown
# Week N — Day 2: Function Calling — the Raw Protocol
> Pairs with `2.1.function-calling-raw.py` · No frameworks today. You will hand-roll the loop every
> framework hides, so nothing an agent does is ever magic to you again.

## 📚 Topics
The tool-use message protocol: tool schemas sent with the request, the model's tool_call response,
executing the tool yourself, returning results, and the loop that repeats until a final answer. Token
cost of tool traffic. Why the model never "runs" anything — it only emits structured requests.

## 🎯 Learning Goals
1. Write out, from memory, the full message sequence of one tool-use turn (roles, content types) —
   then verify against a real API trace.
2. Explain mechanically why tool calling is just constrained text generation (schema → the model emits
   a parseable call), connecting to Day 1's structured outputs.
3. Hand-roll the complete loop: send tools → detect tool_call → execute → append result → repeat →
   detect final answer. No framework imports.
4. Measure token growth per loop turn on a 3-tool task; state where the context budget goes.

## 🛠️ Build in the paired .py
1. Define two tools as JSON schemas: `calculator(expression)` and `read_file(path)`; print the exact
   request payload before sending.
2. The raw loop (≤60 lines): run "What is 3× the number of lessons in weekF?" — requires BOTH tools.
   Log every message dict in order.
3. Failure injection: make `read_file` throw; return the error as the tool result; verify the model
   recovers or asks for help (document which).
4. Token ledger: tokens in/out per turn for exercise 2, as a small table.

## ⚠️ Common Mistakes
Treating tool_call output as text to regex (it's structured — parse it) · forgetting to append the tool
RESULT before the next model call (the loop silently degenerates) · letting the model loop forever
(always a max-turns guard) · schema descriptions written for humans, not for the model choosing tools.

## 🔗 Connects To
Day 1 (structured outputs — a tool call IS one) · Week F-6 (the API mechanics) · Day 3 (this loop +
reasoning = the ReAct agent) · Week O-6 (each loop turn becomes a traced span).

## 📖 References — your API provider's tool-use guide (read the raw HTTP examples, skip the SDK sugar)
```

## §3 Practice `.py` scaffold (generated with the lesson, filled by the learner)

```python
'''
Week <Letter> — Day <N>: <Title>
================================<match title length>

Practice placeholder — pairs with `<N>.0.<slug>.md` in this folder.

HOW TO USE (when you reach this lesson):
  1. Read the paired markdown FIRST (topics, learning goals, core mechanics).
  2. Work through the "Build in the paired .py" exercises below, in order.
  3. Keep this header docstring; append a short "what I learned / what surprised me"
     note at the bottom when done (the main repo's best habit).

EXERCISES (from the paired markdown):
  1. <exercise 1, copied verbatim (may wrap)>
  2. …

Status: NOT STARTED
'''

# =====================================================================
# Exercise 1
# =====================================================================
# TODO


if __name__ == "__main__":
    print("Lesson placeholder — see paired markdown: <N>.0.<slug>.md")
```

## §4 Defense / write-up template (final day of every week)

```markdown
# Week <Letter> Defense — <project name>
## 1. Problem & framing        ← what decision does this system inform; success metric + why
## 2. What I built             ← architecture in ≤10 lines + one diagram if it helps
## 3. Evidence                 ← baseline vs candidates table; the ONE headline number; holdout used once
## 4. Choices I'd defend       ← 3–5 choices, each: alternative considered → why rejected
## 5. Risks & failure modes    ← what breaks first; what I did NOT test
## 6. Costs                    ← compute/tokens/money/time actually spent
## 7. Next steps               ← concrete, ordered
## 8. Retrospective            ← what surprised me; what I'd do differently
```
Public-bar weeks (capstones, flagships) additionally satisfy `2-EXECUTION-PLAN.md` §5.

## §5 Module & week README templates

Module README (see `Addendum/2-ClassicalML_Completion/README.md` as the canonical example):
opening paragraph = which gap this module closes (link the appendix) · one table per week
(Day | Lesson | Output) · Status checkbox block · new-packages line.

Week-level status lives in the module README checkboxes; program-level status ONLY in
`6-MASTER-CHECKLIST.md`.

## §6 Question bank format (per week; see `Addendum/1-ConsolidationPack/questionbanks/qb-week10.md`)

`qb-week<X>.md`: header (covers + where answers go) · 🟢 Easy (10) · 🟡 Medium (10) · 🔴 Tricky (5) ·
🧪 Coding Challenges (5, implemented in `qb-week<X>_challenges.py`). Questions reference specific
lessons ("recall Week-10 Day-1"). Interview-tag: append `⏱️` to any question plausible in a screening
call. Challenges file: docstring spec per challenge + reference solution below a `# ── reference ──` rule.

## §7 SRS card format (Gap-19 mechanism)

`srs-week<X>.txt`, one card per line: `Q;A` — front = question only; back ≤2 sentences. Sources: every
Learning Goal (inverted into a question) + every Common Mistake ("What goes wrong if …?"). Import into
Anki (or the plain-text SM-2 scheduler built in Module 1's SRS task).

## §8 Quality gate — run before accepting ANY generated content

- [ ] All 8 lesson sections present, in order; goals measurable (grep for "understand" — must be absent)
- [ ] Every Build exercise checkable (number/plot/table/assertion) and ≥1 from-scratch-vs-library match
- [ ] Mechanics-first: no framework call before its mechanics day
- [ ] Connects-To names real, existing lessons (verify paths) — no invented references
- [ ] Final day is a defense; deliverable named; public bar included where required
- [ ] .py exercises verbatim-match the .md Build list; header docstring intact
- [ ] Nothing duplicates existing content (grep the topic across `docs/` + `Addendum/` first)
- [ ] Module README + checklist rows updated
