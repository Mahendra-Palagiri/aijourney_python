# Spec — Module 6: LLM Engineering (weeks N, O, P)

> Closes Gap 1 (see appendix): the #1 hiring signal of 2026 — agents, evals, guardrails, production RAG.
> Build at `Addendum/6-LLM_Engineering/`. Prereq: week F ✅. New packages: `pydantic`, an LLM SDK
> (Anthropic/OpenAI/local via `transformers` — exercises must work with any), `rank-bm25`, a vector DB
> client (e.g. `chromadb` or `qdrant-client`), `sentence-transformers`. Every lesson must be runnable
> with a LOCAL model fallback (small instruct model) so no exercise hard-depends on paid APIs.
> Module README opening: "You built the engine in week F. This module makes you the person who ships it."

---

## Week N — Agents & Tool Use (7 days) → `weekN-agents-tools/`

**Day 1 — Structured outputs: the foundation** (`1.0.structured-outputs.md`)
- Topics: why free text breaks systems; JSON mode & schema-constrained decoding (logit-masking intuition —
  the sampler can only pick tokens that keep the JSON valid); Pydantic as the contract; validate-retry loops.
- Goals: (1) explain constrained decoding mechanically, connecting to weekF-3's sampler where YOU chose the
  next token; (2) write a Pydantic schema and a validate→re-prompt loop; (3) measure parse-rate honestly.
- Build: extraction task (structured fields from 20 messy job postings) → naive prompt vs schema-constrained;
  parse rate over 50 runs each, as a table; a retry loop that reaches 100%; log retries needed.
- Mistakes: trusting one good run · schemas with vague field descriptions · unbounded retry loops.
- Connects: weekF-3 (sampling), weekF-6 (APIs), Day 2 (a tool call IS a structured output).

**Day 2 — Function calling: the raw protocol** (`2.0.function-calling-raw.md`)
- Full worked example in `3-CONVENTIONS.md` §2 — use it verbatim as this day's lesson.

**Day 3 — The agent loop (ReAct)** (`3.0.agent-loop-react.md`)
- Topics: reasoning+acting interleave; termination conditions; tool-failure handling; max-turn guards;
  reasoning traces as debugging gold.
- Goals: (1) extend Day-2's loop with a think→act→observe cycle; (2) enumerate the 4 ways the loop ends
  (answer, max turns, tool dead-end, user escalation) and implement all; (3) read a trace and locate the
  exact turn where a failure was decided.
