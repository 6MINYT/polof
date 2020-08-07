import datetime
import os
import zipfile
import sys
import PyPDF2

extension = ".zip"

#try:
#	os.mkdir("D://PDFtemp")
#except Exception:
#
#try:
#	os.mkdir("D://ZIPPDF")
#except Exception:

os.chdir("D:\\ZIPPDF")
print(os.listdir())
with zipfile.ZipFile("1.zip","r") as zip_ref:
	zip_ref.extractall("D:\\PDFtemp")
#os.chdir("D:\\ZIPPDF")
#for item in os.listdir("D:\\ZIPPDF"): # loop through items in dir
#	if item.endswith(extension): # check for ".zip" extension
#		file_name = os.path.abspath(item) # get full path of files
#		zip_ref = zipfile.ZipFile(file_name) # create zipfile object
#		zip_ref.extractall("D:\\ZIPPDF") # extract file to dir
#		zip_ref.close() # close file
#		os.remove(file_name) # delete zipped file

#-----------------------

#file_name = dir_name + "/" + item

