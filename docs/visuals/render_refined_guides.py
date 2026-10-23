"""Lesson-grounded companion diagrams. No model training or network access.

Each image answers a specific learning question. Recorded results are attributed;
toy data are labeled. Existing targets are backed up before their first revision.
"""
import json
import shutil
from pathlib import Path
import numpy as np
from render_weekly_guides import (
    ROOT, INK, BLUE, TEAL, ORANGE, RED, GRAY, PALE,
    plt, page, panel, note, arrow, box, cells, foldgrid, w3, w4,
)
from matplotlib.patches import Rectangle


def matrix(ax, values, color=PALE[0], size=16):
    a = np.asarray(values, dtype=object)
    cells(ax, a, .02, .78, .94/a.shape[1], .65/a.shape[0],
          [[color]*a.shape[1] for _ in a], size)


def stages(fig, labels, y=.55, colors=None):
    n = len(labels); width = .9/n
    ax = panel(fig, (.05, y, .9, .19))
    for i, label in enumerate(labels):
        box(ax, i/n, .25, width, .58, label,
            colors[i] if colors else PALE[i % len(PALE)], 13)
        if i < n-1:
            arrow(ax, (i/n+width,.54), ((i+1)/n,.54))
    return ax


def axes_reshape():
    f=page(2,'Array axes: transpose is not reshape','Week 2 · NumPy • same six values; follow both the value and its original coordinate.')
    a=np.array([['1 (0,0)','2 (0,1)','3 (0,2)'],['4 (1,0)','5 (1,1)','6 (1,2)']])
    for rect,title,v in [((.04,.34,.28,.43),'A · (2, 3)',a),((.37,.34,.25,.43),'A.T · (3, 2)',a.T),((.7,.34,.26,.43),'reshape · (3, 2)',a.reshape(3,2))]:
        ax=panel(f,rect,title)
        colors=[[PALE[int(str(value)[0])-1] for value in row] for row in v]
        cells(ax,v,.02,.78,.94/v.shape[1],.65/v.shape[0],colors,14)
    f.text(.05,.24,'Transpose swaps coordinates:\nA[0, 1] = 2 → A.T[1, 0] = 2',fontsize=16)
    f.text(.55,.24,'Reshape keeps row-major reading order:\n1 → 2 → 3 → 4 → 5 → 6',fontsize=16)
    f.text(.06,.12,'Reshape requires the same cell count: 2×3 = 3×2 = 6. Parentheses above retain each value’s ORIGINAL coordinate.',fontsize=13,color=TEAL)
    note(f,'Both outputs are (3, 2). Inspect the cells: equal shapes do not imply equal arrays.')
    return f


def python_state():
    f=page(1,'A program receives values, branches, and changes objects','Week 1 · types, control flow, collections and classes • follow one concrete score through the program.')
    stages(f,['input() returns\n"72" (str)','int("72")\n72 (int)','score ≥ 70?\nTrue (bool)','Return "pass"\nthen print it'],y=.58)
    ax=panel(f,(.06,.16,.42,.31),'Choose a collection for its job')
    matrix(ax,[['structure','example','access'],['list','[72, 85]','scores[0] → 72'],['tuple','(3, 4)','point[1] → 4'],['dict','score: 72',"record['score'] → 72"]],size=13)
    ax=panel(f,(.57,.16,.37,.31),'Two instances, separate attributes')
    box(ax,0,.65,1,.25,'Student A: score 72',PALE[0],16)
    box(ax,0,.17,1,.25,'Student B: score 85',PALE[1],16)
    ax.text(0,1.0,'A.score += 1',fontsize=14,color=TEAL)
    ax.text(0,.01,'A becomes 73; B remains 85.',fontsize=14)
    note(f,'A function returns a value to its caller. A method receives an instance (self); that instance owns its attributes.')
    return f


def nonlinear_network():
    f=page(9,'Activation makes stacked layers more than one linear map','Week 9 · network anatomy + nonlinear features • a designed XOR example, not a trained benchmark.')
    ax=f.add_axes([.08,.39,.36,.38]);ax.scatter([0,1],[0,1],color=BLUE,s=150,label='class 0');ax.scatter([0,1],[1,0],color=ORANGE,s=150,label='class 1');ax.set(xlim=(-.3,1.3),ylim=(-.3,1.3),xticks=[0,1],yticks=[0,1],xlabel='x1',ylabel='x2',title='No single straight line separates XOR');ax.legend(loc='upper center',fontsize=10)
    ax=panel(f,(.55,.40,.39,.35),'A hidden nonlinear feature')
    ax.text(0,.84,'h1 = ReLU(x1 − x2)\nh2 = ReLU(x2 − x1)\noutput = h1 + h2 = |x1 − x2|',fontsize=17,va='top',linespacing=1.7)
    ax.text(0,.04,'ReLU(z) = max(0, z)\nHidden units keep different regions active.',fontsize=14)
    ax=panel(f,(.06,.14,.88,.15))
    matrix(ax,[['input','h1','h2','output'],['(0,0) or (1,1)',0,0,0],['(1,0)',1,0,1],['(0,1)',0,1,1]],size=14)
    note(f,'Without activation: W2(W1x+b1)+b2 is still affine. Learning adjusts weights; the nonlinearity expands what can be represented.')
    return f


