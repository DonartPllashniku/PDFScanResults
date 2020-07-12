import re

def extract_from_html(input_file="temp.html"):
    """
    :param input_file: HTML input file to be read from
    :return: 1. list of blocks containing headlines and paragraphs from headline to headline
            2. list of headlines lists that include headlines till a paragraph is found
        first and second list are equal on length
    """

    file_to_read = open(input_file, "r+", encoding="utf8")
    html_content = file_to_read.read()

    start_pos = [m.start() for m in re.finditer("font-family:.+Bold", html_content)]
    text_extracted = []
    temp_headlines=[]
    headlines_extracted=[]
    for j in range(0, len(start_pos)):

        i = start_pos[j]

        if j == len(start_pos) - 1:
            end = len(html_content)-1
        else:
            end = start_pos[j+1]
        text_to_read = html_content[i:end]
        begin_index = re.search(">", text_to_read).end()
        end_index = re.search("</span>", text_to_read).start()
        headline_extracted = text_to_read[begin_index:end_index]
        headline_extracted = headline_extracted.replace("<br>", "")
        temp_headlines.append(headline_extracted)
        paragraph_search = re.search("(?<!Bold); font-size.*>", text_to_read)

        if not paragraph_search:
            continue
        else:
            paragraph_start_index = paragraph_search.start()
            text_to_read = text_to_read[paragraph_start_index:end]
            paragraph_start_index = re.search(">", text_to_read).end()
            paragraph_end_index = [m.start() for m in re.finditer("</span>", text_to_read)][-1]
            paragraph_extracted = text_to_read[paragraph_start_index:paragraph_end_index]
            paragraph_extracted = paragraph_extracted.replace("<br>", "")
            paragraph_extracted = re.sub("<span style.+?>", "", paragraph_extracted)
            paragraph_extracted = re.sub("<div style.+?>", "", paragraph_extracted)
            paragraph_extracted = re.sub("</span>", "", paragraph_extracted)
            paragraph_extracted = re.sub("</div>", "", paragraph_extracted)
            #TODO: Recheck this line they are new
            paragraph_extracted = re.sub("<a.*?>", "", paragraph_extracted)

            #The chars not recognized by the pdfminer shall be replaced
            paragraph_extracted = replaceUnknownChars(paragraph_extracted)

            collected_headlines=""
            for head in temp_headlines:
                collected_headlines+=head
            text_extracted.append(collected_headlines+paragraph_extracted)
            headlines_extracted.append(temp_headlines.copy())
            temp_headlines.clear()

    return text_extracted, headlines_extracted

def replaceUnknownChars(paragraph):
    paragraph = paragraph.replace("fÃ¼r", "für")
    paragraph = paragraph.replace("Ã¤", "ä")
    paragraph = paragraph.replace("Ã¼", "ü")
    paragraph = paragraph.replace('Ã¶', 'ö')
    paragraph = paragraph.replace('Ã„', 'Ä')
    paragraph = paragraph.replace('ÃŸ', 'ß')
    paragraph = paragraph.replace('€', 'â‚¬')
    paragraph = paragraph.replace('ï¬€ ', 'ff')
    paragraph = paragraph.replace('ï¬ ', 'f')
    paragraph = paragraph.replace('Ãœ', 'Ü')
    paragraph = paragraph.replace('Ã–', 'Ö')
    paragraph = paragraph.replace('â€¢', '•')
    paragraph = paragraph.replace('â€“', '–')
    paragraph = paragraph.replace('(cid:228)', 'ä')
    paragraph = paragraph.replace('(cid:252)', 'ü')
    paragraph = paragraph.replace('(cid:246)', 'ö')
    paragraph = paragraph.replace('(cid:223)', 'ß')
    #Recheck these
    paragraph = paragraph.replace('(cid:223)', 'Ü')
    paragraph = paragraph.replace('(cid:252)', 'ü')

    
    return paragraph




