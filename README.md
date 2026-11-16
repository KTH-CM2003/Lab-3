# CM2003 Lab 3: CNN architectures, regularization and transfer learning

In this lab, you will be exploring the following topics:
- Convolutional neural network architectures: AlexNet, VGG and ResNet
- Regularization techniques: dropout, weight decay, data augmentation
- Optimizers: SGD and Adam
- Transfer learning
- Hyperparameter tuning

You will mainly be using the OrganSMNIST dataset (abdominal CT slices of 11 organs, 28x28 grayscale)
and, in the last notebook, DermaMNIST (dermatoscopic images of 7 types of skin lesions, 28x28 colour).
Both are part of [MedMNIST](https://medmnist.com/); the notebooks download them automatically into
`cm2003/datasets/` the first time you run them (about 40 MB in total).

## Setting up the environment

Pick **one** of the options below.

### Option 1: On MAIA

Your MAIA workspace already has a ready-made environment called **`DL_labs_GPU`**, so there is
nothing to install. Clone your repository in a JupyterLab terminal (*File > New > Terminal*), open a
notebook and select the kernel **DL_labs_GPU** (*Kernel > Change Kernel...*). If it is not in the
list, refresh the browser tab.

### Option 2: On your own computer with conda

Install [Miniforge](https://github.com/conda-forge/miniforge) (or use an existing
Anaconda/Miniconda), go to the repository folder in a terminal and run `./setup.sh` (macOS / Linux).
On Windows, run the same steps by hand in the *Miniforge Prompt*:
```bash
conda env create -f environment.yml
conda activate cm2003-lab3
python -m ipykernel install --user --name=cm2003-lab3 --display-name "CM2003 Lab 3"
```
Then open a notebook and select the kernel **CM2003 Lab 3**.

### Option 3: On your own computer with uv

```bash
uv venv --python 3.13
uv pip install -r requirements.txt
uv run python -m ipykernel install --user --name=cm2003-lab3 --display-name "CM2003 Lab 3"
```

### GPU or CPU?

Training VGG and ResNet for several epochs is slow on a CPU, so we recommend MAIA (or another
computer with an NVIDIA GPU) for this lab. The notebooks print the device they use: `cuda` (NVIDIA
GPU), `mps` (Apple-silicon Mac) or `cpu`.

## Getting started
1. Start with the `Convolutional architectures.ipynb` notebook. You will implement the training
   loop in `cm2003/train.py` and the AlexNet, VGG and ResNet architectures in `cm2003/models/`, and
   train them on OrganSMNIST.
2. Continue with the `Improving training and transfer learning.ipynb` notebook. You will improve
   the training of VGG with data augmentation, compare optimizers, and use transfer learning with
   models pre-trained on ImageNet.
3. Finally, use the `Model playground.ipynb` notebook to train the best model you can on
   DermaMNIST. This is an open-ended task: try out the different models and techniques from the
   lab and report what you tried, what worked and what did not. You can write your own
   architecture in `cm2003/models/custom_model.py`.

## Submission

Answer the questions in the notebooks in a separate file and submit it on GitHub with your code.
Please also write a short overview of the results and your observations.
