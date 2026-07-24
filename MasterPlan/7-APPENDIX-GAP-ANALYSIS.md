# 📎 7 — Appendix: Gap Analysis (the evidence behind the plan)

> Why every module in this plan exists. Read when you doubt a choice. First review pass:
> `Addendum/aijourney_project_analysis.html` (Opus, June 2026) — it created the Addendum. This second
> pass (July 2026) asks: after the Addendum is done, what STILL blocks "top candidate on the 2026–27
> market"? Every gap below was verified against the repo (grep + file review), not assumed.

---

## Part A — What the program already covers (and covers well)

| Layer | Coverage | Where |
|---|---|---|
| Python + NumPy/Pandas/viz | ✅ solid, question banks w/ "mine vs reference" | Wk 1–2 |
| ML workflow, preprocessing | ✅ | Wk 3–4 |
| Classical ML from scratch | ✅ unusually deep — logistic/linear regression by hand, regularization, VIF, Cook's distance, nested & time-series CV | Wk 5–7 |
| Rigor rituals | ✅ **the program's superpower** — pipelines-in-CV, leakage proofs, single-use holdout, written model defenses | Wk 8 |
| Deep learning | ✅ NN math, PyTorch, CNNs, honest "baseline beat the CNN" capstone | Wk 9–12 |
| Classical ML completion | ✅ tree/boosting mechanics, XGBoost, SHAP/LIME/PDP/calibration/fairness | Addendum Module 2 |
| Unsupervised + math spine | ✅ clustering/PCA/t-SNE/anomaly + probability/CLT/Bayes/linalg/SVD/calculus | Addendum Module 3 |
| Transformer/LLM foundations | ✅ attention by hand → tiny GPT → HF → LoRA → 1 RAG day | Addendum Module 4 (E–F) |
| CV / time series | ✅ transfer learning + DL toolkit; ARIMA→ML→LSTM | Addendum Module 4 (G–H) |
| Local MLOps | ✅ pytest, SQL, FastAPI, Docker, MLflow, drift, orchestration | Addendum Module 5 |

**Pedagogical strengths to PRESERVE (Laws 1–5 in the MasterPlan README):** mechanics-first · paired
files · the model-defense ritual (this is literally what ML interviews test) · evaluation honesty ·
connection threading. Do not "modernize" these away.

## Part B — What the 2026–27 market demands (research, July 2026)

1. **AI Engineer = #1 fastest-growing US title** (+143% YoY postings). Role split into ~6 tracks; each
   wants a different resume signal → hence the role-agnostic core + M11 branch.
2. **Eval literacy is the single biggest "actually built with LLMs" signal.** 2026 ship-gate = versioned
   eval set + numeric score + regression alarm → Module 6 Week O.
3. Stack shifted "LangChain+Pinecone" → **agent orchestration, MCP, eval design, RAG/vector DBs, cost
   optimization, guardrails, observability, frontier-model fluency** → Module 6 (N/O/P).
4. **Comp deltas:** RAG +10–15% · LoRA/QLoRA/RLHF +10–15% · deployment/MLOps +$15–30K over notebook-only
   candidates. (Agentic AI Engineer bands cited $185–320K base at growth-stage; verify live before
   negotiating — bands move.)
5. **Interviews:** "evaluation methodology is the new system design" — cost/latency/guardrails/monitoring
   weighted over architecture diagrams (→ Module 11 Y rubric); big-tech coding bar ≈ pure-SWE loop
   (→ Module 11 X); "production ML is 80% data engineering" probed directly (→ Module 8 S).
6. **Portfolio:** deployed, observable systems with honest eval write-ups beat certificate lists; hiring
   managers open GitHub before the resume (→ Law 6 + Module 10).

Sources listed at the bottom.

## Part C — The gaps (severity-tiered, each mapped to a module)

🔴 Tier 1 — blocks employability · 🟠 Tier 2 — separates top-10% · 🟡 Tier 3 — differentiators · ⚙️ process

