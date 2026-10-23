# Learning images: coverage by week and day

**Current coverage: 41 PNGs and one interactive convolution visualizer.** This sheet describes what the images explain, without separating earlier edits from recent edits.

**Sufficient** means the image set summarizes the main concepts and relationships for that week/day. It does not replace the full lesson, detailed derivations or every practice exercise. Files are grouped by topic where one image would be crowded.

## Weekly coverage

| Week | PNGs | Main visual coverage | Sufficient? |
| --- | ---: | --- | --- |
| 1 | 2 | Python values, control flow, collections, objects, references and loop state. | **Yes — core visual summary.** |
| 2 | 3 | NumPy axes, broadcasting, filtering; Pandas aggregation and chart choice. | **Yes — core visual summary.** |
| 3 | 2 | Features/labels, classifiers, decision regions, splitting and model selection. | **Yes — core visual summary.** |
| 4 | 2 | Missing data, scaling, encoding, column pipelines and training-only fitting. | **Yes — core visual summary.** |
| 5 | 3 | Logistic scores, coefficients, regularization, confusion metrics, thresholds and ROC/AUC. | **Yes — core visual summary.** |
| 6 | 6 | Regression fit, MAE/MSE/RMSE, Ridge, residuals, target caps, leverage and influence. | **Yes — core visual summary.** |
| 7 | 3 | Ordinary/nested CV, selection versus assessment, learning curves and bias/variance clues. | **Yes — core visual summary.** |
| 8 | 2 | Tabular capstone workflow, leakage boundaries, CV comparisons and holdout evidence. | **Yes — core visual summary.** |
| 9 | 2 | Network anatomy, nonlinear activations, forward pass, chain rule and parameter updates. | **Yes — core visual summary.** |
| 10 | 3 | Dataset/batch pairing, gradients, parameter state, epoch metrics and evaluation mode. | **Yes — core visual summary.** |
| 11 | 2 | Convolution, stride/padding, pooling, RGB channels, feature maps and shape flow. | **Yes — core visual summary.** |
| 12 | 2 | Deep-learning project workflow, baseline/CNN paths, measured validation results and defense. | **Yes — core visual summary.** |
| 13 | 6 | NLP framing, tokens, TF-IDF, classification, embeddings, retrieval and RAG. | **Yes — core visual summary.** |
| 14 | 3 | Day 1: image transformations. Day 2: split, training toolkit and model-selection controls. | **Days 1–2: yes. Whole week: not yet.** |

Week 6's six images consist of three interpretation/summary guides and three recorded diagnostic plots. Week 11 also has the interactive HTML visualizer in addition to its two PNGs.

## Day-specific coverage

| Week / day | Coverage | Sufficient? |
| --- | --- | --- |
| 13 Day 1 | NLP framing is represented through the classification, retrieval and RAG examples; no separate orientation poster. | Yes, through shared diagrams |
| 13 Day 2 | Text → tokens → vocabulary IDs → padding | Yes |
| 13 Day 3 | Document-term counts → DF/IDF → numeric TF-IDF weights | Yes |
| 13 Day 4 | Split raw text → fit features/model → transform unseen text → evaluate | Yes |
| 13 Day 5 | Embedding/vector context, exact cosine geometry, numeric similarity calculation | Yes |
| 13 Day 6 | Indexing → query embedding → filtered search → ranked source chunks | Yes |
| 13 Day 7 | Retrieval-augmented generation, evidence, sources and evaluation boundaries | Yes |
| 14 Day 1 | Actual CIFAR-10 image, augmentation, RGB planes, tensor shape, scaling and normalization | Yes |
| 14 Day 2 | Training toolkit overview and disjoint subset/index mapping | Yes as concept summary; experiment curves require actual saved history |
| Later Week 14 days / later Addendum lessons | Not represented by this reviewed image set | **Not covered** |

Earlier weeks are grouped by concept rather than forced into daily image counts. No extra day number is invented where the curriculum uses phases or combined days.

## Images — open by week

### Week 1

- [A single state trace shows aliasing, mutation, reassignment, and a loop result](../../1-PythonFundations/week1/0.1.Weekly_Visual_Guide.png)
- [Python control flow collections and objects](../../1-PythonFundations/week1/0.2.Python_Program_and_Objects.png)

### Week 2

- [Array axes and reshape](../../1-PythonFundations/week2/0.1.Weekly_Visual_Guide.png)
- [Broadcasting and masks](../../1-PythonFundations/week2/0.2.Broadcasting_and_Masks.png)
- [Pandas aggregation and plotting](../../1-PythonFundations/week2/0.3.Pandas_and_Plotting.png)

### Week 3

- [Decision regions and query predictions](../../2-DataAnalysis_Visualization/week3/0.1.Weekly_Visual_Guide.png)
- [Features labels and model selection](../../2-DataAnalysis_Visualization/week3/0.2.ML_Workflow.png)

### Week 4

- [Training-only preprocessing arithmetic](../../2-DataAnalysis_Visualization/week4/0.1.Weekly_Visual_Guide.png)
- [Mixed column preprocessing pipeline](../../2-DataAnalysis_Visualization/week4/0.2.Mixed_Column_Pipeline.png)

### Week 5