def broadcasting():
    f=page(2,'Broadcast dimensions. Select rows with a mask.','Week 2 · NumPy • broadcasting changes how arithmetic aligns; a mask chooses which rows survive.')
    ax=panel(f,(.05,.48,.55,.29),'A + v: compare dimensions from the right')
    matrix(ax,[['A','2','3'],['v','1','3'],['result','2','3']],size=16)
    ax=panel(f,(.67,.48,.28,.29),'Compatible: equal or 1')
    ax.text(0,.77,'(2, 3) + (3,)\n→ (2, 3)',fontsize=21)
    ax.text(0,.33,'(2, 3) + (2,)\n→ error: 3 ≠ 2',fontsize=19,color=RED)
    ax=panel(f,(.05,.15,.55,.24),'One vector applies to each row')
    matrix(ax,[['A row','v','result'],['1, 2, 3','10, 20, 30','11, 22, 33'],['4, 5, 6','10, 20, 30','14, 25, 36']],size=14)
    ax=panel(f,(.67,.15,.28,.24),'Mask: score > 70')
    matrix(ax,[['row','score','keep'],['r0',60,'False'],['r1',80,'True'],['r2',90,'True']],size=13)
    note(f,'Mask [False, True, True] selects r1 and r2: scores [80, 90], mean 85. Their row identities stay attached.')
    return f


def pandas_plotting():
    f=page(2,'A table becomes groups, then a readable chart','Week 2 · Pandas + plotting • a tiny sales table connects filtering, aggregation and visualization.')
    ax=panel(f,(.05,.45,.42,.32),'Original rows')
    matrix(ax,[['day','shop','sales'],[3,'A',30],[1,'A',10],[2,'B',20],[1,'B',5]],size=15)
    ax=panel(f,(.57,.48,.37,.29),'groupby(shop).sales.sum()')
    matrix(ax,[['shop','total'],['A',40],['B',25]],size=17)
    ax=f.add_axes([.08,.16,.34,.20]); ax.bar(['A','B'],[40,25],color=[BLUE,TEAL]);ax.set(ylabel='total sales',title='Bar: compare categories',ylim=(0,48))
    ax=f.add_axes([.59,.16,.34,.20]); ax.plot([1,2,3],[15,20,30],marker='o',color=BLUE); ax.set(xticks=[1,2,3],xlabel='day',ylabel='daily total',title='Line: sort days before connecting')
    note(f,'A histogram answers a different question: how many observations fall in each numeric interval?')
    return f


def query_boundary():
    f=w3()
    for ax,label in zip(f.axes[:3],['query (0, 0.25) → class 1','query (0, 0.25) → class 0','nearest point → class 1']):
        ax.text(.5,1.16,label,transform=ax.transAxes,ha='center',fontsize=11,color=TEAL)
    f.axes[2].plot([0,-.12],[.25,.12],ls='--',color=INK,lw=1.5)
    return f


def model_workflow():
    f=page(3,'Features in. A learned decision out.','Week 3 · ML workflow • example Iris row has 4 measurements and one species label.')
    ax=panel(f,(.05,.52,.43,.26),'X: measurements, y: the answer')
    matrix(ax,[['sepal L','sepal W','petal L','petal W'],[5.1,3.5,1.4,.2]],size=15)
    ax.text(0,.03,'y = setosa · label is not an input feature',fontsize=14,color=TEAL)
    ax=panel(f,(.57,.52,.37,.26),'One task, alternative classifiers')
    ax.text(0,.82,'KNN → nearby labeled samples\nLogistic → linear class scores\nTree → a sequence of feature cuts',fontsize=16,linespacing=1.7,va='top')
    stages(f,['Split raw rows','Fit scaler + model\non training only','Tune inside\ntraining CV','Predict untouched\nheld-out rows'],y=.26)
    f.text(.06,.14,'Compare the same folds and metric. Scaling matters for distances; a tree does not require it.',fontsize=14)
    note(f,'Classification predicts a category. Regression predicts a number. Evaluation checks predictions against held-out labels.')
    return f


def fit_ruler():
    f=w4()
    f.text(.37,.19,'std = √((100 + 0 + 100 + 0) ÷ 4)\n      = √50 ≈ 7.071  (population std)',fontsize=11,color=TEAL)
    return f


def mixed_pipeline():
    f=page(4,'Different columns need different preparation','Week 4 · ColumnTransformer + Pipeline • split first; fit every learned step on training rows only.')
    ax=panel(f,(.05,.59,.28,.2),'One raw row')
    matrix(ax,[['age','city'],['missing','B']],size=17)
    ax=panel(f,(.43,.42,.51,.35),'Parallel column paths')
    box(ax,0,.66,1,.24,'age → median 30 → scale (mean 30, std 7.071) → 0',PALE[0],13)
    box(ax,0,.22,1,.24,'city B → fitted vocabulary [A, B, C] → [0, 1, 0]',PALE[1],14)
    # Parallel routes from the raw row; neither column pipeline feeds the other.
    for endpoint in [(.43,.69),(.43,.54)]:
        ax.annotate('',xy=endpoint,xycoords=fig_coords(f),xytext=(.33,.65),
                    textcoords=fig_coords(f),arrowprops={'arrowstyle':'->','color':BLUE,'lw':2})
    stages(f,['Concatenate\n[0, 0, 1, 0]','Select features\nfit on training only','Classifier\nRF / SVM / logistic'],y=.16)
    f.text(.06,.105,'Held-out row: reuse the same median, scale, category columns and selected features.',fontsize=14)
    note(f,'One-hot columns encode categories without inventing an order. Keep target y out of the feature transformer.')
    return f


def logistic_core():
    f=page(5,'Logistic regression turns a linear score into probability','Week 5 · fitting, interpretation and regularization • toy coefficients, not Titanic measurements.')
    ax=f.add_axes([.07,.44,.42,.34]);z=np.linspace(-6,6,240);p=1/(1+np.exp(-z)); ax.plot(z,p,color=BLUE,lw=3)
    ax.scatter([0],[.5],color=TEAL,s=80);ax.axhline(.5,ls='--',color=GRAY);ax.set(xlabel='linear score z = w·x + b',ylabel='positive-class probability',ylim=(0,1),title='Sigmoid: 1 ÷ (1 + exp(−z))')
    ax=panel(f,(.59,.46,.35,.29),'Interpret coefficients in log-odds')
    ax.text(0,.83,'z = −1 + 0.5 × x\nx = 2 → z = 0 → p = 0.5',fontsize=18)
    ax.text(0,.34,'Holding other features fixed:\nx rises by 1 → log-odds rise by 0.5\n→ odds multiply by exp(0.5) ≈ 1.65',fontsize=14)
    ax=panel(f,(.06,.15,.88,.19),'Regularization limits coefficient growth')
    box(ax,0,.3,.29,.51,'L2: squared penalty\nshrinks coefficients',PALE[0],14)
    box(ax,.35,.3,.29,.51,'L1: absolute penalty\ncan produce exact zeros',PALE[1],14)
    box(ax,.70,.3,.29,.51,'Smaller C\nstronger regularization',PALE[2],14)
    note(f,'Learn coefficients by reducing log loss + penalty. Choose C with validation/CV, then examine threshold trade-offs separately.')
    return f


