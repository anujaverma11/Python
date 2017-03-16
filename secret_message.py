import os

def rename_files() :
  file_list = os.listdir("/Users/anujaverma/Desktop/Nanodegree/NanoDegree/resources/prank")
  print (file_list)
  saved_path= os.getcwd() #get current working directory
  os.chdir("/Users/anujaverma/Desktop/Nanodegree/NanoDegree/resources/prank")
  for file_name in file_list:
      print("Old Name - " + file_name)
      print("new Name - " + file_name.translate(None,"0123456789"))
      os.rename(file_name, file_name.translate(None,"0123456789"))

rename_files()