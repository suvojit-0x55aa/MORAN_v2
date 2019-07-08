import charset
import os
from create_dataset import createDataset


def get_image_filenames(image_list_filename):
    """ Given input file, generate a list of relative filenames"""
    filenames = []
    with open(image_list_filename) as f:
        for line in f:
            # Carve out the ground truth string and file path from lines like:
            # ./2697/6/466_MONIKER_49537.jpg 49537
            filename = line.split(' ', 1)[0][2:]  # split off "./" and number
            filenames.append(filename)
    return filenames


def get_text_and_labels(filename):
    """ 
    Extract the human-readable text and label sequence from image filename
    """
    # Ground truth string lines embedded within base
    # filename between underscores
    # 2697/6/466_MONIKER_49537.jpg --> MONIKER
    text = os.path.basename(filename).split('_', 2)[1]

    # Transform string text to sequence of indices using charset, e.g.,
    # MONIKER -> [12, 14, 13, 8, 10, 4, 17]
    labels = charset.string_to_label(text)

    return text, labels


# Minimum allowable width of image after CNN processing
# min_width = 20

# def is_writable(image_width, text):
#     """Determine whether the CNN-processed image is longer than the string"""
#     return (image_width > min_width) and (len(text) <= seq_lens[image_width])


def gen_data(input_base_dir, image_list_filename, output_filebase):
    image_filenames = get_image_filenames(
        os.path.join(input_base_dir, image_list_filename))
    label_list = []
    image_list = []
    for filename in image_filenames:
        path_filename = os.path.join(input_base_dir, filename)
        if os.stat(path_filename).st_size == 0:
            print('SKIPPING', filename)
            continue
        text, labels = get_text_and_labels(filename)
        image_list.append(path_filename)
        label_list.append(text)
        # if not is_writable(width, text):
        #     print('SKIPPING', filename)
        #     continue
    output_dir = os.path.basename(output_filebase)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    createDataset(output_filebase, image_list, label_list)


def main(argv=None):
    gen_data('../data/images', 'annotation_train.txt',
             '../data/train')
    gen_data('../data/images', 'annotation_val.txt', '../data/val')
    gen_data('../data/images', 'annotation_test.txt', '../data/test')


if __name__ == '__main__':
    main()