def residual_geometry():
    f=page(6,'Read the residual sign before diagnosing the pattern','Week 6 · regression diagnostics • schematic geometry explains the boundary in your recorded plots.')
    ax=f.add_axes([.08,.37,.43,.40]);x=np.linspace(0,7,100)
    ax.fill_between(x,x-5,4,color=PALE[0]); ax.plot(x,x-5,color=ORANGE,lw=3,label='target cap y = 5 → r = prediction − 5')
    ax.axhline(0,color=GRAY);ax.scatter([2,4],[1,-1],s=100,color=[TEAL,RED]);ax.set(xlim=(0,7),ylim=(-5,4),xlabel='prediction',ylabel='residual = prediction − actual',title='If actual ≤ 5, residual ≥ prediction − 5')
    ax.legend(loc='upper left',fontsize=9)
    ax=panel(f,(.61,.38,.33,.39),'Trace two observations')
    matrix(ax,[['pred','actual','residual'],[2,1,'+1'],[4,5,'−1']],size=16)
    ax.text(0,.02,'Positive → overprediction\nNegative → underprediction',fontsize=15)
    stages(f,['Read axis + sign','Check label cap\nand data quality','Inspect unexplained\ncurve / changing spread'],y=.12)
    note(f,'The cap creates a geometric boundary. That boundary alone does not establish nonlinearity or unequal error variance.',
         'Source: week6/4.RegressionDiagnositcs.py • Original recorded scatterplots are retained separately')
    return f


def influence():
    f=page(6,'A large error and a large influence are different','Week 6 · recorded training diagnostics • points below are the ten saved top-Cook’s-D rows, not all training rows.')
    ids=np.array([2757,2580,225,10876,3798,9659,1080,4023,10332,2308])
    cook=np.array([2.001294,1.904147,.484712,.135771,.123410,.051227,.037541,.036925,.036688,.026171])
    lev=np.array([.576413,.403434,.117223,.067223,.054898,.051593,.004830,.033731,.033101,.047587])
    resid=np.array([3.638,5.034,-5.732,4.118,-4.373,2.911,-8.343,-3.085,-3.106,-2.171])
    ax=f.add_axes([.08,.35,.39,.42]);ax.bar(np.arange(10),cook,color=BLUE);ax.set_xticks(np.arange(10),ids,rotation=60);ax.set(ylabel="Cook's distance",xlabel='saved training-row position',title='Influence: how much the fit can change')
    threshold=4/13209;ax.axhline(threshold,color=RED,ls='--',label=f'4/n ≈ {threshold:.5f} (near zero)');ax.legend(fontsize=10)
    ax=f.add_axes([.59,.35,.34,.42]);ax.scatter(lev,resid,s=50+100*cook,color=TEAL);ax.axhline(0,color=GRAY);ax.set(xlabel='leverage',ylabel='studentized residual',title='Bubble size also reflects Cook’s D')
    for i,offset in [(0,(-95,-22)),(1,(-70,10)),(6,(12,0))]:ax.annotate(str(ids[i]),(lev[i],resid[i]),xytext=offset,textcoords='offset points',arrowprops={'arrowstyle':'->'},fontsize=11)
    f.text(.07,.18,'Row 1080: largest error among these rows, but modest leverage.\nRow 2757: high leverage plus error → much larger Cook’s D.',fontsize=16)
    note(f,'4/n is a screening heuristic, not a deletion rule. Verify data and compare validation results before deciding what to do.',
         'Source: week6/6.InfluenceRemoval_vs_Ridge.py saved top-10 output • n = 13,209 • no model rerun')
    return f


def cv_ordinary():
    f=page(7,'One held-out fold per fit. One fresh pipeline per fit.','Week 7 · ordinary CV • each development row is validation once; the final test set stays outside selection.')
    ax=f.add_axes([.07,.28,.43,.44]);foldgrid(ax,5)
    ax=panel(f,(.61,.30,.32,.42),'A complete fit for one row of the grid')
    ax.text(0,.85,'1  Fit imputer/scaler on blue rows\n\n2  Fit model on those transformed rows\n\n3  Transform orange rows; score only\n\n4  Discard fit; start fresh next fold',fontsize=14,va='top')
    ax=panel(f,(.07,.13,.86,.10))
    ax.text(0,.9,'Toy fold scores: [0.80, 0.84, 0.82, 0.78, 0.86] → mean = 0.82',fontsize=17)
    note(f,'Use consistent folds and metric to compare candidates. Fold spread is descriptive; it is not automatically a confidence interval.')
    return f


