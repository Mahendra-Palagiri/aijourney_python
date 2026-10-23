"""Purpose-specific visual examples, not a daily text-card template.

Only creates the ten explicitly listed weekly guide targets. Does not change
lesson text, exercise programs, or earlier diagrams. All examples are synthetic
except Week 8, whose numbers are transcribed from its model-defense report.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp(prefix='weekly-mpl-'))
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[2]
INK, BLUE, TEAL, ORANGE, RED, GRAY = '#172C45', '#236DB5', '#008477', '#D18416', '#BB4654', '#697887'
PALE = ['#E4F0FC', '#DCF3ED', '#FFF0D5', '#EEE6F8', '#FBE3E7', '#E3E9EF']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
                     'text.color': INK, 'axes.labelcolor': INK,
                     'axes.titlecolor': INK, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.facecolor': 'white'})


def page(week, title, subtitle):
    f = plt.figure(figsize=(16, 10), dpi=160)
    f.text(.04, .963, f'WEEK {week:02d}  /  VISUAL LAB', color=TEAL, fontsize=12, weight='bold')
    f.text(.04, .918, title, fontsize=25, weight='bold')
    f.text(.04, .877, subtitle, fontsize=13, color=GRAY)
    return f


def panel(f, rect, title=None):
    ax = f.add_axes(rect)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis('off')
    if title:
        ax.text(0, 1.06, title, fontsize=16, weight='bold', va='bottom')
    return ax


def note(f, text, source='Illustrative example • Read alongside the full lesson'):
    f.text(.04, .052, text, fontsize=14, weight='bold', color=INK)
    f.text(.04, .022, source, fontsize=10, color=GRAY)


def arrow(ax, start, end, color=BLUE, rad=0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=16,
                                linewidth=2, color=color, connectionstyle=f'arc3,rad={rad}'))


def box(ax, x, y, w, h, text, color=PALE[0], size=14):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor='white', linewidth=2))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=size)


def cells(ax, values, x=.05, y=.7, cw=.16, ch=.16, colors=None, size=16):
    a = np.asarray(values, dtype=object)
    if a.ndim == 1:
        a = a[None, :]
    for r in range(a.shape[0]):
        for c in range(a.shape[1]):
            color = colors[r][c] if colors is not None else PALE[0]
            box(ax, x+c*cw, y-r*ch, cw, ch, str(a[r,c]), color, size)


def w1():
    f=page(1, 'Names point to objects. Code changes state.', 'Follow the same list through aliasing, mutation, reassignment, and a function call.')
    positions=[(.04,.52,.43,.27),(.54,.52,.42,.27),(.04,.16,.43,.27)]
    for n,(rect,title) in enumerate(zip(positions,['1  a = [10, 20]; b = a','2  b.append(30)','3  b = [99]'])):
        ax=panel(f,rect,title)
        box(ax,.02,.62,.15,.2,'a',PALE[0],18)
        box(ax,.02,.2,.15,.2,'b',PALE[1],18)
        vals=[10,20] if n==0 else [10,20,30]
        cells(ax,vals,.48,.61,.16,.23)
        arrow(ax,(.18,.72),(.47,.72))
        if n<2:
            arrow(ax,(.18,.3),(.48,.65),TEAL)
            ax.text(.48,.25,'ONE list, TWO names' if n==0 else 'Both names see [10, 20, 30]',fontsize=13)
        else:
            cells(ax,[99],.48,.2,.16,.23,[[PALE[1]]])
            arrow(ax,(.18,.3),(.47,.3),TEAL)
            ax.text(.48,.01,'Rebinding b does not change a.',fontsize=13)
    ax=panel(f,(.54,.16,.42,.27),'4  Trace total(a) through its loop')
    ax.text(0,.89,'def total(a):\n    s = 0\n    for value in a:\n        s += value\n    return s',family='DejaVu Sans Mono',fontsize=11,va='top')
    cells(ax,[['value','s before','s after'],[10,0,10],[20,10,30],[30,30,60]],.44,.74,.18,.18,
          [[PALE[1]]*3]+[[PALE[0]]*3]*3,size=12)
    ax.text(.44,.06,'return 60 → caller receives 60',color=TEAL,fontsize=13)
    note(f,'Predict first: after step 3, what do a and b contain? Trace the arrows to check.')
    return f


def w2():
    f=page(2,'Same values. Different axes. Different results.','Color follows each value so you can see why reshape and transpose are not interchangeable.')
    a=np.arange(1,7).reshape(2,3)
    for rect,title,v in [((.04,.5,.27,.29),'A  ·  shape (2, 3)',a),((.365,.5,.27,.29),'A.T  ·  shape (3, 2)',a.T),((.69,.5,.27,.29),'A.reshape(3, 2)',a.reshape(3,2))]:
        ax=panel(f,rect,title)
        cells(ax,v,.08,.66,.24,.23,[[PALE[int(z)-1] for z in row] for row in v],20)
        ax.text(.08,-.04,'Columns become rows.' if 'A.T' in title else ('Row-major order stays 1, 2, 3, 4, 5, 6.' if 'reshape' in title else 'Read rows left to right.'),fontsize=12)
    ax=panel(f,(.04,.14,.59,.24),'Broadcasting: (2, 3) + (3,) → (2, 3)')
    cells(ax,a,.0,.68,.08,.25,size=17)
    ax.text(.255,.67,'+',fontsize=25)
    cells(ax,[[10,20,30],[10,20,30]],.31,.68,.08,.25,[[PALE[1]]*3]*2,17)
    ax.text(.575,.67,'=',fontsize=25)
    cells(ax,a+np.array([10,20,30]),.64,.68,.09,.25,size=17)
    ax.text(.3,.15,'Same vector applies to each row.\nThe repeated row is conceptual, not a required copy.',fontsize=11)
    ax=panel(f,(.70,.14,.26,.24),'Filtering chooses rows')
    cells(ax,[['score','> 70'],[60,'False'],[80,'True'],[90,'True']],0,.78,.42,.2,
          [[PALE[5]]*2,[PALE[5]]*2,[PALE[1]]*2,[PALE[1]]*2],14)
    ax.text(0,-.05,'Selected scores: [80, 90]; mean = 85',fontsize=11)
    note(f,'Check the cells, not just the shape: two arrays can both be (3, 2) and still differ.')
    return f


def w3():
    f=page(3,'What a decision boundary actually does','Schematic rules on the same toy points—not trained Iris results, and not a model ranking.')
    x=np.array([[-.8,-.6],[-.65,.15],[-.2,-.5],[.5,.65],[.8,.3],[.15,.7],[-.12,.12],[.5,-.3]])
    y=np.array([0,0,0,1,1,1,1,0])
    gx,gy=np.meshgrid(np.linspace(-1,1,220),np.linspace(-1,1,220))
    q=np.c_[gx.ravel(),gy.ravel()]
    rules=[(q[:,0]+q[:,1]>.15).astype(int), ((q[:,0]>.2)|(q[:,1]>.35)).astype(int),y[((q[:,None,:]-x[None,:,:])**2).sum(2).argmin(1)]]
    titles=['Linear score: a straight boundary','Tree-like rule: axis-aligned cuts','1-nearest neighbor: local regions']
    from matplotlib.colors import ListedColormap
    for i,(r,t) in enumerate(zip(rules,titles)):
        ax=f.add_axes([.065+i*.31,.39,.265,.39])
        ax.contourf(gx,gy,r.reshape(gx.shape),levels=[-.5,.5,1.5],cmap=ListedColormap([PALE[0],PALE[2]]))
        for cls,col in [(0,BLUE),(1,ORANGE)]:
            ax.scatter(x[y==cls,0],x[y==cls,1],c=col,s=90,edgecolors='white',linewidths=1.5)
        ax.set(xlim=(-1,1),ylim=(-1,1),xlabel='feature 1',ylabel='feature 2')
        ax.set_title(t,fontsize=13,pad=14)
        ax.scatter([.0],[.25],marker='*',s=190,c=INK,zorder=5)
    ax=panel(f,(.06,.15,.9,.14))
    ax.scatter([.02,.23],[.7,.7],c=[BLUE,ORANGE],s=90)
    ax.text(.045,.7,'known class 0',va='center');ax.text(.255,.7,'known class 1',va='center')
    ax.scatter([.51],[.7],marker='*',s=150,c=INK);ax.text(.535,.7,'same query in every panel',va='center')
    ax.text(0,.12,'Background = the rule’s predicted class at each location.\nA more flexible boundary can fit local patterns—but may also fit noise.',fontsize=15)
    note(f,'Real model selection needs held-out evaluation; a visually intricate boundary is not proof of quality.')
    return f


def w4():
    f=page(4,'Training learns the ruler. Test data only uses it.','A worked imputation + standardization example; all numbers are deliberately small and inspectable.')
    ax=panel(f,(.04,.22,.27,.57),'TRAINING ages')
    cells(ax,[['raw','imputed','scaled'],[20,20,'−1.414'],[30,30,'0'],[40,40,'1.414'],['?',30,'0']],0,.73,.31,.14,
          [[PALE[1]]*3]+[[PALE[0]]*3]*3+[[PALE[2]]*3],13)
    ax.text(0,.0,'Missing value → training median 30',fontsize=12)
    ax=panel(f,(.36,.27,.28,.47),'FITTED STATE (fixed)')
    box(ax,.03,.58,.9,.25,'median = 30',PALE[1],21)
    box(ax,.03,.24,.9,.25,'mean = 30\nstd ≈ 7.071',PALE[0],19)
    ax.text(.03,-.06,'Statistics come from training only.\nStd uses the imputed training values.',fontsize=12)
    ax=panel(f,(.7,.22,.27,.57),'TEST ages')
    cells(ax,[['raw','imputed','scaled'],[100,100,'9.899'],['?',30,'0']],0,.73,.31,.14,
          [[PALE[3]]*3,[PALE[0]]*3,[PALE[2]]*3],13)
    ax.text(0,.12,'100 does NOT change the ruler.\n(100 − 30) ÷ 7.071 ≈ 9.899',fontsize=13)
    ax.text(0,-.02,'No fitting on test rows.',color=RED,weight='bold')
    ax=panel(f,(.04,.11,.92,.06));ax.text(0,.5,'Leakage counterexample: pooling raw train + test values would change the median from 30 to 35.',color=RED,fontsize=13)
    note(f,'Inside CV, each training fold learns its own ruler. Its validation fold only transforms.')
    return f


def confusion(ax,cm):
    ax.imshow(cm,cmap='Blues',vmin=0,vmax=max(5,int(np.max(cm))))
    for r in range(2):
        for c in range(2):
            ax.text(c,r,f'{[["TN","FP"],["FN","TP"]][r][c]}\n{cm[r,c]}',ha='center',va='center',fontsize=19,
                    color='white' if cm[r,c] > .6*max(5,int(np.max(cm))) else INK)
    ax.set_xticks([0,1],['predict 0','predict 1']);ax.set_yticks([0,1],['actual 0','actual 1'])
    ax.tick_params(length=0)


def w5():
    f=page(5,'Move the threshold. Watch the mistakes change.','Eight fixed scores and labels; only the decision threshold changes. Positive when score ≥ threshold.')
    p=np.array([.1,.2,.35,.45,.55,.65,.75,.9]); y=np.array([0,1,0,1,0,1,1,1])
    for i,t in enumerate([.5,.3]):
        ax=f.add_axes([.07+i*.49,.57,.4,.22]);ax.axvspan(t,1,color=PALE[1]);ax.axvline(t,color=TEAL,lw=2)
        for cls,col in [(0,BLUE),(1,ORANGE)]:
            ax.scatter(p[y==cls],np.full(sum(y==cls),cls),s=125,color=col,edgecolor='white',zorder=3)
        for score,label in zip(p,y):ax.text(score,label+.18,f'{score:.2f}',ha='center',fontsize=10)
        ax.set(xlim=(0,1),ylim=(-.4,1.5),xlabel='positive-class score');ax.set_yticks([0,1],['actual 0','actual 1'])
        ax.set_title(f'Threshold {t:.1f}  |  shaded side predicts 1',fontsize=15)
        pred=p>=t;cm=np.array([[sum((y==0)&~pred),sum((y==0)&pred)],[sum((y==1)&~pred),sum((y==1)&pred)]])
        cx=f.add_axes([.09+i*.49,.17,.18,.25]);confusion(cx,cm)
        tx=panel(f,(.3+i*.49,.18,.17,.24));tp,fp,fn=cm[1,1],cm[0,1],cm[1,0]
        tx.text(0,.82,f'Precision\n{tp}/{tp+fp} = {tp/(tp+fp):.2f}',fontsize=17)
        tx.text(0,.36,f'Recall\n{tp}/{tp+fn} = {tp/(tp+fn):.2f}',fontsize=17)
    note(f,'Lowering the threshold finds one more positive here—but also creates one more false alarm.')
    return f


def foldgrid(ax,n,heldout=None):
    ax.set(xlim=(-1,n),ylim=(n,0));ax.axis('off')
    for r in range(n):
        ax.text(-.1,r+.45,f'fit {r+1}',ha='right',va='center',fontsize=12)
        for c in range(n):
            col=ORANGE if r==c else BLUE
            ax.add_patch(Rectangle((c+.025,r+.05),.92,.8,facecolor=col))
            ax.text(c+.48,r+.45,'VAL' if r==c else 'TRAIN',ha='center',va='center',fontsize=10,color='white')
    for c in range(n):ax.text(c+.5,-.3,f'fold {c+1}',ha='center',fontsize=11)


def w7():
    f=page(7,'Cross-validation is repeated separation—not repeated test use.','Blue blocks fit the pipeline. Orange blocks evaluate it. The final test set stays outside selection.')
    ax=panel(f,(.055,.68,.9,.13))
    box(ax,0,.28,.72,.55,'DEVELOPMENT DATA  ·  model and hyperparameter selection',PALE[0],14)
    box(ax,.77,.28,.23,.55,'FINAL TEST\nnot in the CV loop',PALE[3],13)
    ax.plot([.745,.745],[0,1],ls='--',color=GRAY)
    ax=f.add_axes([.07,.25,.4,.31]);foldgrid(ax,5)
    f.text(.07,.605,'Ordinary 5-fold CV',fontsize=18,weight='bold')
    f.text(.075,.16,'Each development row is held out once.\nEvery fit starts a fresh preprocessing + model pipeline.',fontsize=12)
    ax=panel(f,(.56,.2,.4,.38),'Nested CV: zoom into ONE outer split')
    box(ax,0,.7,.68,.22,'OUTER TRAINING',PALE[0],13);box(ax,.73,.7,.27,.22,'OUTER TEST',PALE[3],11)
    for r in range(4):
        for c in range(4):box(ax,c*.17,.52-r*.12,.16,.1,'val' if r==c else 'fit',PALE[2] if r==c else PALE[0],10)
    ax.text(.74,.38,'Never enters\ninner tuning',fontsize=11,color=RED)
    ax.text(0,-.12,'Inner folds choose settings → refit on outer training\n→ score outer test. Repeat for all outer splits.',fontsize=12)
    note(f,'CV folds are not independent experiments; their standard deviation is not automatically a confidence interval.')
    return f


def w8():
    f=page(8,'Your capstone: selection evidence versus final assessment','Recorded Titanic results from reports/model_defense.md—not a new training run.')
    ax=f.add_axes([.24,.49,.67,.29]);means=[.8626,.8639,.8867,.8895];std=[.0132,.0215,.0235,.0214]
    names=['Random forest','Logistic baseline','Gradient boosting','Tuned gradient boosting']
    for i,(m,s) in enumerate(zip(means,std)):
        ax.errorbar(m,i,xerr=s,fmt='o',capsize=7,color=TEAL if i==3 else BLUE,ms=10,lw=2)
        ax.text(.924,i,f'{m:.4f} ± {s:.4f}',va='center',fontsize=12)
    ax.set_yticks(range(4),names);ax.set(xlim=(.82,.995),ylim=(-.6,3.7),xlabel='Development CV ROC-AUC  ·  bars show fold standard deviation')
    ax.invert_yaxis();ax.grid(axis='x',alpha=.2);ax.set_title('Model choice happens here',loc='left',fontsize=16,pad=14)
    ax=f.add_axes([.08,.16,.2,.24]);confusion(ax,np.array([[93,17],[23,46]]))
    ax.set_title('Final holdout counts',fontsize=14,pad=14)
    ax=panel(f,(.4,.18,.55,.2),'After selection is frozen: holdout ROC-AUC = 0.8079')
    ax.text(0,.72,'0.8895  →  0.8079',fontsize=28,weight='bold',color=TEAL)
    ax.text(0,.3,'Different data, different role.\nThe drop is evidence to investigate—not permission to retune on test.',fontsize=14)
    note(f,'The highest CV mean is not a promise of the same test score; error bars above are not confidence intervals.',
         'Source: 3-MLFoundations/week8/reports/model_defense.md • Values reproduced as recorded')
    return f


def w9():
    f=page(9,'One forward pass. One gradient. One smaller loss.','A single linear neuron, with bias fixed at 0: input x = 2, target y = 3, initial weight w = 1.')
    ax=panel(f,(.06,.59,.88,.2))
    for x,text in [(0,'x = 2'),(.24,'× w = 1'),(.48,'prediction = 2'),(.75,'L = (2 − 3)² = 1')]:box(ax,x,.48,.21,.4,text,PALE[0],15)
    for x in [.21,.45,.69]:arrow(ax,(x,.68),(x+.03,.68))
    arrow(ax,(.79,.2),(.57,.2),TEAL);arrow(ax,(.5,.2),(.3,.2),TEAL)
    ax.text(.59,-.04,'dL/dprediction = −2',fontsize=13,color=TEAL)
    ax.text(.12,-.04,'dL/dw = (−2) × 2 = −4',fontsize=13,color=TEAL)
    ax=f.add_axes([.09,.15,.45,.31]);w=np.linspace(.65,1.95,200);ax.plot(w,(2*w-3)**2,color=BLUE,lw=3)
    ax.scatter([1,1.4],[1,.04],s=110,color=[ORANGE,TEAL],zorder=4)
    ax.annotate('before: w=1, L=1',(1,1),xytext=(.7,1.7),arrowprops={'arrowstyle':'->'},fontsize=12)
    ax.annotate('after: w=1.4, L=0.04',(1.4,.04),xytext=(1.2,.65),arrowprops={'arrowstyle':'->'},fontsize=12)
    ax.set(xlabel='weight w',ylabel='loss (2w − 3)²',ylim=(-.05,2.8));ax.grid(alpha=.15)
    ax=panel(f,(.63,.19,.33,.26),'Update with learning rate 0.1')
    ax.text(0,.74,'w_new = 1 − 0.1 × (−4)\n           = 1.4',fontsize=19)
    ax.text(0,.35,'New prediction = 2 × 1.4 = 2.8\nNew loss = (2.8 − 3)² = 0.04',fontsize=15)
    ax.text(0,.02,'Backward computes the slope.\nThe optimizer changes the weight.',fontsize=13,color=TEAL)
    note(f,'The graph makes the roles visible: forward computes values; backward computes derivatives; step updates.')
    return f


def w10():
    f=page(10,'Batches preserve pairs. Gradients preserve history.','Two independent worked examples of what PyTorch stores—not just a list of API names.')
    ax=panel(f,(.04,.2,.43,.58),'A  TensorDataset → batches of two')
    vals=[['X','y'],[1,2],[2,4],[3,6],[4,8],[5,10],[6,12]]
    colors=[[PALE[5]]*2]+[[PALE[i//2]]*2 for i in range(6)]
    cells(ax,vals,0,.8,.19,.11,colors,14)
    for i in range(3):
        yy=.67-i*.26
        arrow(ax,(.4,.745-i*.22),(.61,yy))
        v=2*i+1
        box(ax,.63,yy-.08,.36,.17,f'batch {i+1}: X=[{v}, {v+1}]\ny=[{2*v}, {2*(v+1)}]',PALE[i],11)
    ax.text(0,-.04,'Each batch has X shape [2, 1] and y shape [2, 1].\nRows stay paired when shuffled. 6 samples → 3 batches.',fontsize=12)
    ax=panel(f,(.56,.2,.4,.58),'B  w.grad is an accumulator')
    events=['zero_grad()','forward + backward()','fresh forward + backward()','zero_grad()','fresh forward + backward()','optimizer.step()']
    grads=['0 / None','−4','−8','0 / None','−4','−4 (not cleared)']
    for i,(e,g) in enumerate(zip(events,grads)):
        yy=.82-i*.13
        ax.text(0,yy,e,va='center',fontsize=12)
        box(ax,.64,yy-.045,.34,.095,g,PALE[2] if i==2 else PALE[1],12)
    ax.text(0,-.08,'For L=(2w−3)² at w=1, each backward adds −4.\nA step with lr=0.1 changes w to 1.4, not grad to 0.',fontsize=12)
    note(f,'Clear gradients between ordinary training steps. eval() and no_grad() do not clear existing gradients.')
    return f


def w11():
    f=page(11,'Convolution and pooling: follow the numbers','One-channel arithmetic first. Kernel 2 × 2, stride 1, no padding, zero bias; kernel is not flipped.')
    a=np.array([[1,1,0,0,0],[1,2,2,0,0],[0,2,3,3,0],[0,0,3,4,4],[0,0,0,4,5]])
    k=np.array([[0,1],[1,0]])
    out=np.array([[np.sum(a[r:r+2,c:c+2]*k) for c in range(4)]for r in range(4)])
    pooled=np.array([[out[r:r+2,c:c+2].max() for c in [0,2]]for r in [0,2]])
    assert out[0,0]==2 and pooled.shape==(2,2)
    ax=panel(f,(.04,.4,.27,.38),'Input: 5 × 5')
    colors=[[PALE[2] if r<2 and c<2 else PALE[5] for c in range(5)]for r in range(5)]
    cells(ax,a,0,.72,.18,.18,colors,16)
    ax=panel(f,(.36,.48,.17,.3),'Kernel: 2 × 2')
    cells(ax,k,0,.59,.4,.26,[[PALE[2]]*2]*2,19)
    ax.text(0,.0,'First output:\n1×0 + 1×1\n+ 1×1 + 2×0 = 2',fontsize=13)
    ax=panel(f,(.59,.4,.2,.38),'Feature map: 4 × 4')
    cols=[[PALE[(r//2)*2+c//2] for c in range(4)]for r in range(4)]
    cells(ax,out,0,.72,.23,.2,cols,16)
    ax=panel(f,(.84,.48,.13,.3),'Max pool')
    cells(ax,pooled,0,.57,.48,.25,[[PALE[0],PALE[1]],[PALE[2],PALE[3]]],18)
    ax.text(0,.05,'2 × 2 window\nstride 2\n→ 2 × 2 map',fontsize=12)
    ax=panel(f,(.055,.15,.9,.14),'Now change the channel count: RGB input, eight filters')
    for x,w,t in [(0,.23,'[N, 3, 5, 5]\nRGB input'),(.28,.23,'[N, 8, 4, 4]\n8 output maps'),(.56,.18,'[N, 8, 2, 2]\nafter pooling'),(.79,.19,'[N, 32]\nflattened')]:box(ax,x,.16,w,.54,t,PALE[0],13)
    for x,z in [(.23,.28),(.51,.56),(.74,.79)]:arrow(ax,(x,.42),(z,.42))
    note(f,'Each RGB filter spans all 3 input channels. Pooling shrinks height/width, not the number of channels.')
    return f


FUNCTIONS={1:w1,2:w2,3:w3,4:w4,5:w5,7:w7,8:w8,9:w9,10:w10,11:w11}


def folder(w):
    stage='1-PythonFundations' if w<=2 else '2-DataAnalysis_Visualization' if w<=4 else '3-MLFoundations' if w<=8 else '4-DeepLearningFoundations'
    return ROOT / stage / f'week{w}'


if __name__=='__main__':
    import argparse
    # Use current revisions for targets refined after the original weekly pass.
    from render_refined_guides import SPECS
    current_draws = {relative: draw for relative, draw, _, _ in SPECS}
    p=argparse.ArgumentParser();p.add_argument('--week',type=int);args=p.parse_args()
    for week,fn in FUNCTIONS.items():
        if args.week is not None and week!=args.week:continue
        target=(folder(week)/'0.1.Weekly_Visual_Guide.png').resolve()
        assert ROOT in target.parents
        draw = current_draws.get(str(target.relative_to(ROOT)), fn)
        fig=draw();fig.canvas.draw()
        # Check all text against the canvas. Panel overlaps receive visual QA.
        renderer=fig.canvas.get_renderer()
        for text in fig.findobj(matplotlib.text.Text):
            if text.get_visible() and text.get_text():
                bb=text.get_window_extent(renderer)
                if bb.x0 < -2 or bb.y0 < -2 or bb.x1>fig.bbox.width+2 or bb.y1>fig.bbox.height+2:
                    raise ValueError(f'Off-canvas text, week {week}: {text.get_text()}')
        fig.savefig(target,dpi=160)
        plt.close(fig)
        print(json.dumps({'week':week,'output':str(target)}))
