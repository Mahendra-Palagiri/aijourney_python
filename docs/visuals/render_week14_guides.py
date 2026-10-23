"""Worked diagrams for Week 14. Reads local CIFAR-10; never downloads data."""
from pathlib import Path
import numpy as np
from render_weekly_guides import (
    ROOT, INK, BLUE, TEAL, ORANGE, GRAY, PALE, plt, panel, box, arrow, cells,
)
from matplotlib.patches import Rectangle

TARGETS = {
    1: ROOT / '5-AppliedAI/week14/1.1.RealImageData_Normalization_Augmentation.png',
    2: ROOT / '5-AppliedAI/week14/2.3.Split_Indices_and_Transforms.png',
}


def page(day, title, subtitle):
    fig = plt.figure(figsize=(16, 10), dpi=160)
    fig.text(.04, .96, f'WEEK 14  /  DAY {day}  /  WORKED VISUAL', color=TEAL, weight='bold', fontsize=12)
    fig.text(.04, .91, title, fontsize=25, weight='bold')
    fig.text(.04, .87, subtitle, color=GRAY, fontsize=13)
    return fig


def day1():
    from torchvision import datasets
    from PIL import ImageOps
    dataset = datasets.CIFAR10(root=str(ROOT / '5-AppliedAI/week14/Data'),
                              train=True, download=False, transform=None)
    image, label = dataset[0]
    assert dataset.classes[label] == 'frog'
    fig = page(1, 'One image: appearance, axes, and values',
               'CIFAR-10 training image 0 • label 6 = frog • follow the changes without changing the label.')
    # Real source pixels, a deterministic flip for illustration, and a resize.
    for left, title, picture in [(.04, 'Original · 32 × 32', image),
                                  (.235, 'Horizontal flip', ImageOps.mirror(image)),
                                  (.43, 'Resize · 224 × 224', image.resize((224, 224)))]:
        ax = fig.add_axes([left, .57, .165, .235])
        ax.imshow(picture, interpolation='nearest'); ax.axis('off')
        ax.set_title(title, fontsize=13, loc='left', pad=10)
    fig.text(.04, .535, 'Label stays frog. Enlarging the image does not recover missing detail.', fontsize=12)
    ax = panel(fig, (.65, .55, .31, .25), 'Tensor axes: C × H × W')
    rgb = np.asarray(image)
    for i, (name, cmap) in enumerate([('R', 'Reds'), ('G', 'Greens'), ('B', 'Blues')]):
        child = fig.add_axes([.65 + i*.105, .655, .09, .12])
        child.imshow(rgb[:, :, i], cmap=cmap, vmin=0, vmax=255,
                     interpolation='nearest'); child.axis('off'); child.set_title(name, fontsize=12)
    ax.text(0, .23, 'Native tensor: [3, 32, 32]\nResized tensor: [3, 224, 224]', fontsize=14)
    ax.text(0, -.02, '3 channels remain 3 channels.', fontsize=12, color=TEAL)

    ax = panel(fig, (.04, .29, .92, .15), 'What happens to one channel value?')
    for x, color, text in [(0, PALE[2], 'PIL / uint8\n0 … 255'),
                            (.35, PALE[0], 'ToTensor() / float32\n0 … 1'),
                            (.70, PALE[1], 'Normalize(0.5, 0.5)\n−1 … 1')]:
        box(ax, x, .30, .29, .57, text, color, 14)
    arrow(ax, (.295, .59), (.345, .59)); arrow(ax, (.645, .59), (.695, .59))
    ax.text(.10, .03, 'x = 191', fontsize=13)
    ax.text(.395, .03, '191 ÷ 255 ≈ 0.749', fontsize=13)
    ax.text(.715, .03, '(0.749 − 0.5) ÷ 0.5 ≈ 0.498', fontsize=12)
    ax = panel(fig, (.04, .105, .92, .105))
    ax.plot([.04, .96], [.64, .64], color=INK, lw=2)
    for x, raw, norm in [(.04,'0','−1'),(.27,'0.25','−0.5'),(.50,'0.5','0'),(.73,'0.75','0.5'),(.96,'1','1')]:
        ax.plot([x,x], [.59,.69], color=INK)
        ax.text(x, .83, raw, ha='center', fontsize=12)
        ax.text(x, .31, norm, ha='center', fontsize=12, color=TEAL)
    ax.text(.50, 1.16, 'Before Normalize', ha='center', fontsize=11, color=GRAY)
    ax.text(.50, -.05, 'After Normalize · same shape, changed values', ha='center', fontsize=12, color=TEAL)
    fig.text(.04, .043, 'ToTensor already scales RGB pixels. Normalize shifts/scales; it does not guarantee a Gaussian distribution.', fontsize=12, weight='bold')
    fig.text(.04, .017, 'Display normalized tensors: x × 0.5 + 0.5, then permute(1, 2, 0) → H × W × C. Original PIL image is unchanged.', fontsize=11, color=GRAY)
    return fig


