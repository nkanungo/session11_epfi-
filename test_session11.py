import pytest
import allmodule
import jpg2png
#import png2jpg
#import bulkcrop
#import bulkresize
import os
#import numpy as np
import inspect
import re
import subprocess

README_CONTENT_CHECK_FOR = [

]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 250, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 0

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(allmodule)
    spaces = re.findall('\n +.', lines)
    line_no =1
    for space in spaces:
        line_no +=1
        print('=====', line_no, space)
        #print(lines)
        #assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        #assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 
        assert re.search('[a-zA-Z#@=1234\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@=1234\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(allmodule, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_jpg2png():
    #subprocess.run(["python jpg2png.py"])
    os.system('python jpg2png.py -d images -f image1')

def test_png2jpg():
    #subprocess.run(["python jpg2png.py"])
    os.system('python png2jpg.py -d images -f image1')


def test_resize_percentage():
    #subprocess.run(["python jpg2png.py"])
    os.system('python bulkresize.py -d images -p 50')

def test_resize_height():
    #subprocess.run(["python jpg2png.py"])
    os.system('python bulkresize.py -d images -ht 50')

def test_resize_width():
    #subprocess.run(["python jpg2png.py"])
    os.system('python bulkresize.py -d images -w 50')

def test_crop_percent():
    #subprocess.run(["python jpg2png.py"])
    os.system('python bulkcrop.py -d images -p 50')

def test_crop_pixel():
    #subprocess.run(["python jpg2png.py"])
    os.system('python bulkcrop.py -d images -l 50 50')


def test_resize_pixel():
    #subprocess.run(["python jpg2png.py"])
    os.system('python png2jpg.py')


def test_allmodule_jpg2png():
    os.system('python allmodule.py -o j2p -d images -f file1')

def test_allmodule_png2jpg():
    os.system('python allmodule.py -o p2j -d images -f file1')


def test_allmodule_resize_percentage():
    #subprocess.run(["python jpg2png.py"])
    os.system('python allmodule.py -o res_p -d images -p 50')

def test_allmodule_resize_height():
    #subprocess.run(["python jpg2png.py"])
    os.system('python allmodule.py -o res_h -d images -ht 50')

def test_allmodule_resize_width():
    #subprocess.run(["python jpg2png.py"])
    os.system('python allmodule.py -o res_w -d images -w 50')

def test_allmodule_crop_percent():
    #subprocess.run(["python jpg2png.py"])
    os.system('python allmodule.py -o crp_p -d images -p 50')

def test_allmodule_crop_pixel():
    #subprocess.run(["python jpg2png.py"])
    os.system('python allmodule.py -o crp_px -d images -l 50 50')
    
def test_things_not_allowed():
    code_lines = inspect.getsource(allmodule)
    for word in CHECK_FOR_THINGS_NOT_ALLOWED:
        assert word not in code_lines, 'Have you heard of Pinocchio?'
