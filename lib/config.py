import os

DATASET_ROOT = "dataset"
TRAIN_ROOT = os.path.join(DATASET_ROOT, "train")
VALID_ROOT = os.path.join(DATASET_ROOT, "valid")
TEST_ROOT = os.path.join(DATASET_ROOT, "test")

TRAIN_FRAMES_ROOT = os.path.join(DATASET_ROOT, "train_frames")
VALID_FRAMES_ROOT = os.path.join(DATASET_ROOT, "valid_frames")
TEST_FRAMES_ROOT = os.path.join(DATASET_ROOT, "test_frames")

TRAIN_SOUND_ROOT = os.path.join(DATASET_ROOT, "train_sound")
VALID_SOUND_ROOT = os.path.join(DATASET_ROOT, "valid_sound")
TEST_SOUND_ROOT = os.path.join(DATASET_ROOT, "test_sound")

RESOURCES_ROOT = "resources400"

CATEGORIES_PATH = os.path.join(RESOURCES_ROOT, "categories.json")
CLASSES_PATH = os.path.join(RESOURCES_ROOT, "classes700.json")
TRAIN_METADATA_PATH = os.path.join(RESOURCES_ROOT, "kinetics_train.json")
VAL_METADATA_PATH = os.path.join(RESOURCES_ROOT, "kinetics_val.json")
TEST_METADATA_PATH = os.path.join(RESOURCES_ROOT, "kinetics_test.json")
