# timing.py

"""
Times how long a snipped of code takes to run
over multiple iterations
"""

from time import perf_counter
from collections import namedtuple
import argparse 

print(f'loading allmodule.py: __name__ = {__name__}')

Timing = namedtuple('Timing', 'repeats clapsed average')

def allmodule_func(*args,**kwargs):
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
