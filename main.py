from PIL import Image
import fast_colorthief_backend
import numpy as np
import version
import cv2
from PIL import Image, ImageDraw
import colorsys

__version__ = version.__version__



class Color_object:
    """Build a color palette.  We are using the modified median cut algorithm to cluster similar colors.
    :param color_count: number of colors in the palette
    :param quality: quality settings, 1 is the highest quality, the bigger
                    the number, the faster the palette generation, but the
                    greater the likelihood that colors will be missed.
    :return list: a list of tuple in the form (r, g, b)
    """
    def __init__(self,color_count=5,quality=10):
        self.color_count = color_count
        self.quality = quality
    
    def get_color(self,image,mask=None,output="hsl"):#image cv2 ,output ="rgb"/"hex","int"
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = np.array(image).astype(np.uint8)
        if(mask is None):
            results=fast_colorthief_backend.get_palette(image,self.color_count, self.quality)
        else:
            results=fast_colorthief_backend.get_palette_mask(image, mask,self.color_count, self.quality)
        if(output=="hex"):
            
            results=['#%02x%02x%02x' % x for x in results]
        elif(output=="int"):
            results=[int('0x%02x%02x%02x' % x,0) for x in results]
        elif(output=="hsl"):
            results=[colorsys.rgb_to_hls(x[0]/255.0,x[1]/255.0,x[2]/255) for x in results]
            results=[(int(x[0]*360),int(x[1]*100),int(x[2]*100)) for x in results]
        return results

if __name__=="__main__":
    cl_object= Color_object()
    img=cv2.imread("images/2.png")
    polygon=[(22, 123), (127, 73), (229, 121), (227, 152), (198, 191), (105, 196), (74, 197), (46, 176), (26, 148), (20, 126)]
    height,width=img.shape[:2]
    bg = Image.new('L', (width,height), 0)
    ImageDraw.Draw(bg).polygon(polygon, outline=1, fill=255)
    mask = np.array(bg)
    res=cl_object.get_color(img,mask,"hsl")
    print(res)

    

#9873577
#7908818

