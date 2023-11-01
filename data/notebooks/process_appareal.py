import face_recognition
import cv2
import os
from tqdm import tqdm
from multiprocessing import Process
import matplotlib.pyplot as plt
from IPython.display import Image, display

from concurrent.futures import ThreadPoolExecutor

dir_path = "../raw/appa-real-release"
new_dir_path = "../processed/appa-real"
NUM_PROCESSES = 16

all_imgs = os.listdir(dir_path)
nr_imgs = len(all_imgs)

if not(os.path.exists(new_dir_path) and os.path.isdir(new_dir_path)):
    os.mkdir(new_dir_path)

def save_imgs(thread_idx, nr_imgs, all_imgs, dir_path, new_dir_path):
    lower_bound = (thread_idx * (nr_imgs // NUM_PROCESSES))
    if thread_idx == 7:
        upper_bound = len(all_imgs)
    else:
        upper_bound = ((thread_idx+1) * (nr_imgs // NUM_PROCESSES))
    for i in range(lower_bound, upper_bound):
        img_path = all_imgs[i]
        loaded_img = face_recognition.load_image_file(f"{dir_path}/{img_path}")
        face_locations = face_recognition.face_locations(loaded_img)
        try:
            top, right, bottom, left = face_locations[0]
        except:
            continue

        face = loaded_img[top:bottom, left:right]

        if(face.shape[0] > 128):
            face = cv2.resize(face, (128, 128), interpolation=cv2.INTER_AREA)
        else:
            face = cv2.resize(face, (128, 128), interpolation=cv2.INTER_CUBIC)
        
        cv2.imwrite(f"{new_dir_path}/{img_path}", cv2.cvtColor(face, cv2.COLOR_RGB2BGR))

if __name__ == "__main__":
    # Create and start processes
    processes = []
    for i in range(NUM_PROCESSES):
        print(f"Creating process {i+1}")
        p = Process(target=save_imgs, args=(i, nr_imgs, all_imgs, dir_path, new_dir_path))
        processes.append(p)

    # Wait for all processes to finish
    for i in range(NUM_PROCESSES):
        print(f"Starting process {i+1}")
        processes[i].start()

    # for i in range(NUM_PROCESSES):
    #     print(f"Joining process {i+1}")
    #     processes[i].join()

