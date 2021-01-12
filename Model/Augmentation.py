import tensorflow as tf
import numpy as np
IMG_HEIGHT=720
IMG_WIDTH=1024
# Note - these functions take tensors as argumnets not numpy

def random_crop(blur,target):
    stacked_image = tf.stack([blur, target], axis=0)
    cropped_image = tf.image.random_crop( stacked_image, size=[2, IMG_HEIGHT, IMG_WIDTH, 3] )
    return cropped_image[0], cropped_image[1]

def flip(blur,target):
    return tf.image.flip_left_right(blur),tf.image.flip_left_right(target)

def normalize(blur, target):
    blur = (blur / 127.5) - 1
    target = (target / 127.5) - 1
    return blur, target

@tf.function()
def random_jitter(blur, target):
    blur, target = random_crop(blur, target)
    if tf.random.uniform(()) > 0.5:
        blur = tf.image.flip_left_right(blur)
        target = tf.image.flip_left_right(target)
    return blur, target
 
