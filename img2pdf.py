#script to convert images to pdf :)
from PIL import Image

n = 1 #number of images, must be at least one
extension = '.jpg' #file extension of images
fileout = 'output.pdf' #file name

im_1 = Image.open(r'1'+extension).convert('RGB')
image_list = []

if (n>1):
    for i in range(2,n+1):
        image_list.append(Image.open(mode='r',fp=str(i)+extension).convert('RGB'))

im_1.save(mode='r',fp=fileout,save_all=True, append_images=image_list) #file output