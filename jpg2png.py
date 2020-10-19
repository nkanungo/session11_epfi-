from PIL import Image
import os
from time import perf_counter
from collections import namedtuple
import argparse 

def jpg2png_func(dir,img):
   '''
   Takes input as a JPG image and converts into PNG
   '''
   print('Executing JPG to PNG Module') 
   print("======",dir)
   os.chdir(dir)
   print("-------------",os.curdir)
   im = Image.open(dir+ '\\' +  img + '.jpg')
   im.save(dir+ '\\' + img + '.png')

if __name__ == '__main__':
   '''
    This is the Section which runs while this module is called independently
    This demonstrates how the user can pass the arguments from the commandline of the python and the module 
    behaves based on the given argument
    argument d  to take the directory path from the user
    argument f  to take the file name from the user
    '''

   parser = argparse.ArgumentParser(description=__doc__)
   parser.add_argument('-d', '--dir',
                        type=str,
                        help='Name of the Directory containing file.')
    
   parser.add_argument('-f', '--fil',
                       type=str,
                       help='Name of the file which needs to be converted.')

   args = parser.parse_args() 
   jpg2png_func(dir=args.dir, img=args.fil)
