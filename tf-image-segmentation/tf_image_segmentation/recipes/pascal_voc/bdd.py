
import os
from tf_records import write_image_annotation_pairs_to_tfrecord

def get_pair(mode="train"):

    TRAIN_FILE_LIST = "train.txt"
    VAL_FILE_LIST = "val.txt"
    TEST_FILE_LIST = "test.txt"

    IMAGE_FILE_EXTENSION = ".jpg"
    LABEL_FILE_EXTENSION = ".png"

    IMAGE = "raw_images"
    LABEL = "class_color"

    ROOT = "/media/keti-ai/AI_HARD3/DataSets/BDD/segmentation/"
    TRAIN_PATH = "/media/keti-ai/AI_HARD3/DataSets/BDD/segmentation/train/"
    VAL_PATH = "/media/keti-ai/AI_HARD3/DataSets/BDD/segmentation/val/"
    TEST_PATH = "/media/keti-ai/AI_HARD3/DataSets/BDD/segmentation/test/"

    result = []

    if mode == "train":

        with(open(os.path.join(ROOT, TRAIN_FILE_LIST), "r")) as f:

            for line in f.readlines():

                line = line.rstrip()
                result.append((unicode(os.path.join(TRAIN_PATH, IMAGE, "".join([line, IMAGE_FILE_EXTENSION]))),
                              unicode(os.path.join(TRAIN_PATH, LABEL, "".join([line, LABEL_FILE_EXTENSION])))))

    if mode == "val":
        with(open(os.path.join(ROOT, VAL_FILE_LIST), "r")) as f:

            for line in f.readlines():
                line = line.rstrip()
                result.append((unicode(os.path.join(VAL_PATH, IMAGE, "".join([line, IMAGE_FILE_EXTENSION]))),
                               unicode(os.path.join(VAL_PATH, LABEL, "".join([line, LABEL_FILE_EXTENSION])))))

    if mode == "test":
        with(open(os.path.join(ROOT, VAL_FILE_LIST), "r")) as f:

            for line in f.readlines():
                line = line.rstrip()
                result.append((unicode(os.path.join(TEST_PATH, IMAGE, "".join([line, IMAGE_FILE_EXTENSION]))),
                               unicode(os.path.join(TEST_PATH, LABEL, "".join([line, LABEL_FILE_EXTENSION])))))

    return result

train_data = get_pair(mode="train")
train_filename ="BDD_train.tfrecords"

write_image_annotation_pairs_to_tfrecord(
    filename_pairs=train_data,
    tfrecords_filename=train_filename
)

val_data = get_pair(mode="val")
val_filename ="BDD_val.tfrecords"

write_image_annotation_pairs_to_tfrecord(
    filename_pairs=train_data,
    tfrecords_filename=val_filename
)