def cv_nested():
    f=page(7,'Nested CV evaluates the selection procedure','Week 7 · inner folds choose settings; outer held-out rows assess the tuned procedure.')
    ax=panel(f,(.05,.61,.90,.17))
    box(ax,0,.22,.68,.65,'OUTER TRAIN: samples A, B, C, D',PALE[0],18)
    box(ax,.73,.22,.27,.65,'OUTER HELD-OUT: E',PALE[3],15)
    ax=f.add_axes([.08,.28,.42,.23]);foldgrid(ax,4)
    f.text(.08,.56,'1  Inner CV on A–D: compare settings',fontsize=17,weight='bold')
    ax=panel(f,(.60,.24,.34,.28),'2  Refit → 3  Assess')
    box(ax,0,.65,1,.27,'Refit chosen pipeline on ALL A–D',PALE[0],13)
    arrow(ax,(.5,.64),(.5,.49))
    box(ax,0,.20,1,.27,'Transform E → predict E → outer score',PALE[3],12)
    f.text(.07,.14,'E never enters its own inner search. Rotate outer folds so every sample is held out once.',fontsize=15)
    note(f,'Aggregate outer scores to assess the procedure. A separate final test, if reserved, remains untouched until decisions are finished.')
    return f


def learning_curves():
    f=page(7,'Use learning curves to choose the next experiment','Week 7 · illustrative patterns, not measured results • vertical axis is error, so lower is better.')
    n=np.array([20,40,80,160,320]); curves=[([.30,.32,.33,.34,.34],[.50,.43,.39,.37,.36]),([.03,.06,.09,.12,.14],[.55,.43,.33,.26,.22])]
    for i,((train,val),title) in enumerate(zip(curves,['High errors converge: possible high bias','Gap narrows: more data may help'])):
        ax=f.add_axes([.08+i*.49,.36,.37,.40]);ax.plot(n,train,'o-',label='training',color=BLUE);ax.plot(n,val,'o-',label='validation',color=ORANGE);ax.set(xlabel='training sample count',ylabel='error',ylim=(0,.6),title=title);ax.legend()
    f.text(.08,.19,'Try richer useful features / capacity.\nAlso check optimization and label quality.',fontsize=15)
    f.text(.57,.19,'Try more data or regularization.\nConfirm with a controlled comparison.',fontsize=15)
    note(f,'These patterns are clues, not automatic diagnoses. Change one factor and keep the validation protocol fixed.')
    return f


def batches():
    f=page(10,'Dataset pairs stay together when batch order changes','Week 10 · TensorDataset / DataLoader • five samples, batch_size=2, drop_last=False.')
    ax=panel(f,(.05,.33,.35,.44),'Original paired samples')
    matrix(ax,[['index','X','y'],[0,1,2],[1,2,4],[2,3,6],[3,4,8],[4,5,10]],size=16)
    ax=panel(f,(.52,.33,.42,.44),'Example shuffled order: [3, 0, 4, 1, 2]')
    for i,(rows,xs,ys) in enumerate([('3, 0','4, 1','8, 2'),('4, 1','5, 2','10, 4'),('2','3','6')]):
        box(ax,0,.70-i*.26,1,.22,f'Batch {i+1} · indices [{rows}]\nX=[{xs}] and y=[{ys}]',PALE[i],15)
    f.text(.06,.16,'First two batches: X [2, 1], y [2, 1]. Last batch: X [1, 1], y [1, 1].',fontsize=16)
    note(f,'For this regression example y has one column. Class-index labels in classification usually have shape [N].')
    return f


def gradient_state():
    f=page(10,'Track the weight separately from its gradient','Week 10 · autograd state • L=(2w−3)², starting w=1; SGD learning rate 0.1, no momentum or decay.')
    ax=panel(f,(.05,.19,.90,.58))
    matrix(ax,[['event','w','w.grad','graph'],['start / zero_grad\n(set_to_none=True)',1,'None','none'],['forward → backward',1,-4,'new graph consumed'],['fresh forward → backward',1,-8,'second graph consumed'],['zero_grad(set_to_none=True)',1,'None','none'],['fresh forward → backward',1,-4,'new graph consumed'],['optimizer.step()',1.4,-4,'no graph rebuilt'],['next forward',1.4,-4,'new graph; prediction 2.8']],size=13)
    note(f,'Backward accumulates gradients. step changes parameters, not grad. None means absent; zero is an existing zero-valued gradient.')
    return f


def torch_workflow():
    f=page(10,'One epoch contains many optimizer steps','Week 10 · nn.Module + loss + optimizer • shared metrics, different training and evaluation behavior.')
    stages(f,['Dataset → batches','model.train()','For EACH batch:\nzero → forward → loss','backward → step'],y=.57)
    ax=panel(f,(.08,.33,.84,.17),'Aggregate across samples, not equally across batches')
    ax.text(0,.8,'Batch sizes 64 and 16; mean losses 1 and 3\nEpoch loss = (64×1 + 16×3) ÷ 80 = 1.4  (not 2.0)',fontsize=20,va='top')
    stages(f,['model.eval()','no_grad()','Forward + loss\n(no weight update)','Record validation\nloss and accuracy'],y=.12)
    note(f,'eval() controls layer behavior. no_grad() controls gradient recording. Neither changes dataset transforms.')
    return f


def spatial_cnn():
    f=page(11,'Move the window. Compute one output at a time.','Week 11 · convolution arithmetic • cross-correlation as used by CNNs: do not flip the kernel.')
    a=np.array([[1,2,0],[0,3,1],[2,1,4]]);k=np.array([[1,0],[0,1]])
    for rect,title,v in [((.05,.46,.25,.31),'Input · 3 × 3',a),((.38,.46,.20,.31),'Kernel · 2 × 2',k),((.70,.46,.24,.31),'Feature map · 2 × 2',[[4,3],[1,7]])]:
        ax=panel(f,rect,title);matrix(ax,v,size=20)
    f.text(.06,.34,'Top-left: 1×1 + 2×0 + 0×0 + 3×1 = 4\nMove right: 2×1 + 0×0 + 3×0 + 1×1 = 3',fontsize=16)
    f.text(.61,.34,'Pool the map with a 2×2 window:\nmax = 7 · average = (4+3+1+7) ÷ 4 = 3.75',fontsize=15)
    ax=panel(f,(.06,.13,.88,.12))
    ax.text(0,.85,'Output size = floor((input + 2×padding − kernel) ÷ stride) + 1',fontsize=18,color=TEAL)
    ax.text(0,.36,'3×3, kernel 2, stride 1, padding 0 → 2×2. Stride 2 → 1×1. Formula assumes dilation 1.',fontsize=14)
    note(f,'Convolution learns kernel values. Pooling summarizes a window; it does not learn a kernel.')
    return f


