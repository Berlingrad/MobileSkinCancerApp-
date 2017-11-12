import os, sys, glob
from PIL import Image

size = (299, 299)
filetypes = ['*.jpg', '*.jpeg']
print(os.path)

def resize(infile):
    outfile =  infile.split(".")[0] + "_resized.jpg"
    print(outfile)
    if infile != outfile:

            im = Image.open(infile)

            im.thumbnail(size, Image.ANTIALIAS)
            old_im_size = im.size

            ## By default, black colour would be used as the background for padding!
            new_im = Image.new("RGB", size)

            new_im.paste(im, ((size[0] - old_im_size[0]) / 2,
                              (size[1] - old_im_size[1]) / 2))

            new_im.save( outfile, "JPEG")

            os.remove(infile)

for filename in glob.iglob \
    ("/home/sam/workspace/pycharm/Transfer-Learning-for-Animal-Classification-in-Tensorflow-master/TrainingImages/mole/*jpg"):
    resize(filename)