def day2():
    fig = page(2, 'Split membership once. Transform on retrieval.',
               'Two dataset objects read the same files. Disjoint indices decide which images each subset can retrieve.')
    ax = panel(fig, (.04, .68, .92, .12))
    box(ax, 0, .30, .73, .47, 'Existing training files · 50,000 images · train=True · download=False', PALE[0], 14)
    box(ax, .77, .30, .23, .47, 'Test · 10,000\nheld aside', PALE[3], 13)
    ax.add_patch(Rectangle((0, -.05), .657, .16, facecolor=BLUE))
    ax.add_patch(Rectangle((.657, -.05), .073, .16, facecolor=TEAL))
    ax.text(.32, -.30, '45,000 training', ha='center', color=BLUE, fontsize=12)
    ax.text(.72, -.30, '5,000 validation', ha='center', color=TEAL, fontsize=12)

    ax = panel(fig, (.04, .39, .92, .19), 'See it with 10 images (8 training + 2 validation)')
    order = [7, 2, 9, 0, 5, 1, 8, 4, 6, 3]
    ax.text(0, .89, 'One shuffled index list:', fontsize=12)
    cells(ax, order, .23, .72, .072, .26, [[PALE[0]]*8 + [PALE[1]]*2], 16)
    ax.plot([.804, .804], [.41, 1], color=INK, lw=1.5, linestyle='--')
    ax.text(.23, .25, 'indices[:8] → training membership', fontsize=12, color=BLUE)
    ax.text(.805, .25, 'indices[8:]\n→ validation', fontsize=11, color=TEAL)
    ax.text(.23, -.05, 'Each index appears once → no overlap. Files and original image positions stay unchanged.', fontsize=12)

    for rect, title, route, steps, color in [
        ((.04,.16,.43,.17), 'Training retrieval', 'train_subset[0] → train_data[7]',
         'Image 7 → random flip/rotation\n→ ToTensor → Normalize → (tensor, label)', PALE[0]),
        ((.54,.16,.42,.17), 'Validation retrieval', 'val_subset[0] → val_data[6]',
         'Image 6 → ToTensor → Normalize\n→ (tensor, label)', PALE[1]),
    ]:
        ax = panel(fig, rect, title)
        box(ax, 0, .60, 1, .35, route, color, 13)
        arrow(ax, (.5,.59), (.5,.41), TEAL)
        ax.text(.04, .14, steps, fontsize=13, va='center')

    fig.text(.04,.090, 'DataLoader shuffle=True changes batch order within training; it does not create a new split.', fontsize=13, weight='bold')
    fig.text(.04,.059, 'Transform runs when an image is retrieved. Training appearance can change while subset membership stays fixed.', fontsize=12)
    fig.text(.04,.023, 'Your code: 50,000 indices → [:45000] and [45000:]. A seeded generator repeats the split; validation uses shuffle=False.', fontsize=11, color=GRAY)
    return fig


if __name__ == '__main__':
    for day, draw in [(1, day1), (2, day2)]:
        target = TARGETS[day].resolve()
        assert str(target).startswith(str(ROOT.resolve()) + '/')
        figure = draw()
        figure.canvas.draw()
        renderer = figure.canvas.get_renderer()
        for text in figure.findobj(plt.matplotlib.text.Text):
            if text.get_visible() and text.get_text():
                bbox = text.get_window_extent(renderer)
                assert bbox.x0 >= -2 and bbox.y0 >= -2 and bbox.x1 <= figure.bbox.width+2 and bbox.y1 <= figure.bbox.height+2, text.get_text()
        figure.savefig(target, dpi=160)
        plt.close(figure)
        print(target)
