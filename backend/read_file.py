#import fitz

class PdfFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        count = 0
        text = ""
        doc = fitz.open(self.file_name)
        num_pages = doc.pageCount  # discerning the number of pages will allow us to parse through all the pages

        while count < num_pages:  # The while loop will read each page
            pageRead = doc.loadPage(count)
            count += 1
            text += pageRead.getText("text")

        return text

    def get_file_name(self):
        return self.file_name

