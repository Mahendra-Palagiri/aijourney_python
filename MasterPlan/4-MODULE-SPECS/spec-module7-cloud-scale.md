# Spec — Module 7: Cloud & Scale (weeks Q, R)

> Closes Gap 2: zero cloud coverage anywhere in the program. Build at `Addendum/7-Cloud_Scale/`.
> Prereq: week K ✅ (Docker image exists). Provider: **AWS** by default (largest job-ad footprint;
> concepts transfer) — if the learner prefers GCP, every lesson names the equivalent service in a
> one-line "GCP: …" note. Budget guard: the entire module must be executable for **< $30** (free tier +
> spot + immediate teardown); every lesson ends with a "destroy what you made" step.
> New packages/tools: AWS CLI, `boto3`, `terraform`, `kubectl` (weekR).

---

## Week Q — One Cloud, For Real (6 days) → `weekQ-cloud/`

**Day 1 — Mental model, IAM, and the billing alarm** (`1.0.cloud-mental-model-iam.md`)
- Topics: regions/AZs; the shared-responsibility line; accounts vs users vs roles vs policies
  (least-privilege from minute one); access keys hygiene; billing alerts BEFORE any resource exists.
- Goals: (1) draw the region→AZ→VPC→service mental map from memory; (2) create an admin-locked root +
  a least-privilege IAM user/role for daily work; (3) set a $10 billing alarm and TEST it fires;
  (4) explain why long-lived access keys in code are how horror stories start (and what to do instead).
- Build: account setup checklist executed; `aws sts get-caller-identity` from the CLI with the restricted
  role; the billing alarm; a `cloud/JOURNAL.md` started — every resource ever created gets a line
  (name, why, cost, destroyed-when). This journal is the week's spine.
- Mistakes: working as root · one god-policy user ("it's just me") · skipping the alarm because "I'll
  be careful".
