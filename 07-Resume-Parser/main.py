from pdfminer.high_level import extract_text


# CONVERTING PDF INTO PLAIN TEXT
def extract_text_from_pdf(path):
    with open('resume.pdf', 'rb') as f:
        text = extract_text(f)
        print(text)
        with open('resume.txt', 'w') as converted:
            converted.write(text)


if __name__ == '__main__':
    extension = int(input('1 - PDF\n2 - DOCX\nChoose the file extension of your resume: '))
    if extension == 1:
        print(extract_text_from_pdf('./resume.pdf'))
    elif extension == 2:
        pass
    else:
        pass