def channel_cnn():
    f=page(11,'One filter spans every input channel','Week 11 · channels and architecture • one output map sums channel contributions, then adds one bias.')
    ax=panel(f,(.05,.49,.90,.29),'At one spatial location: three 2×2 planes')
    for i,(name,a,k) in enumerate([('R',[[1,2],[3,4]],[[1,0],[0,0]]),('G',[[5,6],[7,8]],[[0,1],[0,0]]),('B',[[9,10],[11,12]],[[0,0],[1,0]])]):
        x=i*.34
        ax.text(x,.95,name,fontsize=17,color=[RED,TEAL,BLUE][i])
        tint=[PALE[4],PALE[1],PALE[0]][i]
        cells(ax,a,x,.68,.07,.22,[[tint]*2]*2,size=15);ax.text(x+.15,.64,'×',fontsize=20);cells(ax,k,x+.19,.68,.065,.22,[[tint]*2]*2,size=13)
        ax.text(x,.02,f'contribution = {[1,6,11][i]}',fontsize=15)
    f.text(.06,.40,'One filter output = 1 + 6 + 11 + bias 0 = 18. A different filter learns a different feature.',fontsize=17,color=TEAL)
    stages(f,['[N, 3, 32, 32]\nRGB input','Conv: 16 filters\n[N, 16, 32, 32]','Pool 2×2\n[N, 16, 16, 16]','Flatten\n[N, 4096]'],y=.15)
    note(f,'Here Conv uses kernel 3, padding 1, stride 1. Pooling changes H/W; output filter count determines channels.')
    return f


def capstone_evidence():
    f=page(12,'Defend the model with observed evidence','Week 12 · FashionMNIST capstone • approximate recorded observations from the 50-epoch comparison.')
    ax=f.add_axes([.08,.45,.35,.33]);ax.bar(['Baseline MLP','CNN candidate'],[.7218,.6949],color=[BLUE,ORANGE]);ax.set(ylim=(0,1),ylabel='validation accuracy',title='Baseline higher by 2.69 percentage points')
    for i,v in enumerate([.7218,.6949]):ax.text(i,v+.025,f'{100*v:.2f}%',ha='center',fontsize=17)
    ax=panel(f,(.56,.47,.38,.30),'Same comparison, validation loss')
    matrix(ax,[['model','loss ↓'],['Baseline','≈ 0.8145'],['CNN','≈ 0.8340']],size=17)
    ax=panel(f,(.05,.14,.90,.19))
    box(ax,0,.33,.23,.45,'Images\n[N, 1, 28, 28]',PALE[0],13)
    box(ax,.32,.61,.37,.32,'Baseline: flatten 784 → hidden → 10',PALE[0],11)
    box(ax,.32,.06,.37,.32,'CNN: conv/pool → 32×7×7 → 10',PALE[2],11)
    box(ax,.77,.33,.23,.45,'Same validation\nprotocol',PALE[1],12)
    for start,end in [((.23,.56),(.32,.77)),((.23,.56),(.32,.22)),((.69,.77),(.77,.56)),((.69,.22),(.77,.56))]:arrow(ax,start,end)
    note(f,'Observed winner: baseline in this experiment. Next: test one controlled CNN change; this result does not rank all CNNs.',
         'Source: week12/7.0.retrospective.md, “What Actually Happened” • No invented training curve or final-test score')
    return f


def tfidf():
    f=page(13,'From words to counts to TF-IDF weights','Day 3 · a three-document training corpus • raw-count TF, smoothed natural-log IDF, no row normalization here.')
    ax=panel(f,(.05,.48,.41,.30),'Document-term counts')
    matrix(ax,[['document','good','bad','product'],['good product\ngood',2,0,1],['bad product',0,1,1],['good product',1,0,1]],size=13)
    ax=panel(f,(.58,.49,.36,.28),'One column at a time')
    ax.text(0,.85,'N = 3 documents\nDF(good)=2 · DF(bad)=1\nDF(product)=3',fontsize=17,linespacing=1.6,va='top')
    f.text(.06,.37,'IDF(term) = ln((1 + N) ÷ (1 + DF(term))) + 1',fontsize=20,color=TEAL)
    ax=panel(f,(.06,.14,.88,.17))
    matrix(ax,[['term','IDF','document 1: TF × IDF'],['good','ln(4/3)+1 ≈ 1.288','2 × 1.288 ≈ 2.575'],['product','ln(4/4)+1 = 1','1 × 1 = 1']],size=15)
    note(f,'Training learns vocabulary + IDF. Held-out documents only transform. L2 normalization, if enabled, rescales the row afterward.')
    return f


def text_classification():
    f=page(13,'Fit text features once. Reuse them on unseen text.','Day 4 · text classification • a worked toy vocabulary makes the training/held-out boundary visible.')
    ax=panel(f,(.05,.50,.40,.27),'Training text + labels')
    matrix(ax,[['message','class'],['package late','delivery'],['payment failed','billing']],size=15)
    ax=panel(f,(.57,.50,.37,.27),'Training fits the feature state')
    ax.text(0,.81,'Vocabulary:\nfailed, late, package, payment\nLearn IDF + classifier parameters\nRetain the fitted pipeline',fontsize=15,linespacing=1.5,va='top')
    stages(f,['Unseen message\n“package failed”','Existing vocabulary\n[1, 0, 1, 0] counts','Apply stored IDF\nthen classifier','Predict class\ncompare with true label'],y=.19)
    f.text(.07,.105,'Inspect confusion counts, class imbalance, duplicates and mistakes. No invented predicted class is shown.',fontsize=13)
    note(f,'Split raw messages first. Fit vocabulary, IDF and model on training only; keep duplicates/groups out of both sides.')
    return f