- Build: agent over this repo with 3 tools — `grep_repo(pattern)`, `read_file(path)`, `run_python(code)`
  (sandboxed: subprocess + timeout) — run a fixed 20-task set (provide it in the lesson: "which week covers
  Cook's distance?", "how many lessons mention softmax?", "run weekD-4's exercise 2 and report the
  output"…); score success rate; full traces saved to `traces/`.
- Mistakes: no max-turns · swallowing tool errors instead of showing the model · prompt-tinkering per task
  instead of fixing the loop.
- Connects: Day 2 (loop), weekJ-1 (the sandbox needs tests), Week O-1 (this 20-task set becomes the eval seed).

**Day 4 — Memory & context budget** (`4.0.agent-memory-context.md`)
- Topics: context window as RAM; token budget arithmetic per turn; conversation summarization;
  scratchpad files vs stuffed context; what to forget.
- Goals: (1) compute the budget: model context − system − tools − history = remaining, per turn, on real
  traces; (2) implement rolling summarization (summarize turns >k old); (3) decide-and-defend what goes to
  external state vs context.
- Build: Day-3 agent survives a scripted 50-turn session without exceeding 50% of context; plot tokens/turn
  before vs after memory management; a `memory.md` scratchpad the agent reads/writes via tools.
- Mistakes: summarizing away the task constraints · unbounded scratchpads · measuring nothing.
- Connects: Day 3, weekP-6 (KV cache is the same budget at the serving layer).

**Day 5 — MCP: the standard way in** (`5.0.mcp-server-client.md`)
- Topics: Model Context Protocol — servers/clients, tools/resources/prompts; why a protocol beats N×M
  custom integrations; transport basics (stdio).
- Goals: (1) map Day-3's hand-rolled tools onto MCP concepts 1:1; (2) build a minimal MCP server exposing
  `search_repo` + `read_lesson`; (3) connect a standard client and run the Day-3 task set through it.
- Build: the server (~80 lines with the `mcp` package); side-by-side: hand-rolled vs MCP on 10 tasks
  (success, latency, lines-of-code table); write one paragraph: what the protocol bought and cost.
- Mistakes: exposing `run_python` over MCP without the sandbox · tool descriptions that made sense in
  code but not to a model choosing among 20 servers.
- Connects: Day 3 (same tools, standard plumbing), Flagship 1 (its tool layer becomes an MCP server).

**Day 6 — Multi-agent & the judgment day** (`6.0.multi-agent-judgment.md`)
- Topics: orchestrator/worker, reviewer/critic patterns; frameworks (LangGraph-class) AFTER hand-rolling;
  the do-you-even-need-an-agent decision tree; cost/reliability of agent sprawl.
- Goals: (1) hand-roll a 2-agent pattern (worker drafts, critic reviews against a rubric, worker revises);
  (2) rebuild the same in one framework and articulate what it abstracted; (3) produce the decision table:
  direct call vs single agent vs multi-agent on the SAME task — cost, latency, success, debuggability.
- Build: the worker-critic pair on a summarization-with-citations task; the framework port; the measured
  decision table (this table is an interview answer — keep it).
- Mistakes: multi-agent as a default (it's a last resort) · critic with no rubric (vibes reviewing vibes) ·
  benchmarking only success and ignoring cost columns.
- Connects: Day 3–5, Week O (the rubric is an eval), weekM (orchestration at the pipeline level).

**Day 7 — Mini-project + defense: "Repo Butler v0"** (`7.0.agents-miniproject.md`)
- Build: agent with ≥3 tools + Day-4 memory + structured JSON logging; frozen 30-task eval set with
  per-category success (lookup / multi-hop / execution tasks); cost ledger; failure taxonomy (≥4 named
  failure modes with trace excerpts).
- Deliverable: `weekN_defense.md` (template §4) + tag the eval set `weekN-eval-v1` (Week O reuses it).
- Public bar: repo public with traces + README; this is Flagship 1's skeleton.

---

## Week O — Evals, Guardrails & LLMOps (7 days) → `weekO-evals-guardrails/`

**Day 1 — The eval harness, from scratch** (`1.0.eval-harness.md`)
- Topics: golden sets; graders: exact-match / regex / rubric; eval-set versioning (the set is code);
  why "it feels better" is not evidence.
- Goals: (1) build a harness (~120 lines, zero frameworks): load tasks, run system, grade, report per-category
  scores + deltas vs last run; (2) version the set and the scores; (3) state the harness's own blind spots.
- Build: harness wrapped around weekN's Butler using `weekN-eval-v1`; baseline scores committed as
  `evals/results/<date>.json`; one deliberately-bad prompt change → show the delta catch it.
- Mistakes: eval set drifts silently (version it) · grading generation with exact-match only · testing on
  the tasks you tuned on (hold out a slice).
- Connects: weekN-7, Week 7 (this IS cross-validation discipline, new domain), Day 3 (CI).

**Day 2 — LLM-as-judge, validated before trusted** (`2.0.llm-judge-validation.md`)
- Topics: judge prompts & rubrics; judge biases (position, verbosity, self-preference); agreement metrics;
  pairwise vs absolute scoring; when humans stay in the loop.
- Goals: (1) write a rubric judge for answer-faithfulness; (2) hand-label 30 outputs FIRST, then measure
  judge-human agreement (report %, and where it disagrees); (3) demonstrate one bias experimentally
  (swap answer order → does the verdict flip?).
- Build: the judge + the 30-item labeled set + agreement table + the position-bias experiment; only then
  wire the judge into Day-1's harness for the fuzzy categories.
- Mistakes: judging with the same model that generated (self-preference) · rubric so vague the judge
  free-styles · skipping the human-agreement step (a judge you never validated is a random number).
- Connects: Day 1, weekB (this is interpretability ethics again — trust must be earned).

**Day 3 — Regression gates & eval-driven development** (`3.0.regression-gates-ci.md`)
- Topics: evals in CI; thresholds & flakiness (n runs, mean±sd — Week 7's variance thinking); the EDD loop:
  failing eval → change → green; treating prompts as code (review, diff, rollback).
- Goals: (1) wire the harness into CI (weekJ-5's GitHub Actions) so a PR that drops the score >2 points
  blocks; (2) handle nondeterminism: 3 runs, gate on mean; (3) find a real change that "reads better" but
  scores worse — document it (this anecdote is interview gold).
- Build: the CI job + a demonstration PR that gets blocked + the flakiness study (same commit, 5 runs,
  score distribution).
- Mistakes: gating on a single run · thresholds with no rationale · fixing the eval instead of the system.
- Connects: Day 1–2, weekJ-5 (CI), Week 7 (CV mean vs variance — literally the same statistics).

**Day 4 — Prompt injection & jailbreaks** (`4.0.prompt-injection-redteam.md`)
- Topics: attack taxonomy — direct injection, indirect (poisoned documents — the RAG case!), tool-mediated
  exfiltration; jailbreak families; why "please ignore previous instructions" still works too often.
- Goals: (1) attack YOUR weekN Butler with 10 attacks across the taxonomy (provide the attack list in the
  lesson: a poisoned lesson-file that instructs the agent to dump its system prompt; a task that tricks
  `run_python` into reading outside the repo; …); (2) document ≥3 that succeed, with traces; (3) explain
  WHY each worked (instruction/data confusion is the root).
- Build: `attacks/` folder with each attack + result + trace; a findings table (attack, vector, success,
  severity).
- Mistakes: assuming your own docs are trusted input (Flagship 1 reads markdown — markdown is an attack
  surface) · testing only direct injection · treating a failed attack as proof of safety.
- Connects: weekN-3 (the tools are the blast radius), Day 5 (defenses), weekB-5 (responsible-AI thread).

**Day 5 — Guardrails & safety rails** (`5.0.guardrails-defenses.md`)
- Topics: defense in depth — privilege separation (least-privilege tools), input marking (data vs
  instructions), output filtering, PII detection/redaction, human-in-the-loop for consequential actions;
  refusal UX; the red-team checklist as a standing ritual.
- Goals: (1) implement ≥3 defenses against Day-4's successful attacks; (2) re-run ALL 10 attacks, report
  the before/after table; (3) add a PII redaction pass and measure its false positives too; (4) write the
  reusable red-team checklist for every future LLM feature.
- Build: defended Butler + before/after attack table + `redteam-checklist.md` (goes in `Career/` too).
- Mistakes: one big "safety prompt" as the only defense · filters that block the happy path (measure both
  directions) · declaring victory after defending only known attacks.
- Connects: Day 4, weekK-2 (API input validation — same instinct, new layer).

**Day 6 — Observability, cost & LLMOps** (`6.0.tracing-cost-llmops.md`)
- Topics: structured tracing (span per retrieve/generate/tool-call: latency, tokens, cost); dashboards
  from JSON logs (no vendor needed — logs + a notebook); prompt versioning & staged rollout; semantic
  caching; retries/fallbacks/streaming as reliability primitives.
- Goals: (1) instrument the Butler end-to-end (every span: name, duration, tokens, cost, parent); (2) build
  the cost/latency dashboard from logs; (3) find the slowest span and cut it ≥30% (caching or model choice);
  (4) implement model-fallback (primary fails → cheaper local model) and show it firing.
- Build: tracing decorator (~40 lines) + dashboard notebook + the optimization with before/after numbers +
  the fallback demo.
- Mistakes: logging text but not structure · optimizing cost with no quality re-check (re-run the evals!) ·
  cache keyed on exact strings when semantically-equal queries miss.
- Connects: weekK-5 (drift monitoring sibling), weekL-1 (MLflow = same instinct for training), Day 1 (evals
  re-run after every optimization).

**Day 7 — Mini-project + defense: the Ship Gate** (`7.0.ship-gate-miniproject.md`)
- Build: the complete gate around the Butler — versioned eval set (grown to 50 tasks incl. Day-2 judge
  categories + Day-4 security tests) · headline score · CI regression gate · tracing + cost dashboard ·
  guardrails with attack results.
- Deliverable: `weekO_defense.md` written for a skeptical staff engineer: "here is the evidence this system
  can ship, and here is exactly what would page us."
- Public bar: everything public; this defense becomes blog post 3 (eval-harness write-up, M7).

---

## Week P — Advanced RAG & Inference (7 days) → `weekP-rag-inference/`

**Day 1 — Retrieval eval first** (`1.0.retrieval-eval-chunking.md`)
- Topics: hit-rate@k, MRR; building the retrieval golden set; chunking as a measured decision (size ×
  overlap × structure-aware splitting), not folklore.
- Goals: (1) build a 50-query retrieval golden set over this repo (query → the lesson file(s) that answer
  it); (2) implement hit-rate@k and MRR from scratch; (3) run the chunking ablation grid and pick a winner
  WITH numbers.
- Build: golden set (versioned) + metrics (~40 lines) + ablation table (3 sizes × 2 overlaps ×
  {naive, heading-aware}) + one paragraph: which won and a mechanism-level guess why.
- Mistakes: evaluating retrieval by reading answers (measure retrieval alone first) · golden queries that
  all look alike (mix lookup/multi-hop/paraphrase) · chunking by token count through table/code blocks.
- Connects: weekF-6 (the from-scratch index), Week 7 (ablation = fair comparison discipline).

**Day 2 — BM25 by hand + hybrid fusion** (`2.0.bm25-hybrid-fusion.md`)
- Topics: term frequency, IDF, the BM25 formula (compute one score fully by hand — this is the
  mechanics-first day); why lexical catches what dense misses (rare tokens, exact names) and vice versa;
  reciprocal-rank fusion.
- Goals: (1) hand-compute BM25 for one query over 3 tiny docs, every term; (2) implement BM25 (~60 lines),
  verify vs `rank-bm25`; (3) implement RRF; (4) measure sparse vs dense vs hybrid on Day-1's golden set.
- Build: the hand calculation (in comments) + implementation + verification + the 3-way results table.
- Mistakes: skipping the hand computation · fusing raw scores instead of ranks (scales differ — that's
  why RRF exists) · concluding hybrid always wins (report where dense alone was better).
- Connects: Day 1, weekE-2 (TF-IDF — BM25 is its battle-hardened cousin), weekD-4 (cosine similarity).

**Day 3 — Reranking & a real vector DB** (`3.0.reranking-vectordb.md`)
- Topics: bi-encoder vs cross-encoder mechanics (why cross-attention over the PAIR wins accuracy and costs
  latency — connect to weekF-1); two-stage retrieve→rerank; graduating from the from-scratch index to a
  vector DB (persistence, metadata filtering, ANN concept).
- Goals: (1) explain bi vs cross encoder with the attention diagram; (2) add a cross-encoder reranker and
  measure the gain + the latency price; (3) migrate to a vector DB with metadata (module, week, day) and
  demonstrate filtered retrieval ("only search weekD").
- Build: rerank stage + before/after table (hit-rate@k AND p50 latency) + the migration + 3 filtered queries.
- Mistakes: reranking 100 candidates when 20 suffice · benchmarking accuracy without latency columns ·
  treating ANN recall as exact (it's approximate — know the knob).
- Connects: weekF-1 (cross-attention), Day 2 (candidates from hybrid), weekU-4 (same cascade in recsys).

**Day 4 — RAG failure modes & agentic RAG** (`4.0.rag-failures-agentic.md`)
- Topics: the failure taxonomy — retrieval miss / context dilution / faithfulness failure (right context,
  wrong answer) / multi-hop gaps; query rewriting; iterative (agentic) retrieval; when RAG is the wrong
  tool entirely.
- Goals: (1) separate faithfulness from relevance in the eval (two scores per answer, weekO-2's judge);
  (2) build a failure gallery: ≥6 real failures, classified, each with mechanism diagnosis; (3) implement
  query rewriting + agentic multi-hop retrieval and show which failure classes each fixes (and doesn't).
- Build: the two-score eval + failure gallery + rewriting/multi-hop implementations + per-class fix table.
- Mistakes: blaming the LLM when retrieval missed (your separated metrics exist for this) · adding agentic
  loops before measuring simple RAG · fixing failures one anecdote at a time instead of by class.
- Connects: weekO-1/2 (harness+judge), weekN-3 (the loop), Flagship 1 (this IS its diagnosis toolkit).

**Day 5 — Quantization & local inference** (`5.0.quantization-local-models.md`)
- Topics: what int8/int4 actually round (weights, activations, KV); quality-vs-memory arithmetic
  (7B × 2 bytes fp16 = 14 GB → int4 ≈ 3.5 GB); GGUF-class formats; running a 7B-class instruct model
  locally; when local beats API (privacy, cost, latency floor).
- Goals: (1) do the memory arithmetic for 3 model sizes × 3 precisions, as a table, BEFORE downloading
  anything; (2) run a local model and wire it as the Butler's fallback; (3) measure the quality delta
  across quantization levels on YOUR eval set (not just perplexity).
- Build: the arithmetic table + local serving + eval-score-vs-precision table + tokens/sec measurements.
- Mistakes: trusting perplexity alone (task evals or it didn't happen) · comparing quantized-local vs
  API on different prompts · ignoring first-token vs throughput latency (different UX budgets).
- Connects: weekF-4 (HF loading), weekO-6 (fallback slot ready), weekD-1 (what rounding does to a
  distribution).

**Day 6 — Serving economics: KV cache, batching, DPO taste** (`6.0.serving-economics-dpo.md`)
- Topics: KV cache BY HAND (per-token per-layer memory formula — derive why long contexts eat GPUs);
  continuous batching intuition (why naive batching wastes the GPU between sequences); vLLM-class server
  benchmarking; DPO at concept+small scale (preference pairs → the DPO loss → one training run; the
  practical successor to RLHF for mortals — extends weekF-5's LoRA).
- Goals: (1) derive the KV-cache formula and compute it for the Day-5 model at 4k/32k context; (2) benchmark
  a vLLM-class server: throughput-vs-latency curve at 1/4/16 concurrent requests; (3) explain DPO's loss in
  one paragraph (reference model, why no reward model) and run one tiny DPO fine-tune on ~200 preference
  pairs; eval before/after.
- Build: the derivation + the benchmark curves + the DPO run with eval deltas.
- Mistakes: benchmarking at concurrency 1 and extrapolating · DPO on pairs the model already agrees with
  (no gradient) · skipping the before/after eval (weekO habit by now).
- Connects: weekN-4 (context budget, serving side), weekF-5 (LoRA — DPO rides the same adapters),
  weekR-3 (profiling mindset).

**Day 7 — Mini-project + defense: Flagship 1 upgrade** (`7.0.rag-inference-miniproject.md`)
- Build: Butler upgraded — hybrid+rerank retrieval · two-score RAG eval · quantized local fallback ·
  cost-per-query ledger · the full before/after table vs weekN-7 baseline.
- Deliverable: `weekP_defense.md` + a 1-page decision memo: **"fine-tune vs prompt vs RAG"** — the decision
  framework with THIS system's numbers as evidence (a standing interview question, answered with receipts).
- Public bar: Flagship 1 deployed (M6 outcome) — weekQ moves it to a real cloud URL.
