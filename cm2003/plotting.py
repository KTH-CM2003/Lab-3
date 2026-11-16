import matplotlib.pyplot as plt


def plot_results(results, labels=None, title=None):
    """
    Plot the loss curves and validation accuracy of one or more training runs.

    Args:
        results: the results dictionary returned by cm2003.train.train, or a list of them
            to compare several runs in the same plots.
        labels: a name for each run (used in the legend), e.g. ['Adam', 'SGD'].
        title: an optional title for the figure.
    """
    if isinstance(results, dict):
        results = [results]
    if labels is None:
        labels = [f'Run {i + 1}' for i in range(len(results))] if len(results) > 1 else ['']

    fig, (ax_loss, ax_acc) = plt.subplots(1, 2, figsize=(12, 4))
    for i, (res, label) in enumerate(zip(results, labels)):
        color = f'C{i}'
        prefix = f'{label} ' if label else ''
        epochs = range(1, len(res['train_loss']) + 1)
        ax_loss.plot(epochs, res['train_loss'], color=color, label=f'{prefix}train')
        val_epochs = range(1, len(res['val_loss']) + 1)
        ax_loss.plot(val_epochs, res['val_loss'], color=color, linestyle='--', label=f'{prefix}val')
        ax_acc.plot(val_epochs, res['val_accuracy'], color=color, label=f'{prefix}val' if prefix else 'Validation')

    ax_loss.set_xlabel('Epoch')
    ax_loss.set_ylabel('Loss')
    ax_loss.legend()
    ax_acc.set_xlabel('Epoch')
    ax_acc.set_ylabel('Accuracy')
    ax_acc.legend()
    if title:
        fig.suptitle(title)
    fig.tight_layout()
    plt.show()