### 🔴 Gap 1 — LLM *engineering* is one day → **Module 6 (N/O/P)**
Repo evidence: the entire agentic/eval/guardrail surface = `weekF/6.0.llm-apis-prompting-rag.md`, one day.
Zero hits anywhere for agents, function/tool calling, MCP, guardrails, prompt injection, vector DB,
reranking, LangChain/LangGraph. Missing: agents & tool use, **evals as an engineering discipline (the #1
signal)**, safety/guardrails (a RAG app reading documents has an injection surface on day one — never
mentioned), production LLM systems (tracing, cost, caching, fallbacks), advanced RAG (hybrid, rerank,
faithfulness-vs-relevance). Worst coverage-to-demand ratio in the program.

### 🔴 Gap 2 — Zero cloud → **Module 7 (Q/R)**
Repo evidence: no AWS/GCP/Azure/k8s/cloud hits (only false positives). Module 5 is deliberately local-first
and stops there. "Deployed on my laptop" doesn't survive a hiring manager; every MLE ad lists a cloud.
Also folds in distributed training / GPU fluency (bridges weekG-5's single-GPU AMP work).

### 🔴 Gap 3 — No public artifact exists or is planned → **Module 10 + Law 6**
Repo evidence: everything is private markdown on toy datasets (Iris/MNIST-class, "prefer small/cacheable").
The only "portfolio" mention in ~190 Addendum files is one line calling a defense doc "the portfolio's
spine". The program's depth is invisible. Fix: 3 deployed flagships, 6 posts (repurposed defenses — the
Week-12 "baseline won" retro is already a great post), GitHub-as-artifact, resume/vocabulary translation.

### 🔴 Gap 4 — No interview prep of any kind → **Module 11 (X/Y/Z)**
Repo evidence: zero DSA/system-design/behavioral hits; question banks test retention, not performance.
Missing: DSA (~75 problems), ML system design (the 2026 core round — but the defense ritual is 70% of it
already), breadth-under-pressure drills, behavioral story bank (the journey is strong material), mock loops.

### 🔴 Gap 5 — The timeline → **the 3-track restructure (`2-EXECUTION-PLAN.md` §2–3)**
Repo evidence: 13 content-weeks took 12 calendar months (Jul 2025–Jun 2026). Remaining main-course +
Addendum + extensions at that pace + the Addendum's own serial start-gate = employable ~2028–29, in the
fastest-moving field there is. The gate maximizes depth-purity but delays the most marketable skills
(transformers/LLMs) ~a year and defers ALL public evidence to the very end. Fix: three parallel tracks,
time-boxed months, market-critical work pulled early, public artifacts from M1 → interview-ready ~July 2027
without sacrificing mechanics-first.

### 🟠 Gap 6 — Experimentation & causal inference → **Module 8 Week T**
weekD-2 has hypothesis-testing mechanics; nothing on A/B *design* (power/MDE, peeking, CUPED) or causal
inference (confounding, DAGs, diff-in-diff, propensity, uplift). All "A/B"/"causal" greps were false
positives (e.g. "causal mask"). #1 DS interview domain; also how AI features are validated in industry.

### 🟠 Gap 7 — Data engineering beyond read_csv → **Module 8 Week S**
weekJ-3/4 has SQL + window functions (good). Missing: columnar/Parquet, DuckDB at volume, Polars/larger-
than-memory, dbt-style transforms, data-quality gates, feature stores. "Production ML is 80% data
engineering" is now an explicit probe.

### 🟠 Gap 8 — Recommenders absent → **Module 9 Week U**
Zero coverage; top-3 system-design prompt and a whole industry. Reuses weekD-5 SVD + Week-6 SGD + weekC
t-SNE + weekP ANN beautifully — high-leverage, well-connected addition.

