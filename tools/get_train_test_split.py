import os
import random
from random import shuffle
from math import floor

random.seed(42)

train_split, val_split, test_split = 0.8, 0.1, 0.1
assert train_split + val_split + test_split == 1


def get_training_and_testing_sets(file_list, train_split, val_split,
                                  test_split):
    split_index_train = int(floor(len(file_list) * train_split))
    split_index_val = int(floor(len(file_list) * (train_split + val_split)))
    training = file_list[:split_index_train]
    validation = file_list[split_index_train:split_index_val]
    testing = file_list[split_index_val:]
    return {'train': training, 'val': validation, 'test': testing}


def get_file_list_from_dir(datadir):
    all_files = os.listdir(os.path.abspath(datadir))
    data_files = list(filter(lambda file: file.endswith('.jpg'), all_files))
    return data_files


def randomize_files(file_list):
    shuffle(file_list)


if __name__ == '__main__':
    DATA_DIR = '../data/IAMhand2printv5'
    file_list = get_file_list_from_dir(DATA_DIR)
    randomize_files(file_list)
    data_split = get_training_and_testing_sets(file_list, train_split,
                                               val_split, test_split)

    # Write to file
    for x_set_name, x_set in data_split.items():
        with open(os.path.join(DATA_DIR, x_set_name + '.txt'), 'w') as f:
            for item in x_set:
                f.write("{}\n".format(item))
