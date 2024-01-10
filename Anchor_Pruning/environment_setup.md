# Setup environment for anchor pruning
1. Create a new environment and activate it.
    ```shell=
    conda create -n anchor_pruning python=3.8
    conda activate anchor_pruning
    ```
2. Install pytorch and cuda.
    ```shell=
    conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
    ```
3. Test out pytorch installation. You can use the following python script to check if your GPU driver and CUDA is enabled and accessible by PyTorch.
    ```shell=
    import torch
    torch.cuda.is_available()
    d = torch.cuda.current_device()
    torch.cuda.get_device_name(d)
    ```
4. Follow the [instruction](https://github.com/Mxbonn/anchor_pruning/tree/master#installation) to install other required packages.