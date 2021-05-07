import fast_colorthief
import numpy as np
import cv2
#import colorthief
from PIL import Image, ImageDraw
import PIL
import time


def test_some_output_returned(img_cv,mask):
    
    image = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    # image = Image.fromarray(image)
  
    
    # image = image.convert('RGBA')
    # t1=time.time()
    
    image = np.array(image).astype(np.uint8)
    print("time convert ",time.time()-t1)
   
    # image[:,:,3]=mask
    
    # print(mask.shape)
    # t1=time.time()
    # for i in range(img_cv.shape[0]):
    #     for j in range(img_cv.shape[1]):
    #         if(mask[i][j]==0):
    #             image[i][j][3]=10
    # print("time convert ",time.time()-t1)
   

    
    rast_palette = fast_colorthief.get_palette(image ,mask,3, 10)
    
    
    print(rast_palette)


def test_same_output():
    image_path = 'tests/veverka_lidl.jpg'

    fast_palette = fast_colorthief.get_palette(image_path, 5, 10)
    colorthief_orig = colorthief.ColorThief(image_path)
    original_palette = colorthief_orig.get_palette(5, 10)
    assert (fast_palette == original_palette)


def print_speed():
    image = cv2.imread('veverka_lidl.jpg')
    image = PIL.Image.open('veverka_lidl.jpg')
    image = image.convert('RGBA')
    image = np.array(image).astype(np.uint8)
    print(image[0][0])

    iterations = 10

    start = time.time()

    for i in range(iterations):
        fast_colorthief.get_palette(image)



if __name__ == '__main__':
    img=cv2.imread("b.png")
    polygon=[(14, 2), (214, 14), (222, 356), (13, 360), (11, 3)]
    height,width=img.shape[:2]
    bg = Image.new('L', (width,height), 0)
    ImageDraw.Draw(bg).polygon(polygon, outline=1, fill=255)
    mask = np.array(bg)
   
    for i in range(3):
        t1=time.time()
        test_some_output_returned(img,mask)
        print(time.time()-t1)