def cosine():
    f=page(13,'Cosine compares direction, not vector length','Day 5 · toy 2D vectors for exact geometry; axes are unnamed embedding dimensions, not semantic concepts.')
    for i,(b,title) in enumerate([([2,0],'Same direction: +1'),([0,1],'Perpendicular: 0'),([-1,0],'Opposite: −1')]):
        ax=f.add_axes([.07+i*.32,.47,.24,.30]);ax.axhline(0,color=GRAY,lw=.7);ax.axvline(0,color=GRAY,lw=.7)
        ax.arrow(0,0,1,0,width=.025,length_includes_head=True,color=BLUE,zorder=3)
        # Slight vertical offset is NOT used: parallel means the same direction.
        ax.arrow(0,0,b[0],b[1],width=.012,length_includes_head=True,color=TEAL,zorder=4,alpha=.75)
        ax.set(xlim=(-1.4,2.4),ylim=(-.5,1.5),aspect='equal',title=title,xticks=[-1,0,1,2],yticks=[0,1]);ax.set_xlabel('dimension 1')
    ax=panel(f,(.07,.16,.86,.18),'A numeric example: a = [1, 2], b = [2, 1]')
    ax.text(0,.85,'a·b = 1×2 + 2×1 = 4     ||a|| = ||b|| = √5\ncosine(a,b) = 4 ÷ (√5 × √5) = 0.8',fontsize=20,va='top')
    ax.text(0,-.10,'Scaling b to [4, 2] doubles dot product and norm → cosine remains 0.8.',fontsize=14,color=TEAL)
    note(f,'Embeddings come from a model. Similarity is not probability, truth, or guaranteed meaning; cosine is undefined for a zero vector.')
    return f


def retrieval():
    f=page(13,'Build the index once. Search it for every query.','Day 6 · retrieval returns source chunks • all vectors and scores below are illustrative, not model measurements.')
    stages(f,['Source documents','Chunks + metadata','Compatible embeddings','Stored index'],y=.59)
    ax=panel(f,(.05,.39,.90,.12))
    box(ax,0,.2,.29,.65,'Question → query embedding',PALE[1],13)
    box(ax,.36,.2,.28,.65,'SEARCH the stored index',PALE[0],14)
    box(ax,.71,.2,.29,.65,'Ranked source chunks',PALE[2],14)
    arrow(ax,(.29,.52),(.36,.52));arrow(ax,(.64,.52),(.71,.52))
    # Cross-panel link: the stored index feeds search, not the output list.
    ax.annotate('',xy=(.50,.50),xycoords=fig_coords(f),xytext=(.85,.62),
                textcoords=fig_coords(f),arrowprops={'arrowstyle':'->','color':TEAL,'lw':2})
    f.text(.61,.59,'index supplies candidates',color=TEAL,fontsize=12)
    ax=panel(f,(.07,.12,.86,.20),'Filter first in this example: language = en, then top-k = 2')
    matrix(ax,[['chunk','language','toy cosine','action'],['A: return policy','en',.92,'rank 1'],['B: return policy','fr',.95,'excluded'],['C: shipping help','en',.71,'rank 2']],size=14)
    note(f,'Top-k is a count, not a confidence threshold. Inspect evidence relevance; generating an answer is a separate step.')
    return f


