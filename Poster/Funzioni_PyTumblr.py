'''
Created on 27 mar 2016

@author: linky
'''
import requests
import random
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def get_stuff_from_tumblr(arg):
    """
        ritorna un dizionario {url: [tag1, tag2]}
    """
    diz = {}

    url = 'https://www.tumblr.com/search/' + arg  # +'/recent'
    response = requests.get(url)
    sleep(5)
    html = response.content

    soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

    list_post = soup.find_all('img', attrs={"class": "photo"})
    a = 0
    for k in list_post:
        # print k.get('src')
        if(not 'data' in k.get('src')):
            diz[k.get('src')] = get_tags_from_tumblr(
                k)  # TO DO: get_fucking_tgs, DONE!!
            a += 1

    return diz


def get_tags_from_tumblr(div1_post):
    """
        prende in ingresso il nodo html di un immagine e risale ai tag!
    """
    tmp = div1_post.find_parents()

    div_post = tmp[1].find_next_siblings()
    lista_tag = []
    try:
        tags = div_post[1].find_all(
            'a', attrs={"class": "post_tag"})  # get('data-tag')
        for k in range(tags.__len__()):
            # vediamo se la lista contiene qualcosa:
            if(tags[k].get('data-tag')):
                lista_tag.append(tags[k].get('data-tag'))

    except(IndexError):
        # I post analizzati non presentano immagini
        pass

    return lista_tag


def get_urls_from_reddit(querry):
    lista_titoli = []
    lista_url = []

    lista_finale = []

    browser = webdriver.Firefox(
        executable_path='/home/alex/Documents/Coder/geckodriver')

    browser.get('https://www.reddit.com/r/' + querry)

    #buttons = browser.find_element_by_css_selector("button.c-btn:nth-child(2)")
    # buttons.click()

    sleep(0.5)

    siteTable_ = browser.find_elements_by_id(
        "siteTable")[0]  # .get_attribute("innerHTML")
    html = browser.execute_script("return arguments[0].innerHTML;", siteTable_)
    #siteTable = browser.find_elements_by_class_name('sitetable linklisting')[0].get_attribute("innerHTML")
    try:
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        urls = soup.find_all(
            "div")#mi passo tutti i div, dentro c'e' l'attr data-
            #attrs={"class": "title may-blank "})
            
        l=0

        for k in urls:
            if(k.get("data-url")):
               lista_url.append(k.get("data-url"))
               #variabile = k.contents[4].innerText()
               variabile = k.find_all("p", attrs={"class": "title"})[0]#<---Debugging: guarda cosa contiene 
               #print("Potrei addaree: %s" %(variabile.text))
               lista_titoli.append(variabile.text)
               l +=1
            

    except (TypeError):
        print ("Probabilmente hanno cambiato l'html")

    browser.quit()
    
    l =0 
    for i in range(0, lista_url.__len__()):
        lista_finale.append(lista_url[i]+ '\t'+ lista_titoli[l])
        #print("Dio cane, Addato %s \t %s \n" %(lista_url[i], lista_titoli[l]) )
        l +=1
    

    return lista_finale[1:]


def get_nsfw_urls_from_reddit(querry):
    lista_titoli = []
    lista_url = []

    lista_finale = []

    # Il broser ha smesso di funzionare come dovrebbe
    browser = webdriver.Firefox(
        executable_path='/home/alex/Documents/Coder/geckodriver')
                                                              
    
    browser.refresh()
    browser.get('https://www.reddit.com/r/' + querry + '/new')
    
    
    buttons = browser.find_element_by_css_selector("button.c-btn:nth-child(2)")
    buttons.click()

    sleep(2.5)

    siteTable_ = browser.find_elements_by_id(
        "siteTable")[0]  # .get_attribute("innerHTML")
    html = browser.execute_script("return arguments[0].innerHTML;", siteTable_)
    #siteTable = browser.find_elements_by_class_name('sitetable linklisting')[0].get_attribute("innerHTML")--> DIO PORCO
    try:
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        urls = soup.find_all(
            "a", attrs={"class": "title may-blank outbound"})

        for k in urls:
            lista_url.append(k.get("href"))
            lista_titoli.append(k.getText())

    except (TypeError):
        print ("Probabilmente hanno cambiato l'html")

    browser.quit()
    for i in range(0, lista_url.__len__()):
        lista_finale.append(lista_url[i] + '\t' + lista_titoli[i])

    return lista_finale


