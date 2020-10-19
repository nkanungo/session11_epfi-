from PIL import Image
import os, sys
from time import perf_counter
from collections import namedtuple
import argparse 


def bulkcrop(path,**kwargs):
    '''
    This function takes the parameters and based on the given parameter calls the respective Function
    crp_p Calls the bulk crop given the percentage
    crp_px Calls the bulk resize given the pixel
    '''
    #os.chdir(path)
    list_image=[]
    #print('getting Inside this')
    for item in os.listdir(path):
     #   print('getting inside for ',item)
      #  print(os.path)
        if os.path.isfile(item):
       #     print('getting inside if ')
            im = Image.open(item)
            width, height = im.size
        #    print(width,height)
         #   print(kwargs)
          #  print('percent' in kwargs)
            if 'percent' in kwargs:
                #print('Cropping with user defined percentage')
                left = (width -width *(kwargs['percent']/100))/2
                top = (height-height *(kwargs['percent']/100))/2
                right = width-left
                bottom = height-top
                # Setting the points for cropped image 
#                 left = int(width/4)
#                 top = int(height  * (kwargs['percent']/100))
#                 right = int(width * 3/4)
#                 bottom = int(height  * (kwargs['percent']/100))
                
            elif 'image_width' in kwargs and 'image_height' in kwargs and kwargs['image_width']<=width and kwargs['image_height'] <=height:
                left = (width - kwargs['image_width'])/2
                top = (height - kwargs['image_height'])/2
                right = width-left
                bottom = height-top
            else:
                list_image.append(im)
                continue
            
            #raise ValueError('Looks like you have either not given all required fields or given size exceeds original image size')
                
            f, _ = os.path.splitext(item)
            imResize = im.crop((left, top, right, bottom)) 
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

if __name__ == '__main__':

    '''
    This is the Section which runs while this module is called independently
    This demonstrates how the user can pass the arguments from the commandline of the python and the module 
    behaves based on the given argument
    argument d  to take the directory path from the user
    argument p  to take the resize or crop percentage from the user
    argument l  to take the pixel from the user
    '''
    # get code, repeats from arguments
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-d', '--dir',
                        type=str,
                        help='Name of the Directory containing file.')

    parser.add_argument('-p', '--percent',
                        type=int,
                        help='Percentage to resize or crop of original image.')

    parser.add_argument('-l', '--length',
                        type=str,
                        help='coordinates to crop.')

    args = parser.parse_args()
    
#    print(f'timing: {args.code}...')
    bulkcrop(path=args.dir, percent=args.percent, length=args.length)

   