import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '../data'))

MS_CELEB_DIR = os.path.join(DATA_DIR, 'ms_celeb')
FACES_DATA = os.path.join(MS_CELEB_DIR, 'FaceImageCroppedWithAlignment.tsv')
MS_CELEB_CLEAN_LIST = os.path.join(MS_CELEB_DIR, 'MS-Celeb-1M_clean_list.txt')
UNFILTERED_MS_CELEB_IMAGES_DIR = os.path.join(MS_CELEB_DIR, 'unfiltered_ms_celeb_images')
FILTERED_MS_CELEB_IMAGES_DIR = os.path.join(MS_CELEB_DIR, 'filtered_ms_celeb_images')

LFW_DIR = os.path.join(DATA_DIR, 'lfw')
LFW_FUNNELED_DIR = os.path.join(LFW_DIR, 'lfw_funneled')
LFW_PAIRS_6000 = os.path.join(LFW_DIR, 'pairs.txt')
