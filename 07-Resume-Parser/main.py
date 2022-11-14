import docx2txt
import nltk
import re
import requests
import subprocess
from tokens import *
from pdfminer.high_level import extract_text


# DOWNLOADING NLTK LIBRARIES
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')


# SETTING UP PHONE PARSING REGEX
PHONE_REG = re.compile(r"[\+\(]?[1-9][0-9 .\-\()]{12,}[0-9]")

# SETTING UP EMAIL PARSING REGEX
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')



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


# EXTRACTING PHONE NUMBER
def extract_phone_number(txt):
    phone = re.findall(PHONE_REG, txt)
    if phone:
        number = ''.join(phone[0])
        if txt.find(number) > 0 and len(number) < 16:
            return number


# EXTRACTING EMAIL ADDRESS
def extract_email_address(txt):
    return re.findall(EMAIL_REG, txt)


# EXTRACTING SKILLS
def skill_exists(skill):
    url = f'https://api.apilayer.com/skills?q={skill}&amp;count=1'
    headers = {'apikey': API_KEY}  # INSERT YOUR SKILL API KEY HERE (go to https://apilayer.com/marketplace/skills-api)
    response = requests.request('GET', url, headers=headers)
    result = response.json()

    if response.status_code == 200:
        return len(result) > 0 and result[0].lower() == skill.lower()
    raise Exception(result.get('message'))


def extract_skills(input_txt):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_txt)

    # FILTERING OUT STOP WORDS
    filtered_tokens_1 = [w for w in word_tokens if w not in stop_words]

    # FILTERING OUT PUNCTUATION
    filtered_tokens_2 = [w for w in filtered_tokens_1 if w.isalpha()]

    # GENERATING BIGRAMS AND TRIGRAMS
    bigrams_tigrams = list(map(' '.join, nltk.everygrams(filtered_tokens_2, 2, 3)))

    found_skills = set()

    for token in filtered_tokens_2[0:50]:  # HERE I SLICED THE SET TO LIMIT THE ITERATIONS AND NOT CRASH THE PROGRAM
        if skill_exists(token.lower()):
            print('aqui 6')
            found_skills.add(token)

    for ngram in bigrams_tigrams[0:50]:   # HERE I SLICED THE SET TO LIMIT THE ITERATIONS AND NOT CRASH THE PROGRAM
        if skill_exists(ngram.lower()):
            found_skills.add(ngram)

    return found_skills


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
    phone_number = extract_phone_number(parsed_text)
    email_address = extract_email_address(parsed_text)
    skills = extract_skills(parsed_text)
    if name:
        print('Name: ', name[0])
    if phone_number:
        print('Phone number: ', phone_number)
    if email_address:
        print('Email address: ', email_address)
    if skills:
        print('Skills :', skills)
