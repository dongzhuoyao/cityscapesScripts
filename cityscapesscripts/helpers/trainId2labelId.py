import os
import cv2
import glob
import labels
trainId_result_dir = "/Users/ht/Documents/dataset/cityscapes/refinenet_cityscapes_test_result_png"
labelId_result_dir = "/Users/ht/Documents/dataset/cityscapes/refinenet_cityscapes_test_result_png_labelid"

if not os.path.exists(labelId_result_dir):
    print("dst_dir not exist,mkdir..")
    os.makedirs(labelId_result_dir)

searchFine = os.path.join(trainId_result_dir, "*.png")
filesFine = glob.glob(searchFine)

for f in filesFine:
    print(f)
    img = cv2.imread(f,0)
    name = f.rsplit("/",1)[1]
    (row,col) = img.shape
    for i in range(row):
        for j in range(col):
            img[i,j] = labels.trainId2label[img[i,j]].id

    cv2.imwrite(os.path.join(labelId_result_dir,name),img)