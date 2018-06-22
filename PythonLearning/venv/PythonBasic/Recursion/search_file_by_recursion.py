'''
1.输入要查找的特定目标文件扩展名，来遍历查找特定扩展名的文件，eg:python find_file.py txt
2.通过-f指定将结果写入到特定名称的文件，eg：python -f txt_result txt,否则将结果打印在控制台
3.在指定要查找的特定扩展名文件后，指定查找的根目录，eg：python find_file.py txt /

'''

# import sys
import os
import argparse
# import pdb
from pprint import pprint

def find_path_of_file_by_suffix(specific_file_suffix,search_directory):
    """
    result_path_filename
    """
    result_path_filename = list()
    result_path_filename.extend(
        [os.path.join(dirpath,filename) \
         for dirpath,dirnames,filenames in os.walk(search_directory) \
         for filename in filenames if os.path.splitext(filename)[1] \
         == ('.' + specific_file_suffix)])
    pprint(result_path_filename)

# find_path_file('TXT','C:\\') #Unit test for function find_path_of_file_by_suffix

def find_file(specific_file_suffix,search_directory):
    """
    result_filename don't have path
    """
    result_filename = list()
    os.path.walk(search_directory,lambda arg,dirname,names:result_filename.extend([i for i in names if os.path.splitext(i)[1] == ('.' + specific_file_suffix)]),())
    pprint(result_filename)

# find_file('txt', 'C:\\') #Unit test for function find_path_of_file_by_suffix

def save_result_to_file(_filename,specific_file_suffix,search_directory):
    """
    save result to specific file
    """
    result_path_filename = list()
    result_path_filename.extend(
        [os.path.join(dirpath,filename) \
         for dirpath,dirnames,filenames in os.walk(search_directory) \
         for filename in filenames if os.path.splitext(filename)[1] \
         == ('.' + specific_file_suffix)])
    with open(_filename,'w') as f:
        f.write("\n".join(result_path_filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_suffix",help="specific the file suffix")
    parser.add_argument("rootdir",help="specific the root directory")
    parser.add_argument("-f","--file",help="record result to file")
    args = parser.parse_args()
    specific_file = args.file_suffix
    search_directory = args.rootdir
    if args.file:
        filename = args.file
        save_result_to_file(filename,specific_file,search_directory)
    else:
        #        find_file(specific_file,search_directory)
        find_path_of_file_by_suffix(specific_file,search_directory)