def get_querry():
    lista = ['earth', 'amazing', 'pics', 'nature', 'wild', 'view']
    #['aww','cute','wow', 'awesome','incredible','adorable','cute animals', 'animals', 'cute']
    #['food', 'delicious', 'sweet', 'yummy', 'food porn', 'chocolate', 'candy', 'healty food']
    #['funny','meme','dank memes', 'humour','lol','funny pictures', 'memes','hilarious']
    #['earth', 'amazing', 'pics', 'nature', 'wild','view']
    return lista[random.randint(0, len(lista)) - 1]


def get_searching_tags(tags):
    # data una lista di tags, ritorna un tag a caso presente nella lista
    return tags[random.randint(0, len(tags)) - 1]


def smart_likes(query):
    """
        ritorna una una lista con : post_id,reblog_key ,tags[]
    """
    lista_str = []
    response = requests.get(
        'https://www.tumblr.com/search/' + query + '/recent')

    html = response.content

    soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

    articles = soup.find_all('article')

    for article in articles:
        info = []
        tags = article.find_all('a', attrs={'class': 'post_tag'})
        lista_tags = []
        post_id = article['data-id']
        post_key = article['data-reblog-key']

        for k in tags:
            lista_tags.append(k['data-tag'])
        info.append(post_id)
        info.append(post_key)
        info.append(lista_tags)

        lista_str.append(info)
    return lista_str


def smart_reblog(query):
    """ ritorna una una lista con : post_id,reblog_key ,tags[]"""

    lista_finale = []

    response = requests.get('https://www.tumblr.com/search/' + query)

    html = response.content

    soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

    articles = soup.find_all('article')

    for article in articles:
        notes = article.find('span', attrs={'class': 'note_link_current'})
        _note = notes.getText().split(' ')
        note = _note[0].replace(",", '')
        if(int(note) > 75):
            print ("Ha %d note" % (int(note)))
            info = []
            tags = article.find_all('a', attrs={'class': 'post_tag'})
            lista_tags = []
            post_id = article['data-id']
            post_key = article['data-reblog-key']

            for k in tags:
                lista_tags.append(k['data-tag'])
            info.append(post_id)
            info.append(post_key)
            info.append(lista_tags)

            lista_finale.append(info)
    return lista_finale
def smart_reblog_adv(pg_web):
    lista_finale = []

    response = requests.get(pg_web)
    html = response.content
    soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    articles = soup.find_all('article')

    for article in articles:
        reblog_control = article.find('a', attrs={'class': 'reblog_button'})
        link = reblog_control['href']
        lista_finale.append(link)
        
    return lista_finale

def get_titoli_from_reddit(query):
    lista_titoli = []

    # Il broser ha smesso di funzionare come dovrebbe
    browser = webdriver.Firefox(
        executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    browser.get('https://www.reddit.com/r/' + query+"/top/?sort=top&t=month")

    """
    buttons = browser.find_element_by_css_selector("button.c-btn:nth-child(2)")
    buttons.click()"""

    sleep(2.5)

    siteTable_ = browser.find_elements_by_id(
        "siteTable")[0]  # .get_attribute("innerHTML")
    html = browser.execute_script("return arguments[0].innerHTML;", siteTable_)
    #siteTable = browser.find_elements_by_class_name('sitetable linklisting')[0].get_attribute("innerHTML")
    try:
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        urls = soup.find_all("a", attrs={"class": "title may-blank "})

        for k in urls:
            lista_titoli.append(k.getText())

    except (TypeError):
        print ("Probabilmente hanno cambiato l'html")

    browser.quit()
    return lista_titoli[1:]

def __main__():
    print("\nICSDI\n")
