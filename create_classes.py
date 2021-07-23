import json

from lib.config import TRAIN_METADATA_PATH, VAL_METADATA_PATH


def get_classes():
    with open(TRAIN_METADATA_PATH, 'r') as fp:
        train = json.load(fp)

    with open(VAL_METADATA_PATH, 'r') as fp:
        val = json.load(fp)

    classes = [vid['annotations']['label'] for _, vid in train.items()]
    classes += [vid['annotations']['label'] for _, vid in val.items()]
    classes = list(set(classes))
    return classes


if __name__ == '__main__':
    print(len(get_classes()))


    print()
    for c in get_classes():
        print(c)