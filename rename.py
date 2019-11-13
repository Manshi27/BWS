import csv
import os
import cv2
import numpy as np
count = 1
for path, subdirnames, filenames in os.walk("trainingImages"):
    for filename in filenames:
        if filename.startswith("."):
            print("Skipping File:", filename)  # Skipping files that startwith .
            continue
        img_path = os.path.join(path, filename)  # fetching image path
        print("img_path", img_path)
        img = cv2.imread(img_path)
        if img is None:
            print("Image not loaded properly")
            continue
        # image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # resized_image = cv2.resize(image, (28, 28))
        # print(resized_image.shape)
        # result = np.array(resized_image).flatten()
        # print(result)
        new_path = "renamed"
        print("Desired path is",os.path.join(new_path, "%d.jpg" % count))
        cv2.imwrite(os.path.join(new_path, "%d.jpg" % count), img)
        count += 1