P='1-PythonFundations';D='2-DataAnalysis_Visualization';M='3-MLFoundations';L='4-DeepLearningFoundations';N='5-AppliedAI'
# Relative path, draw function, title, lesson source. Existing indices were checked.
SPECS=[
 (f'{P}/week1/0.2.Python_Program_and_Objects.png',python_state,'Python control flow collections and objects','docs/curriculum/1-PythonFundations/1.week1.md'),
 (f'{P}/week2/0.1.Weekly_Visual_Guide.png',axes_reshape,'Array axes and reshape','docs/curriculum/1-PythonFundations/2.week2.md'),
 (f'{P}/week2/0.2.Broadcasting_and_Masks.png',broadcasting,'Broadcasting and masks','docs/curriculum/1-PythonFundations/2.week2.md'),
 (f'{P}/week2/0.3.Pandas_and_Plotting.png',pandas_plotting,'Pandas aggregation and plotting','docs/curriculum/1-PythonFundations/2.week2.md'),
 (f'{D}/week3/0.1.Weekly_Visual_Guide.png',query_boundary,'Decision regions and query predictions','docs/curriculum/2-DataAnalysis_Visualization/3.week3.md'),
 (f'{D}/week3/0.2.ML_Workflow.png',model_workflow,'Features labels and model selection','docs/curriculum/2-DataAnalysis_Visualization/3.week3.md'),
 (f'{D}/week4/0.1.Weekly_Visual_Guide.png',fit_ruler,'Training-only preprocessing arithmetic','docs/curriculum/2-DataAnalysis_Visualization/4.week4.md'),
 (f'{D}/week4/0.2.Mixed_Column_Pipeline.png',mixed_pipeline,'Mixed column preprocessing pipeline','docs/curriculum/2-DataAnalysis_Visualization/4.week4.md'),
 (f'{M}/week5/0.2.Logistic_Model_and_Regularization.png',logistic_core,'Logistic scores and regularization','docs/curriculum/3-MLFoundations/5.week5.md'),
 (f'{M}/week6/0.1.Residual_Interpretation.png',residual_geometry,'Residual sign and target-cap geometry',f'{M}/week6/4.RegressionDiagnositcs.py'),
 (f'{M}/week6/0.2.Influence_Interpretation.png',influence,'Recorded leverage residual and influence',f'{M}/week6/6.InfluenceRemoval_vs_Ridge.py'),
 (f'{M}/week7/0.1.Weekly_Visual_Guide.png',cv_ordinary,'Ordinary cross-validation','docs/curriculum/3-MLFoundations/7.week7.md'),
 (f'{M}/week7/0.2.Nested_Cross_Validation.png',cv_nested,'Nested selection and assessment','docs/curriculum/3-MLFoundations/7.week7.md'),
 (f'{M}/week7/0.3.Learning_Curves.png',learning_curves,'Learning curve diagnoses','docs/curriculum/3-MLFoundations/7.week7.md'),
 (f'{L}/week9/0.2.Activations_and_Nonlinearity.png',nonlinear_network,'Nonlinear hidden features and network anatomy',f'{L}/week9/3.ForwardPropagation_ActivationFunctions.md'),
 (f'{L}/week10/0.1.Weekly_Visual_Guide.png',batches,'Batch pairing and partial batch',f'{L}/week10/5.0.pytorch_datapiplelines-dataset-tensordataset-dataloader.md'),
 (f'{L}/week10/0.2.Autograd_State.png',gradient_state,'Weight gradient and graph state',f'{L}/week10/3.0.pytorch_gradients_autograd.md'),
 (f'{L}/week10/0.3.Training_and_Evaluation.png',torch_workflow,'Epoch workflow and metrics',f'{L}/week10/6.0.pytorch_workflow.md'),
 (f'{L}/week11/0.1.Weekly_Visual_Guide.png',spatial_cnn,'Convolution windows and pooling',f'{L}/week11/4.0.cnnmath_stride_padding.md'),
 (f'{L}/week11/0.2.Channels_and_Shapes.png',channel_cnn,'RGB filters output maps and shapes',f'{L}/week11/2.0.CNN_ImageTensorShapes.md'),
 (f'{L}/week12/7.1.Learning_Flow.png',capstone_evidence,'Observed capstone results and model defense',f'{L}/week12/7.0.retrospective.md'),
 (f'{N}/week13/3.1.Learning_Flow.png',tfidf,'Numerical bag-of-words and TF-IDF',f'{N}/week13/3.0.Bag-of-words_TF-IDF.md'),
 (f'{N}/week13/4.2.Learning_Flow.png',text_classification,'Text feature fit and held-out transform',f'{N}/week13/4.0.TextClassificationWorkflow.md'),
 (f'{N}/week13/5.1.Learning_Flow.png',cosine,'Correct cosine geometry and arithmetic',f'{N}/week13/5.0.Embeddings_CosineSimilarity.md'),
 (f'{N}/week13/6.2.Learning_Flow.png',retrieval,'Index search filter and ranking',f'{N}/week13/6.0.SemanticSearch_Retrieval.md'),
]


def fig_coords(figure):
    return figure.transFigure


def roc_ranking():
    f=page(5,'A threshold gives a decision. AUC evaluates ranking.','Week 5 · same eight toy scores as the confusion-matrix guide • 5 positives, 3 negatives.')
    scores=np.array([.1,.2,.35,.45,.55,.65,.75,.9]);actual=np.array([0,1,0,1,0,1,1,1])
    tpr=[0.];fpr=[0.]
    for threshold in sorted(scores,reverse=True):
        positive=scores>=threshold;tpr.append(sum(positive & (actual==1))/5);fpr.append(sum(positive & (actual==0))/3)
    ax=f.add_axes([.09,.31,.40,.45]);ax.plot(fpr,tpr,'o-',color=BLUE);ax.plot([0,1],[0,1],'--',color=GRAY)
    for threshold,label,offset in [(.5,'threshold 0.5',(15,-27)),(.3,'threshold 0.3',(12,-30))]:
        positive=scores>=threshold;x=sum(positive & (actual==0))/3;y=sum(positive & (actual==1))/5
        ax.scatter([x],[y],s=100,color=TEAL,zorder=4);ax.annotate(label,(x,y),xytext=offset,textcoords='offset points',fontsize=11)
    ax.set(xlim=(0,1),ylim=(0,1.05),xlabel='FPR = FP ÷ actual negatives',ylabel='TPR = TP ÷ actual positives',title='ROC: sweep the threshold')
    ax=panel(f,(.59,.35,.35,.36),'Count positive-negative pairs')
    wins=sum(p>n for p in scores[actual==1] for n in scores[actual==0])
    assert wins == 12
    ax.text(0,.84,'5 × 3 = 15 pairs\nPositive score wins 12 pairs\nAUC = 12 ÷ 15 = 0.8',fontsize=19,va='top',linespacing=1.6)
    ax.text(0,.12,'No ties in this example.\nA tie would contribute half a win.',fontsize=14)
    f.text(.08,.15,'Changing one threshold changes TP/FP counts; it does not change these fixed scores or their AUC.',fontsize=15)
    note(f,'Select an operating threshold using validation and error costs. For rare positives, also inspect precision-recall behavior.')
    return f


def regression_core():
    f=page(6,'Fit a line. Measure its errors. Control its weights.','Week 6 · toy data and exact arithmetic • lines have no intercept; this is not a new housing-data experiment.')
    x=np.array([1.,2.,3.]);y=np.array([2.,4.,8.]);ols=float(x@y/(x@x));ridge=float(x@y/(x@x+1))
    ax=f.add_axes([.08,.35,.40,.42]);ax.scatter(x,y,s=110,color=INK,label='observed');grid=np.linspace(0,3.3,100)
    ax.plot(grid,ols*grid,color=BLUE,label=f'OLS w={ols:.3f}');ax.plot(grid,ridge*grid,color=TEAL,label=f'Ridge w={ridge:.3f}')
    for xx,yy in zip(x,y):ax.plot([xx,xx],[yy,ols*xx],':',color=GRAY)
    ax.set(xlabel='x',ylabel='y',title='Dotted segments are prediction errors');ax.legend(fontsize=11)
    ax=panel(f,(.59,.36,.35,.38),'Squared error makes large misses costly')
    ax.text(0,.85,'OLS minimizes Σ(y − wx)²\nw = Σxy ÷ Σx² = 34 ÷ 14\n\nRidge adds λw², here λ=1\nw = 34 ÷ (14 + 1)',fontsize=16,va='top',linespacing=1.6)
    f.text(.07,.18,'For predictions [2, 4, 6] versus actual [2, 4, 8]:\nMAE = 2/3 ≈ 0.667 · MSE = 4/3 ≈ 1.333 · RMSE ≈ 1.155',fontsize=17)
    note(f,'Ridge shrinks w here; that does not prove better generalization. Choose regularization with validation, then inspect residuals.')
    return f


