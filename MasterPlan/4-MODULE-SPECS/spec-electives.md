# Spec — Electives (E1–E8)

> Tier-3 differentiators. **Do NOT start any elective until Phases ①–⑥ of `6-MASTER-CHECKLIST.md` are
> essentially done** (post-core, or during job search to deepen a branch). Pick by role branch
> (`2-EXECUTION-PLAN.md` §4). Each is ≤1 week and follows the full format law. Build at
> `Addendum/Electives/weekE<n>-<slug>/`. These specs are lighter than modules 6–9 by design — expand
> the chosen one to full day-detail (via `5-AI-WORKFLOW.md` §2) only when you commit to it.

| # | Elective (folder) | Core days | Strongest for | Key connections |
|---|---|---|---|---|
| **E1** | RL & preference tuning (`weekE1-rl-dpo/`) | bandits (ε-greedy, UCB) → MDP/Bellman intuition → policy gradient from scratch on CartPole → PPO concept → DPO deep-dive extending weekP-6 | LLM eng, research-leaning | weekP-6 (DPO), weekU-5 (exploration), Week 9 (gradients) |
| **E2** | Diffusion & multimodal (`weekE2-diffusion-multimodal/`) | forward/reverse diffusion math on 2-D toy data → DDPM training loop → latent-diffusion concept → CLIP contrastive objective → one multimodal app | CV, GenAI product | weekG (CV), weekE-3 (contrastive/embeddings), Week 9 |
| **E3** | Speech & audio (`weekE3-speech-audio/`, 2–3 days) | audio as signals (spectrograms) → Whisper-class ASR as a component → TTS APIs → a voice-agent loop (ASR→weekN agent→TTS) | product/agents | weekN (agent loop), weekF (transformers under the hood) |
| **E4** | Graph ML (`weekE4-graph-ml/`) | graphs as data → message-passing intuition → GCN from scratch on a small graph → node classification | fraud/social/bio niches | weekU (bipartite user-item graph), weekD-4 (linear algebra) |
| **E5** | Edge & on-device (`weekE5-edge-ondevice/`, 2–3 days) | ONNX export → int8 quantized mobile inference → latency/size budgets on-device | mobile/embedded niches | weekP-5 (quantization), weekR-3 (profiling) |
| **E6** | AI governance depth (`weekE6-governance/`) | EU AI Act risk tiers & obligations → model cards → system cards → audit trails/lineage → the compliance-ready defense | regulated industries | weekB-5 (fairness seed), weekL-3 (lineage) |
| **E7** | Kaggle competition (`weekE7-kaggle/`) | one tabular competition end-to-end with weekA/weekB skills → leaderboard feedback loop → a medal as external validation | DS/MLE credibility | weekA (boosting), weekB (interpretability), Week 8 (workflow) |
| **E8** | Open-source contribution (`weekE8-oss/`) | read a real codebase (sklearn/HF) → find a good-first-issue or doc gap → 2–3 small merged PRs | all (strong hire signal) | weekJ (SE practices), teaches real-codebase reading no lesson can |

**Selection guidance:** most candidates do **zero to two** electives before their first offer. E8 (OSS)
and E7 (Kaggle) give the most external validation per hour and suit any branch; E1 suits the LLM branch;
E6 matters only if targeting finance/health/gov. Everything here is explicitly cuttable — the core is the
job-getter, electives are the tie-breakers.
