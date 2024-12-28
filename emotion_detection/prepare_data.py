import os
import cv2
import numpy as np

from utils import get_face_landmarks

data_dir = './data'

output = []
for emotion_index, emotion in enumerate(sorted(os.listdir(data_dir))):
    for image_path_ in os.listdir(os.path.join(data_dir, emotion)):
        image_path = os.path.join(data_dir, emotion, image_path_)

        image = cv2.imread(image_path)

        face_landamarks = get_face_landmarks(image)

        # print(len(face_landamarks))
        if len(face_landamarks) == 1404:
            face_landamarks.append(int(emotion_index))
            output.append(face_landamarks)

np.savetxt('data.txt', np.asarray(output))
