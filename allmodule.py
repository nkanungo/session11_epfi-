# timing.py

"""
# Author Nihar Kanungo
"""

from time import perf_counter
from collections import namedtuple
import argparse

print(f'loading allmodule.py: __name__ = {__name__}')

Timing = namedtuple('Timing', 'repeats clapsed average')

def allmodule_func(*args,**kwargs):
    '''
    This function takes the parameters and based on the given parameter calls the respective Function
    j2p Calls the JPG to PNG Module
    p2j Calls the PNG to JPG Module
    res_p Calls the bulk resize given the percentage 
    res_w Calls the bulk resize given the width
    res_h Calls the bulk resize given the height
    crp_p Calls the bulk crop given the percentage
    crp_px Calls the bulk resize given the pixel
    '''
    print('Getting into all Module Function', kwargs)
    if kwargs['opt'] == 'j2p':
        import jpg2png as j2p
        j2p.jpg2png_func(kwargs['dir'],kwargs['fil'])
    elif kwargs['opt'] == 'p2j':
        import png2jpg as p2j
        p2j.png2jpg_func(kwargs['dir'],kwargs['fil'])
    elif kwargs['opt']== 'res_p':
        import bulkresize as br
        br.resize(kwargs['dir'], percent=kwargs['percent'])
    elif kwargs['opt']== 'res_w':
        import bulkresize as br
        br.resize(kwargs['dir'], percent=kwargs['width'])
    elif kwargs['opt']== 'res_h':
        import bulkresize as br
        br.resize(kwargs['dir'], percent=kwargs['height'])
    elif kwargs['opt'] == 'crp_px':
        import bulkcrop as bc
        len_val= kwargs['length'].split(',')
        bc.bulkcrop(kwargs['dir'], image_width=int(len_val[0]),image_height=int(len_val[1]))
    elif kwargs['opt'] == 'crp_p':
        import bulkcrop as bc
        bc.bulkcrop(kwargs['dir'],percent=kwargs['percent'])
    return 'Processing Completed , Please check the directory'

if __name__ == '__main__':

    '''
    This is the Section which runs while this module is called independently
    This demonstrates how the user can pass the arguments from the commandline of the python and the module 
    behaves based on the given argument
    argument o  to take the option argument from the user
    argument d  to take the directory path from the user
    argument f  to take the file name from the user
    argument p  to take the resize or crop percentage from the user
    argument w  to take the width value from the user
    argument ht to take the height value from the user
    argument l  to take the pixel from the user

    '''    
    print('running this command line code')

    # get code, repeats from arguments
    parser = argparse.ArgumentParser(description=__doc__)

    # parser.add_argument('code',
    #                     type=str,
    #                     help='The Python code snippet to time.')
    parser.add_argument('-o', '--opt',
                        type=str,
                        help='Operation to perform.')

    parser.add_argument('-d', '--dir',
                        type=str,
                        help='Name of the Directory containing file.')

    parser.add_argument('-f', '--fil',
                        type=str,
                        help='Name of the file which needs to be converted.')

    parser.add_argument('-p', '--percent',
                        type=int,
                        help='Percentage to resize or crop of original image.')

    parser.add_argument('-w', '--width',
                        type=int,
                        help='Width to resize.')

    parser.add_argument('-ht', '--height',
                        type=int,
                        help='height to resize.')

    parser.add_argument('-l', '--length',
                        type=str,
                        help='coordinates to crop.')

    args = parser.parse_args()
    print(args.opt)
    print(args.dir)
    print(args.fil)

#    print(f'timing: {args.code}...')
    allmodule_func(opt=args.opt, dir=args.dir, fil=args.fil, percent=args.percent, width=args.width, height=args.height, length=args.length)
