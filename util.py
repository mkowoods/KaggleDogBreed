import cv2
import preprocess
import os
import numpy as np

def read_image_as_rbg(img_id = None, shape = None):
    #img_id = '0a0c223352985ec154fd604d7ddceabd'
    img_BGR = cv2.imread(os.path.join(preprocess.DATA_DIR_PATH, 'train', f'{img_id}.jpg'))
    if shape is not None:
        img_BGR = cv2.resize(img_BGR, shape)
    return cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

def get_image_matrix_from_ids(list_of_ids, output_size = (200, 200)):
    img_matrix = np.zeros((len(list_of_ids), output_size[0], output_size[1], 3), dtype='float32') #stores all of the images in a 4 dim tensor
    for idx, img_id in enumerate(list_of_ids):
        img = read_image_as_rbg(img_id=img_id, shape=output_size)
        img_matrix[idx] = img
    return img_matrix

def decode_arr(input_arr, labels):
    """
    input_arr: vector of size 4
    """
    assert input_arr.shape == (4,), 'input wrong shape'
    return labels[input_arr.argmax()]

