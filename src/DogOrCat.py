import cv2
import numpy as np
import sys
import os
from keras.models import load_model

dir = os.path.dirname(__file__)
root_dir = os.path.dirname(dir)
file_path = []

def get_path(path):

    if(os.path.exists(path)):
        pass
    else:
        exit ("The data doesn't exist, check your input please.")

    if(os.path.isfile(path)):
        file_path.append(path)
        return file_path


    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                file_path.append(os.path.join(root, file))

    return file_path


def load_data(path):

    data = []
    imagePaths = get_path(path)

    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        image = cv2.resize(image, (Width, Height))
        image = np.array(image).reshape(Width, Height, 3)
        data.append(image)
    data = np.array(data, dtype="float") / 255.0

    return data

def record_ans(ans):

    filename = root_dir+'/data/temp/anstemp'
    if(os.path.exists(filename)):
        os.remove(filename)

    os.mknod(filename)

    with open(filename, 'w') as f:
        j = 0
        for item in ans:
            if item[0] > item[1]:
                f.write(file_path[j] + "   cat");
                print(file_path[j] + "   cat")
                j += 1;
            else:
                f.write(file_path[j] + "   dog")
                print(file_path[j] + "   dog")
                j += 1;

def main(image_path):
    global Width, Height
    Width = 224
    Height = 224
    X_test = load_data(image_path)

    model = load_model(root_dir+'/model/DogOrCat/0.0.3/DogOrCat.model')
    ans = model.predict(X_test)

    record_ans(ans)

if __name__ == '__main__':
    for i in range(1, len(sys.argv)):
        url = sys.argv[i]
        main(url)