def capstone_protocol():
    f=page(8,'The capstone is a sequence of evidence boundaries','Week 8 · Titanic project • keep model selection separate from the final holdout assessment.')
    ax=panel(f,(.05,.45,.90,.32),'Split raw rows before any learned preprocessing')
    box(ax,0,.48,.20,.34,'Titanic rows\nX + survival y',PALE[0],14)
    box(ax,.30,.68,.31,.25,'Development rows → CV folds',PALE[0],14)
    box(ax,.30,.12,.31,.25,'Final holdout → keep locked',PALE[3],14)
    arrow(ax,(.20,.65),(.30,.80));arrow(ax,(.20,.65),(.30,.24))
    box(ax,.71,.68,.29,.25,'Fit prep + candidates\ninside each training fold',PALE[1],12)
    box(ax,.71,.12,.29,.25,'Assess after selection\nusing fitted pipeline',PALE[3],12)
    arrow(ax,(.61,.80),(.71,.80));arrow(ax,(.61,.24),(.71,.24))
    stages(f,['Baseline + candidates','Choose/tune with CV\nconsistent metric','Refit selected pipeline\non development rows','Unlock final holdout\nwrite model defense'],y=.15)
    note(f,'Record split, metric, CV spread, final score and limitations. Use the results companion for saved measurements.',
         'Sources: docs/curriculum/3-MLFoundations/8.week8.md and week8/reports/model_defense.md')
    return f


def dl_capstone_protocol():
    f=page(12,'From FashionMNIST batches to a defensible comparison','Week 12 · project phases • compare a flattened baseline with a CNN under a consistent validation protocol.')
    ax=panel(f,(.05,.45,.90,.32),'Two model paths start from the same image representation')
    box(ax,0,.43,.22,.34,'Batch: [N, 1, 28, 28]\nclass labels: [N]',PALE[0],13)
    box(ax,.32,.69,.34,.23,'Baseline: flatten → hidden → 10 logits',PALE[0],11)
    box(ax,.32,.13,.34,.23,'CNN: conv/pool → flatten → 10 logits',PALE[2],11)
    box(ax,.77,.43,.23,.34,'CrossEntropyLoss\ncompare with labels',PALE[1],12)
    for start,end in [((.22,.60),(.32,.80)),((.22,.60),(.32,.24)),((.66,.80),(.77,.60)),((.66,.24),(.77,.60))]:arrow(ax,start,end)
    stages(f,['Train: zero gradients\nforward/loss/backward/step','Validate: eval + no_grad\nloss and accuracy','Compare recorded\nvalidation evidence','Select + defend\nlimitations and next trial'],y=.15)
    note(f,'Compare validation evidence before choosing a model. More epochs or greater complexity do not guarantee improvement.',
         'Sources: Week 12 framing, baseline/CNN training, comparison and retrospective lessons')
    return f


SPECS += [
 (f'{M}/week5/0.3.ROC_and_Ranking.png',roc_ranking,'ROC thresholds and AUC ranking','docs/curriculum/3-MLFoundations/5.week5.md'),
 (f'{M}/week6/0.3.Regression_Fit_and_Metrics.png',regression_core,'Regression fitting error metrics and Ridge','docs/curriculum/3-MLFoundations/6.week6.md'),
 (f'{M}/week8/0.2.Capstone_Workflow.png',capstone_protocol,'Tabular capstone selection and assessment','docs/curriculum/3-MLFoundations/8.week8.md'),
 (f'{L}/week12/0.1.Capstone_Workflow.png',dl_capstone_protocol,'Deep learning capstone end-to-end workflow','docs/curriculum/4-DeepLearningFoundations/12.week12.md'),
]


def render(only=None):
    import hashlib
    import matplotlib
    for relative,draw,title,source in SPECS:
        if only and draw.__name__ not in only:
            continue
        target=(ROOT/relative).resolve()
        assert str(target).startswith(str(ROOT.resolve())+'/')
        assert (ROOT/source).is_file(), source
        figure=draw();figure.canvas.draw();renderer=figure.canvas.get_renderer()
        for text in figure.findobj(matplotlib.text.Text):
            if text.get_visible() and text.get_text():
                b=text.get_window_extent(renderer)
                assert b.x0>=-2 and b.y0>=-2 and b.x1<=figure.bbox.width+2 and b.y1<=figure.bbox.height+2,(relative,text.get_text())
        archive=ROOT/'docs/visuals/archive/refinement-2026-10-23'/relative
        is_replacement = ('0.1.Weekly_Visual_Guide' in relative or '/week13/' in relative or relative.endswith('/7.1.Learning_Flow.png'))
        if target.exists() and not archive.exists() and is_replacement:
            archive.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,archive)
        figure.savefig(target,dpi=160);plt.close(figure)
        print(json.dumps({'path':relative,'title':title,'source':source,
                          'archivePath':str(archive.relative_to(ROOT)) if archive.exists() else None,
                          'archiveSha256':hashlib.sha256(archive.read_bytes()).hexdigest() if archive.exists() else None}))


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--only', nargs='+', help='Render selected function names after a layout repair')
    render(parser.parse_args().only)
