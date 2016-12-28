from PIL import Image
import os, glob, sys

# Where to look for Cityscapes
if 'CITYSCAPES_DATASET' in os.environ:
        cityscapesPath = os.environ['CITYSCAPES_DATASET']
else:
        cityscapesPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','..')

leftimagePath = "/Users/ht/Documents/database/leftImg8bit_trainvaltest/leftImg8bit/"

searchFine = os.path.join(cityscapesPath, "gtFine", "*", "*", "*_gt*_labelTrainIds.png")
filesFine = glob.glob(searchFine)
f_train = open(os.path.join(cityscapesPath,"train.txt"),"w")
f_test = open(os.path.join(cityscapesPath,"test.txt"),"w")
f_val = open(os.path.join(cityscapesPath,"val.txt"),"w")


for f in filesFine:
    print(f)
    tmp = f.split("/gtFine/")
    tmp2 = f.split("/")
    post_f = tmp[1]

    phase = tmp2[-3]
    name = tmp2[-1]

    label_path = os.path.join(cityscapesPath,phase+"_anno/",name)
    img_label = Image.open(f)
    img_label = img_label.resize((500, 250), Image.NEAREST)
    img_label.save(label_path)

    tmp3 = name.rsplit("_",2)
    img_path = leftimagePath+phase+"/"+tmp2[-2]+"/"+tmp3[0]+"_leftImg8bit.png"
    img = Image.open(img_path)
    img = img.resize((500,250),Image.NEAREST)
    final_img_path = os.path.join(cityscapesPath,phase,tmp3[0]+"_leftImg8bit.png")
    img.save(final_img_path)

    write_line = final_img_path+" "+label_path+"\n"
    if phase=="train":
        f_train.write(write_line)
        f_train.flush()
    elif phase=="test":
        f_test.write(write_line)
        f_test.flush()
    elif phase=="val":
        f_val.write(write_line)
        f_val.flush()
    else:
        print("invalid phase name..")
        sys.exit(-1)


f_train.close()
f_test.close()
f_val.close()