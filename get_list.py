
import os as system

def getList (list, extension, arg):
  file_path = system.getcwd() + f"\\lists\\{list}{extension}"
  fileExist = system.path.isfile(file_path)
  if fileExist:
    file = open(file_path, arg)
    return file
  else: 
    return False