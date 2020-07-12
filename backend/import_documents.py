from backend.read_file import PdfFile
import pandas as pd
from backend.sources import *

# category_source="backend/data/Leistungstexte vorbereitung.xlsx"
#category_list = pd.read_excel(sources['category_source']).iloc[:,0]

gothear_file_path=sources['gothear']
gothear_obj=PdfFile(gothear_file_path)



