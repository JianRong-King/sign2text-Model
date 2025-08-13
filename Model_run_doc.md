## How to run the model

Do your usual conda env set up 

```
conda create --name glofe python=3.8
conda activate glofe
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=11.3 -c pytorch -c conda-forge
pip install -r requirements.txt
```


## Just Follow ReadMe.md for the file & config

Download the How2Sign Model Weights from the pre training google drive link and extract the file and replace the one in models. 


Can reference the file paths as below:
```


dataset - path: sign2text-Model\how2sign\dataset\openpose_output\json
model weight / vn model path : sign2text-Model\how2sign\vn_model


```


## For Inference

```
python train_how2_pose_DDP_inter_VN.py --ngpus 1 --work_dir_prefix "Ur model path dir" --work_dir "how2sign\vn_model" --tokenizer "notebooks/how2sign/how2sign-bpe25000-tokenizer-uncased" --bs 40 --prefix test-vn --phase test --weights "how2sign\vn_model\glofe_vn_how2sign_0224.pt"
```