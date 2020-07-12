import pdfid
import os
import sys
from pathlib import *
import pandas as pd
import string
from datetime import datetime
import glob

# print(glob.glob("C:\\Users\\hp\\Desktop\\PDF\\PDF MALWARE\\MALWARE_PDF_PRE_04-2011_10982_files\\*"))
# DP
fileDir = os.path.dirname(os.path.realpath('__file__'))
# filename = os.path.join(fileDir, 'frequencies.csv')
#dataset = pd.read_csv(filename, delim_whitespace=True)

matrix = list()
temp_list = list()
temp_list1 = list()

# Pathi ne PC
# dir_path = Path('C:\\Users\\hp\\Desktop\\PDF\\PDF TO SCAN\\Scan')
# dir_path = Path('C:\\Users\\hp\\Desktop\\PDF\\PDF TO SCAN\\CLEAN_PDF_9000_files')
# dir_path = Path('C:\\Users\\hp\\Desktop\\PDF\\PDF MALWARE\\MALWARE_PDF_PRE_04-2011_10982_files')
# pdf_files = list(dir_path.glob('*.pdf'))

# pdf_files = list(dir_path.glob('*'))
# index = 0
# for pdffile in pdf_files:
#     temp_list = list()
#     index = index + 1
#     pdfUrl = str(pdffile)
#     pdfUrl.rsplit('\\', 1)[1]
#     lista = pdfid.Main(pdfUrl)
    
#     # for word in words:

#     for word in lista.keys():
#         temp_list.append(lista[word][0])
#         # print(temp_list)
#     #temp_list.append(datetime.now().strftime('%H:%M:%S'))
#     matrix.append(temp_list)
  
# dataframe=pd.DataFrame(matrix)
# dataframe.to_csv("frequencies.csv")

def my_method(directory_path):
    temp_list = list()
    temp_list2 = list()
    pdfUrl = str(directory_path)
    lista = pdfid.Main(pdfUrl)
    
    # for word in words:

    for word in lista.keys():
        temp_list2.append(word)
        temp_list.append(lista[word][0])
        # print(temp_list)
    return temp_list2, temp_list

