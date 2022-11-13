import docx2txt
import nltk
from pdfminer.high_level import extract_text


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


# CONVERTING PDF INTO TXT
def extract_text_from_pdf(path):
    with open(path, 'rb') as pdf:
        text = extract_text(pdf)
        with open('resume.txt', 'w') as converted:
            converted.write(text)
            print(f'resume.txt saved successfully.')
    return text


# CONVERTING DOCX INTO TXT
def extract_text_from_docx(path):
    with open(path, 'rb') as docx:
        text = docx2txt.process(docx)
        if text:
            text.replace('\t', ' ')
        with open('resume.txt', 'w') as converted:
            converted.write(text)
            print(f'resume.txt saved successfully.')
    return text


# EXTRACTING NAMES
def extract_names(txt):
    names = []
    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                names.append(' '.join(chunk_leave[0] for chunk_leave in chunk.leaves()))
    return names


if __name__ == '__main__':
    extension = int(input('1 - PDF\n2 - DOCX\nChoose the file extension of your resume: '))
    parsed_text = ''
    while extension != 1 and extension != 2:
        extension = int(input('1 - PDF\n2 - DOCX\nChoose the file extension of your resume: '))
    if extension == 1:
        parsed_text = extract_text_from_pdf('resume.pdf')
    elif extension == 2:
        parsed_text = extract_text_from_docx('resume.docx')
    else:
        pass
    name = extract_names(parsed_text)

    if name:
        print('Name: ', name[0])
