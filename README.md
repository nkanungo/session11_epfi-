allmodule
===========
def allmodule_func(*args,**kwargs):
   
    This function takes the parameters and based on the given parameter calls the respective Function
    j2p Calls the JPG to PNG Module
    p2j Calls the PNG to JPG Module
    res_p Calls the bulk resize given the percentage 
    res_w Calls the bulk resize given the width
    res_h Calls the bulk resize given the height
    crp_p Calls the bulk crop given the percentage
    crp_px Calls the bulk resize given the pixel

if __name__ == '__main__':

    
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
 
 bulkresize
 ===============
 def resize(path,**kwargs):
   
    This function takes the parameters and based on the given parameter calls the respective Function
    bulk resize given the percentage 
    bulk resize given the width
    bulk resize given the height
    
 if __name__ == '__main__':

  
    This is the Section which runs while this module is called independently
    This demonstrates how the user can pass the arguments from the commandline of the python and the module 
    behaves based on the given argument
    argument d  to take the directory path from the user
    argument p  to take the resize or crop percentage from the user
    argument w  to take the width value from the user
    argument ht to take the height value from the user
    
    
 bulkcrop
 ==========
 def bulkcrop(path,**kwargs):
   
    This function takes the parameters and based on the given parameter calls the respective Function
    crp_p Calls the bulk crop given the percentage
    crp_px Calls the bulk resize given the pixel

if __name__ == '__main__':

    This is the Section which runs while this module is called independently
    This demonstrates how the user can pass the arguments from the commandline of the python and the module 
    behaves based on the given argument
    argument d  to take the directory path from the user
    argument p  to take the resize or crop percentage from the user
    argument l  to take the pixel from the user
    
    
jpg2png
==========
def jpg2png_func(dir,img):
   
   Takes input as a JPG image and converts into PNG
   
if __name__ == '__main__':
  
    This is the Section which runs while this module is called independently
    This demonstrates how the user can pass the arguments from the commandline of the python and the module 
    behaves based on the given argument
    argument d  to take the directory path from the user
    argument f  to take the file name from the user
    
png2jpg
=========
def png2jpg_func(dir,img):
    
   Takes input as a PNG image and converts into JPG

if __name__ == '__main__':

    This is the Section which runs while this module is called independently
    This demonstrates how the user can pass the arguments from the commandline of the python and the module 
    behaves based on the given argument
    argument d  to take the directory path from the user
    argument f  to take the file name from the user