- [The same eight predictions under two thresholds link individual mistakes to confusion counts, precision, and recall.](../../3-MLFoundations/week5/0.1.Weekly_Visual_Guide.png)
- [Logistic scores and regularization](../../3-MLFoundations/week5/0.2.Logistic_Model_and_Regularization.png)
- [ROC thresholds and AUC ranking](../../3-MLFoundations/week5/0.3.ROC_and_Ranking.png)

### Week 6

- [Residual sign and target-cap geometry](../../3-MLFoundations/week6/0.1.Residual_Interpretation.png)
- [Recorded leverage residual and influence](../../3-MLFoundations/week6/0.2.Influence_Interpretation.png)
- [Regression fitting, error metrics and Ridge](../../3-MLFoundations/week6/0.3.Regression_Fit_and_Metrics.png)
- [Residual diagnostic plots](../../3-MLFoundations/week6/4.1Regression_diagnostics.png)
- [Cook's distance](../../3-MLFoundations/week6/5.1CooksDistancePlot.png)
- [Leverage versus studentized residual](../../3-MLFoundations/week6/5.2Leverage_StudentizedResidual.png)

### Week 7

- [Ordinary cross-validation](../../3-MLFoundations/week7/0.1.Weekly_Visual_Guide.png)
- [Nested selection and assessment](../../3-MLFoundations/week7/0.2.Nested_Cross_Validation.png)
- [Learning curve diagnoses](../../3-MLFoundations/week7/0.3.Learning_Curves.png)

### Week 8

- [A chart of the recorded capstone CV means and spread, separated from holdout results, replaces six generic workflow summaries.](../../3-MLFoundations/week8/0.1.Weekly_Visual_Guide.png)
- [Tabular capstone workflow and selection boundaries](../../3-MLFoundations/week8/0.2.Capstone_Workflow.png)

### Week 9

- [One numerical forward/backward/update example connects the derivative to movement on an actual loss curve.](../../4-DeepLearningFoundations/week9/0.1.Weekly_Visual_Guide.png)
- [Nonlinear hidden features and network anatomy](../../4-DeepLearningFoundations/week9/0.2.Activations_and_Nonlinearity.png)

### Week 10

- [Batch pairing and partial batch](../../4-DeepLearningFoundations/week10/0.1.Weekly_Visual_Guide.png)
- [Weight gradient and graph state](../../4-DeepLearningFoundations/week10/0.2.Autograd_State.png)
- [Epoch workflow and metrics](../../4-DeepLearningFoundations/week10/0.3.Training_and_Evaluation.png)

### Week 11

- [Convolution windows and pooling](../../4-DeepLearningFoundations/week11/0.1.Weekly_Visual_Guide.png)
- [RGB filters output maps and shapes](../../4-DeepLearningFoundations/week11/0.2.Channels_and_Shapes.png)
- [Interactive convolution visualizer](../../4-DeepLearningFoundations/week11/4.2.cnn_convolution_visualizer.html)

### Week 12

- [Deep learning capstone workflow](../../4-DeepLearningFoundations/week12/0.1.Capstone_Workflow.png)
- [Observed capstone results and model defense](../../4-DeepLearningFoundations/week12/7.1.Learning_Flow.png)

### Week 13

- [Text Cleaning, Tokenization, and Vocabulary](../../5-AppliedAI/week13/2.1.Learning_Flow.png)
- [Numerical bag-of-words and TF-IDF](../../5-AppliedAI/week13/3.1.Learning_Flow.png)
- [Text feature fit and held-out transform](../../5-AppliedAI/week13/4.2.Learning_Flow.png)
- [Correct cosine geometry and arithmetic](../../5-AppliedAI/week13/5.1.Learning_Flow.png)
- [Index search filter and ranking](../../5-AppliedAI/week13/6.2.Learning_Flow.png)
- [LLMs, Grounding, RAG, and Retrospective](../../5-AppliedAI/week13/7.1.Learning_Flow.png)

### Week 14

- [Real CIFAR-10 image, channel axes, pixel scaling and normalization](../../5-AppliedAI/week14/1.1.RealImageData_Normalization_Augmentation.png)
- [Deep-learning training toolkit overview](../../5-AppliedAI/week14/2.1.DeepLearning_Training_Toolkit.png)
- [Shuffled indices, subset membership, separate transforms and batch order](../../5-AppliedAI/week14/2.3.Split_Indices_and_Transforms.png)

## Scope and checks

- All previous review recommendations for Weeks 1–13 have been implemented, including the separate Week 2/7/10/11 companions and cosine/retrieval corrections.
- Week 5 includes ROC/AUC, Week 6 includes regression fitting/metrics, and Weeks 8/12 include the complete project flow as well as recorded results.
- Worked diagrams use visible numbers, state changes, axes or data paths. Toy examples are labeled; recorded results are attributed. Training was not rerun to manufacture new charts.
- Rendered PNGs were visually inspected. File integrity, local links, archive hashes, canonical paths and representative arithmetic are verified. The existing HTML visualizer's browser interactions were not retested.
- Lesson prose and exercise programs remain intact. [Backups](archive/refinement-2026-10-23/) and [archived text cards](archive/text-card-batch/) are recoverable; they are not gaps in current coverage.
- The [MasterPlan map](../../MasterPlan/1-PROGRAM-MAP.md) places later curriculum in Addendum weeks; this sheet does not claim those future lessons are covered.

[Machine-readable inventory](curated-visuals.json) · [Rendering sources and maintenance](README.md)
