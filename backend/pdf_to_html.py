import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import HTMLConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams


def convert_pdf_to_html(input, output="temp.html"):
    """
    :param input: PDF File to be converted,
    :param output:  output filename, default is temp.html
    :return: doesn't return anything
    """
    debug = 0
    password = b''
    pagenos = set()
    maxpages = 0
    imagewriter = None
    rotation = 0
    layoutmode = 'normal'
    encoding = 'utf-8'
    scale = 1
    caching = True
    laparams = LAParams()

    #
    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFPageInterpreter.debug = debug
    #
    rsrcmgr = PDFResourceManager(caching=caching)

    outfile=output
    if outfile:
        outfp = open(outfile, 'w', encoding=encoding)
    else:
        outfp = sys.stdout

    device = HTMLConverter(rsrcmgr, outfp, scale=scale,
                           layoutmode=layoutmode, laparams=laparams,
                           imagewriter=imagewriter, debug=debug)

    with open(input, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, pagenos,
                                      maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            page.rotate = (page.rotate+rotation) % 360
            interpreter.process_page(page)
    device.close()
    outfp.close()
    return

#convert_pdf_to_html("../media/user_donart/Gothaer_GewerbeProtect_BHV_Handel_Handwerk_Gewerbe_216295.pdf")
#if __name__ == '__main__': sys.exit()
