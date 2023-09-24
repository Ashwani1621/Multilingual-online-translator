import requests
from bs4 import BeautifulSoup

lang_input = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
word_input = input("Type the word you want to translate:")
print("You chose {} as a language to translate {}.".format(lang_input, word_input))





def url_generator(lang, words):
    if lang == "en":
        l1 = "french"
        l2 = "english"
    else:
        l1 = "english"
        l2 = "french"
    full_url = "https://context.reverso.net/translation/{}-{}/{}".format(l1, l2, words)
    return full_url


url = url_generator(lang_input, word_input)



def connect():  # To establish the connection
    global page
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    status = page.status_code

    if status == 200:
        return ("{} OK".format(status))


def translations():  # To print translated words
    topics1=[]
    paragraphs = soup.select(".display-term")
    for paragraph in paragraphs:
        topics1.append(paragraph.get_text())
    return topics1


def examples(): # To print translated Examples
    topics2=[]
    paragraphs =soup.find_all('section', {'id': "examples-content"})
    for paragraph in paragraphs:
        examples = paragraph.find_all('span', {'class': 'text'})
        for example in examples:
            topics2.append(example.text.strip())
    return topics2




print(connect())
soup = BeautifulSoup(page.content,"html.parser")
print("Translations")
print(translations())
print(examples())






