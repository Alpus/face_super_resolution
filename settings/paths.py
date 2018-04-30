import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))


DATA_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '../data'))


DATASETS_DIR = os.path.join(DATA_DIR, 'datasets')

MS_CELEB_DIR = os.path.join(DATASETS_DIR, 'ms_celeb')
FACES_DATA = os.path.join(MS_CELEB_DIR, 'FaceImageCroppedWithAlignment.tsv')
MS_CELEB_CLEAN_LIST = os.path.join(MS_CELEB_DIR, 'MS-Celeb-1M_clean_list.txt')
UNFILTERED_MS_CELEB_IMAGES_DIR = os.path.join(MS_CELEB_DIR, 'unfiltered_ms_celeb_images')
FILTERED_MS_CELEB_IMAGES_DIR = os.path.join(MS_CELEB_DIR, 'filtered_ms_celeb_images')

LFW_DIR = os.path.join(DATASETS_DIR, 'lfw')
LFW_FUNNELED_DIR = os.path.join(LFW_DIR, 'lfw_funneled')
LFW_PAIRS_6000 = os.path.join(LFW_FUNNELED_DIR, 'pairs.txt')


ANALYSIS_DIR = os.path.join(DATA_DIR, 'analysis')
ROC_AUC_DIR = os.path.join(ANALYSIS_DIR, 'roc_auc')


WEIGHTS_DIR = os.path.join(DATA_DIR, 'weights')

LIGHT_CNN_WEIGHTS_DIR = os.path.join(WEIGHTS_DIR, 'light_cnn')
LIGHT_CNN_9_WEIGHT = os.path.join(LIGHT_CNN_WEIGHTS_DIR, 'LightCNN_9Layers_checkpoint.pth.tar')

SRGAN_WEIGHTS_DIR = os.path.join(WEIGHTS_DIR, 'srgan')

SRGAN_MSE_LOSS_WEIGHTS_DIR = os.path.join(SRGAN_WEIGHTS_DIR, 'mse_loss')
SRGAN_MSE_LOSS_BEST_WEIGHT = os.path.join(SRGAN_MSE_LOSS_WEIGHTS_DIR, '0000601682.pth')

SRGAN_VGG_LOSS_3_1_WEIGHTS_DIR = os.path.join(SRGAN_WEIGHTS_DIR, 'vgg_loss_3.1')
SRGAN_VGG_LOSS_3_1_GENERATOR_WEIGHTS_DIR = os.path.join(SRGAN_VGG_LOSS_3_1_WEIGHTS_DIR, 'generator')
SRGAN_VGG_LOSS_3_1_DISCRIMINATOR_WEIGHTS_DIR = os.path.join(SRGAN_VGG_LOSS_3_1_WEIGHTS_DIR, 'discriminator')

SRGAN_VGG_LOSS_3_1_NO_ADVERSARIAL_WEIGHTS_DIR = os.path.join(SRGAN_WEIGHTS_DIR, 'vgg_loss_3.1_no_adversarial')

SRGAN_LIGHT_CNN_9_LOSS_MFM4_WEIGHTS_DIR = os.path.join(SRGAN_WEIGHTS_DIR, 'light_cnn_9_loss_mfm4')
SRGAN_LIGHT_CNN_9_LOSS_MFM4_GENERATOR_WEIGHTS_DIR = os.path.join(SRGAN_LIGHT_CNN_9_LOSS_MFM4_WEIGHTS_DIR, 'generator')
SRGAN_LIGHT_CNN_9_LOSS_MFM4_DISCRIMINATOR_WEIGHTS_DIR = os.path.join(SRGAN_LIGHT_CNN_9_LOSS_MFM4_WEIGHTS_DIR, 'discriminator')

SRGAN_LIGHT_CNN_9_LOSS_MFM4_NO_ADVERSARIAL_WEIGHTS_DIR = os.path.join(SRGAN_WEIGHTS_DIR, 'light_cnn_9_loss_mfm4_no_adversarial')


LOGS_DIR = os.path.join(DATA_DIR, 'logs')

ERRORS_LOGS_DIR = os.path.join(LOGS_DIR, 'errors')

SRGAN_LOGS_DIR = os.path.join(LOGS_DIR, 'srgan')

SRGAN_MSE_LOSS_LOGS_DIR = os.path.join(SRGAN_LOGS_DIR, 'mse_loss')
SRGAN_VGG_LOSS_3_1_LOGS_DIR = os.path.join(SRGAN_LOGS_DIR, 'vgg_loss_3.1')
SRGAN_VGG_LOSS_3_1_NO_ADVERSARIAL_LOGS_DIR = os.path.join(SRGAN_LOGS_DIR, 'vgg_loss_3.1_no_adversarial')
SRGAN_LIGHT_CNN_9_LOSS_MFM4_LOGS_DIR = os.path.join(SRGAN_LOGS_DIR, 'light_cnn_9_loss_mfm4')
SRGAN_LIGHT_CNN_9_LOSS_MFM4_NO_ADVERSARIAL_LOGS_DIR = os.path.join(SRGAN_LOGS_DIR, 'light_cnn_9_loss_mfm4_no_adversarial')