### 🟠 Gap 9 — Fine-tuning stops at LoRA; no preference tuning / quantized inference → **folded into Module 6 Week P**
weekF-5 covers LoRA; missing QLoRA/quantization for inference, DPO (2026-practical preference tuning),
fine-tune-vs-prompt-vs-RAG decision framework, serving optimizations (KV cache, continuous batching,
vLLM). Extends an existing lesson rather than filling a void → 🟠 not 🔴.

### 🟠 Gap 10 — Streaming/production debugging reps → **folded into Module 7 Week R (chaos day)**
weekK-5 monitors batch drift; missing live-service debugging + incident postmortems (a postmortem is a
model defense for failures). Cheap, high-signal: break the deployment 5 ways, diagnose from logs.

### 🟡 Tier 3 electives (E1–E8, `spec-electives.md`)
RL/DPO · diffusion/multimodal · speech · graph ML · edge/on-device · governance depth · Kaggle · OSS.
Most candidates do 0–2 before an offer; E7/E8 give the most external validation per hour.

### ⚙️ Process gaps (baked into the plan, not a module)
- **19 — retention has artifacts but no schedule** → SRS system (R1 + Law: "no Done without cards").
- **20 — no external validation** → cloud cert, Kaggle, human mocks, publishing (readers = validation).
- **21 — learning alone** → one community, one talk, one accountability partner (Module 10 W.2).
- **22 — AI-assisted dev not practiced deliberately** → every flagship logs where AI helped/failed/was
  verified (Law 6 companion); interviewers ask this directly.
- **23 — no timeboxing** → named monthly outcomes + cut-lines + weekly review (§7 ritual).

## Part D — Coverage scorecard (after main course + Addendum, BEFORE this plan)

| Market cluster | Coverage | Gap → module |
|---|---|---|
| Python + classical ML rigor | ████████░░ 85% | — |
| Math foundations | ████████░░ 80% | — |
| Deep learning foundations | ████████░░ 80% | — |
| Transformer/LLM foundations | ███████░░░ 70% | — |
| **LLM engineering (agents/evals/RAG/guardrails)** | ██░░░░░░░░ 15% | 1,9 → M6 |
| MLOps (local) | ███████░░░ 70% | 10 → M7 |
| **Cloud & scale** | ░░░░░░░░░░ 0% | 2 → M7 |
| Data engineering | ███░░░░░░░ 25% | 7 → M8 |
| Experimentation/causal | ██░░░░░░░░ 20% | 6 → M8 |
| Recommenders | ░░░░░░░░░░ 0% | 8 → M9 |
| **Public portfolio** | █░░░░░░░░░ 5% | 3 → M10 |
| **Interview readiness** | █░░░░░░░░░ 10% | 4 → M11 |
| Time-to-market | ██░░░░░░░░ (2028 at current pace) | 5 → restructure |

## Sources (market research, July 2026)
- [AI Developer Hiring 2026: Skills That Actually Matter](https://www.digitalapplied.com/blog/ai-developer-hiring-skills-that-matter-2026)
- [15 AI Engineer Skills Every Hire Should Have in 2026](https://www.ayautomate.com/blog/ai-engineer-skills-2026)
- [AI Engineering Jobs 2026: Roles, Skills & Salaries](https://nexusitgroup.com/ai-engineering-jobs/)
- [The Agentic AI Engineer Roadmap for 2026](https://medium.com/data-science-collective/the-agentic-ai-engineer-roadmap-for-2026-skills-stack-and-order-fc1dfa17948d)
- [Machine Learning System Design Interview (2026 Guide) — Exponent](https://www.tryexponent.com/blog/machine-learning-system-design-interview-guide)
- [ML System Design Interview — IGotAnOffer](https://igotanoffer.com/en/advice/machine-learning-system-design-interview)
- [AI Engineer Resume Guide 2026 — MirrorCV](https://mirrorcv.com/resume-guide/ai-ml-engineer)
- [Meta MLE Interview Guide 2026 — DataInterview](https://www.datainterview.com/blog/meta-machine-learning-engineer-interview)
