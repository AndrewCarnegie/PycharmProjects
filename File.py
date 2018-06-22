import os

def read_file(file_path):
    with open(file_path, 'r', encoding='UTF-8',errors='ignore' ) as f:
      return f.read()
      
      
fpath = 'C:\\D Disk\\New Text Document.txt'
print read_file(fpath)
        
        