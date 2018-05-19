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
|SRGAN with Light CNN 9 (MFM4) NO ADVERSARIAL|`0.96832`|
|SRGAN with Light CNN 9 (MFM4)|`0.96742`|
|SRGAN with Light CNN 9 (FC) NO ADVERSARIAL|`0.96594`|
|SRGAN with LIGHT CNN 9 (MFM4) NO ADVERSARIAL NO IMAGE|`0.96421`|
|SRGAN with VGG (3.1)|`0.96349`|
|SRGAN with VGG (3.1) NO ADVERSARIAL|`0.96346`|
|SRGAN with MSE|`0.95951`|
|Bicubic interpolation|`0.93559`|

You can reproduce results using `recognition_test.ipynb`
