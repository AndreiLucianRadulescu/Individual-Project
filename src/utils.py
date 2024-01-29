import json
from sklearn.model_selection import StratifiedShuffleSplit
from skimage import color, io
from skimage.feature import hog
all_images_path = '../data/processed/all_images/'

def get_class_dict(filename):
    with open(filename, "r") as f:
        class_dict = json.load(f)
    
    return class_dict

def get_class(age, class_dict):
    for label, age_interval in class_dict.items():
        if age >= age_interval[0] and age <= age_interval[1]:
            return label

    return -1

def compute_hog(filename):
    rgb_image = io.imread(f"{all_images_path}/{filename}") / 255.0
    gray_image = color.rgb2gray(rgb_image)
    hog_feature, _ = hog(gray_image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True)
    
    return hog_feature
