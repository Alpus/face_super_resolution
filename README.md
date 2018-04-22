# Super-Resolution for Face Recognition Improvement


Repository based on:
* [LightCNN](https://github.com/AlfredXiangWu/LightCNN)
* [SRGAN](https://github.com/aitorzip/PyTorch-SRGAN)


## Data

If you want to reproduce work with datasets:
1) Download and place data in corresponding directories
    * [Aligned LFW](http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz) -> `data/datasets/lfw/lfw_funneled`
    * [Aligned and cropped MS-Celeb-1M ](https://msceleb.blob.core.windows.net/msceleb-v1/FaceImageCroppedWithAlignment.tsv) -> `data/datasets/ms_celeb/FaceImageCroppedWithAlignment.tsv`
    * [Filtered list of MS-Celeb-1M](https://pan.baidu.com/s/1gfxB0iB) -> `data/datasets/ms_celeb/MS-Celeb-1M_clean_list.txt`
2) And run `dataset_preparing.ipynb`

[Weights for LightCNN](https://drive.google.com/file/d/0ByNaVHFekDPRWk5XUFRvTTRIVmc/view) -> `data/weights/light_cnn`

## Train

You can reproduce train pipeline using `srgan_training.ipynb`


## Results

||ROC AUC|
|---|---|
|Real-HR|`0.982`|
|LR|`0.935`|

You can reproduce results using `recognition_test.ipynb`