- Connects: weekJ-2 (config/secrets discipline), weekK-3 (the image that's about to ship).

**Day 2 — Storage & data on object stores** (`2.0.object-storage-data.md`)
- Topics: S3 mechanics — buckets/keys/prefixes (it's not a filesystem); storage classes & lifecycle;
  presigned URLs; versioning; DuckDB querying Parquet directly from S3 (bridge to weekS).
- Goals: (1) explain why S3 lists are prefix scans, not directory walks (and what that does to layout
  design); (2) move the program's datasets to a bucket with a sane prefix scheme; (3) generate a presigned
  URL and explain its exact security semantics; (4) query a Parquet file in S3 from local DuckDB without
  downloading it.
- Build: the bucket + layout doc + presigned-URL demo + the remote DuckDB query with timing vs local.
- Mistakes: public buckets (the classic) · millions of tiny objects (batch them) · treating S3 as
  low-latency storage.
- Connects: weekS-1 (Parquet), weekL-3 (data versioning gets a real backend).

**Day 3 — Compute mapped, and the first real deploy** (`3.0.compute-deploy-containers.md`)
- Topics: the compute menu — EC2 (VMs) vs Lambda (functions) vs managed containers (ECS/Fargate;
  GCP: Cloud Run) — cost/cold-start/ops-burden trade-offs; pushing the weekK Docker image to a registry;
  HTTPS endpoint with logs.
- Goals: (1) fill the compute decision table (workload → right choice → why) for 5 scenarios incl. "bursty
  inference API" and "nightly batch scoring" (weekK-4's distinction, now with real services); (2) push the
  weekK image to ECR and deploy on Fargate; (3) read your service's logs in CloudWatch and find one request
  end-to-end.
- Build: the live HTTPS endpoint of the Week-12 model API + `curl` demo + logs screenshot-equivalent +
  cost/day estimate written BEFORE checking billing, then verified.
- Mistakes: EC2-by-default (undifferentiated ops burden) · no log retention thought · leaving it running
  (journal + teardown!).
- Connects: weekK-2/3 (the API+image), weekO-6 (tracing meets cloud logs).

**Day 4 — Managed ML & rented GPUs** (`4.0.managed-ml-gpu-rental.md`)
- Topics: the managed-ML menu (SageMaker-class endpoints, batch transform; GCP: Vertex) and when managed
  beats DIY; GPU rental workflow for training — instance choice, spot pricing mechanics, the
  checkpoint-resume discipline (weekG-5) as spot-interruption insurance.
- Goals: (1) deploy one model to a managed endpoint and compare vs Day-3's DIY on cost/control/effort
  (table); (2) rent a spot GPU, rerun weekG-3's transfer-learning fine-tune ON IT, survive a simulated
  interruption via checkpoint-resume; (3) compute the actual training cost and compare to a month of
  Colab-class subscription.
- Build: managed-endpoint deploy + the DIY-vs-managed table + the spot training run (with `nvidia-smi`
  proof and the resume test) + the cost table.
- Mistakes: managed endpoints for hobby-scale traffic (cost floor) · spot without checkpoints ·
  forgetting the GPU exists overnight (alarm + journal).
- Connects: weekG-5 (checkpointing pays off), weekR-2 (multi-GPU next), weekP-5 (GPU memory arithmetic).

**Day 5 — IaC taste: Terraform once** (`5.0.terraform-iac.md`)
- Topics: declarative infra — state, plan/apply/destroy; why click-ops doesn't scale or survive audits;
  reading HCL; drift.
- Goals: (1) recreate Day-3's whole deployment from one `main.tf` (registry, service, role);
  (2) `terraform destroy` and re-`apply`, proving reproducibility; (3) explain state files and why they're
  sensitive; (4) diff-read a plan and reject a bad one.
- Build: `cloud/terraform/main.tf` + the destroy/recreate cycle logged in the journal + one deliberate
  manual change detected as drift.
- Mistakes: state file in git unencrypted · terraform for one-off experiments (know when console is fine) ·
  apply without reading the plan.
- Connects: Day 3 (same infra, now as code), weekJ-5 (CI can now deploy).

**Day 6 — Capstone: everything live + defense** (`6.0.cloud-capstone-defense.md`)
- Build: three things on real URLs — Week-12 model API (Day 3), **Flagship 1** (weekP's Butler, with its
  tracing), and the MLflow tracking server (weekL) — plus: architecture diagram, per-service monthly cost
  table (projected vs billed), teardown/rebuild runbook (Terraform).
- Deliverable: `weekQ_defense.md` — every placement justified by cost/latency/ops-burden; the "what would
  I change at 100× traffic" section; journal reconciled against the actual bill.
- Public bar: URLs in Flagship READMEs; the cost table published (post-4 material).

---

## Week R — Scale & Reliability (5 days) → `weekR-scale-reliability/`

**Day 1 — Kubernetes reading fluency** (`1.0.kubernetes-fluency.md`)
- Topics: pods/deployments/services/ingress as concepts; the reconciliation loop (desired vs actual state —
  k8s's one big idea); reading manifests line by line; when k8s is overkill (usually, at this scale).
- Goals: (1) explain the reconciliation loop and why it makes self-healing "free"; (2) deploy the weekK
  image to a managed k8s (EKS-class or local kind/minikube to keep cost zero) and explain EVERY line of the
  manifest; (3) kill the pod, watch it resurrect, narrate why; (4) write the honest paragraph: what k8s
  buys, what it costs, when Fargate was the right call anyway.
- Build: the manifest (fully commented) + the deploy + the kill/resurrect demo + scale to 3 replicas and
  back.
- Mistakes: memorizing kubectl instead of the reconciliation model · k8s-because-job-ads (fluency ≠
  adopting it) · no resource limits on the pod.
- Connects: weekQ-3 (same image, heavier orchestrator), weekK-3 (Docker).

**Day 2 — Distributed training: DDP for real** (`2.0.ddp-distributed-training.md`)
- Topics: data-parallel mechanics — replicate model, shard batches, all-reduce gradients (derive that
  averaged gradients == bigger batch); why LR scales with world size; communication overhead as the tax.
- Goals: (1) derive the gradient-averaging equivalence on paper; (2) convert weekG-3's training to DDP and
  run on a 2-GPU spot instance (weekQ-4 workflow); (3) measure the honest speedup (wall-clock, incl. the
  overhead — expect <2×, explain the gap); (4) describe model-parallel and when data-parallel stops being
  enough (concept level, weekP-6's memory math says when).
- Build: the derivation + DDP script (torchrun) + 1-GPU vs 2-GPU table (time/epoch, samples/sec, final
  accuracy — must match!) + the overhead explanation.
- Mistakes: forgetting the DistributedSampler (each GPU sees all data = silent wrongness) · comparing
  against an unoptimized 1-GPU baseline · scaling LR without warmup and blaming DDP for divergence.
- Connects: weekG-5 (AMP + checkpointing carry over), weekQ-4 (the rented hardware), Week 9 (gradient
  descent — still just gradients).

**Day 3 — Profiling & performance** (`3.0.profiling-performance.md`)
- Topics: torch.profiler + trace reading (find the gaps where the GPU idles); the usual suspect
  (DataLoader starvation); AMP + `torch.compile` measured; the profile→fix→re-measure loop as a
  discipline.
- Goals: (1) profile weekG-3's training and produce the time breakdown (data/H2D/forward/backward/step);
  (2) find and fix the biggest bottleneck (workers, pin_memory, prefetch — whatever the trace says, not
  folklore); (3) measure AMP and torch.compile deltas separately; (4) state the final speedup stack
  honestly (compounding, with a table).
- Build: profiler traces before/after + the fix + the ablation table (baseline / +fix / +AMP / +compile).
- Mistakes: optimizing without profiling first · stacking all fixes at once (ablate!) · benchmarking with
  cold caches / first-epoch compilation cost included.
- Connects: weekG-5 (extends it), weekP-6 (same mindset, inference side), Day 2 (profile the DDP run too).

**Day 4 — Chaos day: break it, diagnose from logs alone** (`4.0.chaos-day-incidents.md`)
- Topics: production debugging as a drill; the incident postmortem as a ritual (a model defense for
  failures: timeline → root cause → mechanism → fix → prevention).
- Goals: (1) break the weekQ deployment 5 scripted ways — kill the container mid-request · poison an input
  (malformed payload the API mishandles) · fill the disk · throttle memory until OOM · expire/rotate a
  credential — (2) diagnose each FROM LOGS/METRICS ONLY (no peeking at the break script); (3) write 5
  mini-postmortems; (4) add one prevention per incident (health check, input validation, disk alarm,
  memory limit, secret rotation runbook).
- Build: the 5 break scripts + 5 postmortems (`incidents/`) + the 5 preventions committed.
- Mistakes: diagnosing by re-reading the break script (defeats the drill) · postmortems that name blame
  instead of mechanism · preventions never tested (re-run the break — is it caught now?).
- Connects: weekK-5 (monitoring grows teeth), weekO-6 (traces are how you see), weekJ-1 (tests are
  preventions too).

**Day 5 — Reliability checklist + defense** (`5.0.reliability-defense.md`)
- Build: the standing reliability checklist applied to ALL flagships — health checks, timeouts, retries
  with backoff, graceful degradation (weekO-6's fallback), resource limits, alarms; each item verified,
  not just written.
- Deliverable: `weekR_defense.md` centered on the question every senior interview asks: **"what breaks
  first under 10× load, and how would you know?"** — answered per flagship with evidence from Days 1–4.
- Public bar: postmortems published (M9's post 4 — chaos-day write-up; rare and memorable content).
