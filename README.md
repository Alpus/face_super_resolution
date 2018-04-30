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

Trained on MS-Celeb-1M dataset. You can reproduce train pipeline using `srgan_training.ipynb`


## Results

All approaches tested on LWF 6000 pairs.

||ROC AUC|
|---|---|
|**Real HR**|**`0.98207`**|
|SRGAN with Light CNN 9 loss (MFM4)|`0.96767`|
|SRGAN with VGG LOSS (3.1)|`0.96371`|
|SRGAN with VGG LOSS (3.1) NO ADVERSARIAL|`0.96360`|
|SRGAN with MSE loss|`0.95963`|
|Bicubic interpolation|`0.93559`|

You can reproduce results using `recognition_test.ipynb`
