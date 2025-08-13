# Installing dependencies

... follow repo setup guide

- Comment out `requirements.txt`

  ```
  # deepspeed==0.16.3
  ..
  # torch==2.1.1+cu121
  # torchaudio==2.1.1+cu121
  # torchvision==0.16.1+cu121
  ```

- Install torch `pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126`
  - run `python -c "import torch; print(torch.__version__)"` to validate
- Install cuda toolkit `conda install nvidia/label/cuda-12.6.0::cuda-nvcc`
  - run `nvcc --version` to validate
- Ensure torch and cuda version match
- install deepspeed
  - in Unisign repo, git clone https://github.com/deepspeedai/DeepSpeed.git
  - cd Deepspeed
  - set DS_BUILD_CUTLASS_OPS=0 DS_BUILD_RAGGED_DEVICE_OPS=0 DS_BUILD_EVOFORMER_ATTN=0 (refer to https://github.com/deepspeedai/DeepSpeed/issues/4669)
  - pip install .
  - run `python -c "import deepspeed; print(deepspeed.__version__)"` to validate

# Downloading mt5-base weights

- pip install huggingface_hub
- huggingface-cli download google/mt5-base --local-dir ./pretrained_weight/mt5-base
