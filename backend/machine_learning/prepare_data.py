# import text_nlp as tnlp
import pandas as pd
import os




fileDir = os.path.dirname(os.path.realpath('__file__'))
#For accessing the file in the parent folder of the current folder
filename = os.path.join(fileDir, '../dataset-fixed-v4.csv')

dataset = pd.read_csv(filename, delim_whitespace=True)




keywords=dataset.columns[3:]



count=0
matrix=list()
for data in dataset.iloc[:, 1]:
    data = data.replace("fÃ¼r", "für")
    data = data.replace("Ã¤", "ä")
    data = data.replace("Ã¼", "ü")
    data = data.replace('Ã¶', 'ö')
    data = data.replace('Ã„', 'Ä')
    data = data.replace('ÃŸ', 'ß')
    data = data.replace('€', 'â‚¬')
    data = data.replace('ï¬€ ', 'ff')
    data = data.replace('ï¬ ', 'f')
    data = data.replace('Ãœ', 'Ü')
    data = data.replace('Ã–', 'Ö')
    data = data.replace('â€¢', '•')
    data = data.replace('â€“', '–')
    data = data.replace('(cid:228)', 'ä')
    data = data.replace('(cid:252)', 'ü')
    data = data.replace('(cid:246)', 'ö')
    data = data.replace('(cid:223)', 'ß')

    # tokens, bigrams, trigrams = tnlp.tokenize_text(data)


    dict_of_frequencies = {}
    for keyword in keywords:
        dict_of_frequencies[keyword] = 0

    for keyword in keywords:
        for token in tokens:
            if token.casefold() == keyword.casefold():
                dict_of_frequencies[keyword] += 1
        for bigram in bigrams:
            new_bigram=bigram[0]+" "+bigram[1]

            if new_bigram.casefold() == keyword.casefold(): 
                dict_of_frequencies[keyword] += 1

                if bigram[0].casefold() in keywords:
                    if bigram[0].casefold() in dict_of_frequencies:
                        dict_of_frequencies[bigram[0].casefold()] -= 1


                if bigram[1].casefold() in keywords:
                    if bigram[1].casefold() in dict_of_frequencies:
                        dict_of_frequencies[bigram[1].casefold()] -= 1

        for trigram in trigrams:
            new_trigram=trigram[0]+" "+trigram[1]+" "+trigram[2]
            bigram1 = trigram[0]+" "+trigram[1]
            bigram2 = trigram[1]+" "+trigram[2]

            if new_trigram.casefold() == keyword.casefold():
                dict_of_frequencies[keyword] += 1

                if bigram1.casefold() in keywords:
                    if bigram1.casefold() in dict_of_frequencies:
                        dict_of_frequencies[bigram1.casefold()] -= 1

                if bigram2.casefold() in keywords:
                    if bigram2.casefold() in dict_of_frequencies:
                        dict_of_frequencies[bigram2.casefold()] -= 1

                if bigram1.casefold() in keywords and bigram2.casefold() in keywords:
                    if trigram[0].casefold() in keywords:
                        if trigram[0].casefold() in dict_of_frequencies:
                            dict_of_frequencies[trigram[0].casefold()] += 1

                    if trigram[1].casefold() in keywords:
                        if trigram[1].casefold() in dict_of_frequencies:
                            dict_of_frequencies[trigram[1].casefold()] += 1

                    if trigram[2].casefold() in keywords:
                        if trigram[2].casefold() in dict_of_frequencies:
                            dict_of_frequencies[trigram[2].casefold()] += 1





    matrix.append(list(dict_of_frequencies.values()))


dataframe=pd.DataFrame(matrix)
dataframe.to_csv("frequencies.csv")
