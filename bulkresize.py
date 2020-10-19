from PIL import Image
import os, sys
from time import perf_counter
from collections import namedtuple
import argparse 

def resize(path,**kwargs):
    '''
    This function takes the parameters and based on the given parameter calls the respective Function
    bulk resize given the percentage 
    bulk resize given the width
    bulk resize given the height
    bulk crop given the percentage
    bulk resize given the pixel
    '''
    #os.chdir(path)
    for item in os.listdir(path):
        if os.path.isfile(item):
            im = Image.open(item)
            width, height = im.size
            if 'percent' in kwargs and bool(kwargs['percent']):
                width  = int(width  * (kwargs['percent']/100))
                height = int(height * (kwargs['percent']/100))
            elif 'width' in kwargs:
                ratio = kwargs['width']/ width
                width  = kwargs['width']
                height = ratio * height
            elif 'height' in kwargs:
                ratio = kwargs['height']/ height
                height = kwargs['height']  
                width = ratio* width
            f, _ = os.path.splitext(item)
            imResize = im.resize((width,height), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

if __name__ == '__main__':

    '''
    This is the Section which runs while this module is called independently
    This demonstrates how the user can pass the arguments from the commandline of the python and the module 
    behaves based on the given argument
    argument d  to take the directory path from the user
    argument p  to take the resize or crop percentage from the user
    argument w  to take the width value from the user
    argument ht to take the height value from the user
    '''    
    # get code, repeats from arguments
    parser = argparse.ArgumentParser(description=__doc__)

    
    parser.add_argument('-d', '--dir',
                        type=str,
                        help='Name of the Directory containing file.')
    
    parser.add_argument('-p', '--percent',
                        type=int,
                        help='Percentage to resize or crop of original image.')
    
    parser.add_argument('-w', '--width',
                        type=int,
                        help='Width to resize.')

    parser.add_argument('-ht', '--height',
                        type=int,
                        help='height to resize.')

    args = parser.parse_args()

#    print(f'timing: {args.code}...')
    resize(path=args.dir, percent=args.percent, width=args.width, height=args.height)
