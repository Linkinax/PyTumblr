'''
Created on 27 mar 2016

@author: linky
'''
import requests
import random
import getpass
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium

import stem.process
from stem import Signal
from stem.control import Controller
from splinter import Browser



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

    browser.get('https://new.reddit.com/r/' + querry+ "/top/")

    #buttons = browser.find_element_by_css_selector("button.c-btn:nth-child(2)")
    # buttons.click()

    sleep(0.5)

    siteTable_ = browser.find_elements_by_class_name("s1wjvfsx-0.eQjckQ")[1]  # .get_attribute("innerHTML")
    html = browser.execute_script("return arguments[0].innerHTML;", siteTable_)
    #siteTable = browser.find_elements_by_class_name('sitetable linklisting')[0].get_attribute("innerHTML")
    try:
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        urls = soup.find_all(
            "img", attrs={"class": "media-element evajbz-0 ctgYFX"})
        titoli = soup.find_all(
            "h2",attrs={ "class": "cdg6za-1 gLBuPH"})
        for t in titoli:
            lista_titoli.append(t.get_text())

        for k in urls:
            lista_url.append(k.get("src"))
            

    except (TypeError):
        print ("Probabilmente hanno cambiato l'html")
    
    
    browser.quit()
    for i in range(0, lista_url.__len__()):
        lista_finale.append(lista_url[i] + '\t' + lista_titoli[i])

    return lista_finale


def get_nsfw_urls_from_reddit(querry):
    lista_titoli = []
    lista_url = []

    lista_finale = []

    # Il broser ha smesso di funzionare come dovrebbe
    browser = webdriver.Firefox(
        executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    browser.get('https://new.reddit.com/r/' + querry + '/new')

    buttons = browser.find_element_by_css_selector("button.c-btn:nth-child(2)")
    buttons.click()

    sleep(2.5)

    siteTable_ = browser.find_elements_by_id(
        "siteTable")[0]  # .get_attribute("innerHTML")
    html = browser.execute_script("return arguments[0].innerHTML;", siteTable_)
    #siteTable = browser.find_elements_by_class_name('sitetable linklisting')[0].get_attribute("innerHTML")
    try:
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        urls = soup.find_all(
            "a", attrs={"class": "thumbnail may-blank outbound"})

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

    

def get_titoli_from_reddit(query):
    lista_titoli = []
    # Il broser ha smesso di funzionare come dovrebbe
    browser = webdriver.Firefox(
        executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    browser.get('https://www.reddit.com/r/' + query+"/top/")#?sort=top&t=year")

    """
    buttons = browser.find_element_by_css_selector("button.c-btn:nth-child(2)")
    buttons.click()"""
    sleep(2.5)
    siteTable_ = browser.find_elements_by_id("siteTable")[0]  # .get_attribute("innerHTML")
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
def get_titoli_from_new_reddit(query):
    lista_titoli = []
    # Il broser ha smesso di funzionare come dovrebbe
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    browser.get('https://www.reddit.com/r/' + query+"/top/?sort=top&t=week")

    lista_span = browser.find_elements_by_tag_name("span") # .get_attribute("innerHTML")
    
    html = browser.execute_script("return arguments[0].innerHTML;", lista_span)
    #siteTable = browser.find_elements_by_class_name('sitetable linklisting')[0].get_attribute("innerHTML")
    try:
        soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
        urls = soup.find_all("a")#, attrs={"class": "title may-blank "})
        for k in urls:
            lista_titoli.append(k.getText())

    except (TypeError):
        print ("Probabilmente hanno cambiato l'html")

    browser.quit()
    return lista_titoli[1:]

def get_quotes():
    lista_titoli = []
    # Il broser ha smesso di funzionare come dovrebbe
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    browser.get('http://inspirationalshit.com/quotes')
    
    for _ in range(25):
        
        ps = browser.find_elements_by_class_name("text-uppercase")[26]
        auth = browser.find_elements_by_class_name("text-uppercase")[27]
        lista_titoli.append(ps.text+ " - " +auth.text)
        arrow = browser.find_element_by_class_name("nextbutton")
        arrow.click()
    
        sleep(0.5)
    browser.quit()
    return lista_titoli

def like_ig():
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    #browser.get('https://www.instagram.com/explore/?hl=it')
    browser.get('https://www.instagram.com/accounts/login/?hl=it')
    
    loggin = raw_input("Loggo?")
    
    id = browser.find_elements_by_name("username")
    passw= browser.find_elements_by_name("password")
    
    id[0].send_keys("unsaid.citations")
    password = raw_input("Zio passa la password: ")
    passw[0].send_keys(str(password))
    
    button = browser.find_elements_by_tag_name("button")[0]
    button.click()
    
    
    sleep(5)
    queries=["like4like","l4l","f4f","photo","likeforlike", "inspiration", "motivation", "smile","follow4follow","cute", "quotes", "happy"]#"quote", "inspiration",
    temp =0
    while True:
        for query in queries:
        
            browser.get('https://www.instagram.com/explore/tags/'+query+'/?hl=it')
            #browser.get('https://www.instagram.com/valentina.jitariu/?hl=it')
            sleep(5)
            siteTable = browser.find_elements_by_tag_name("article")
    
            for _ in range(1):#)"_e3il2")[9:]:#_mck9w._gvoze._tn0ps"):
                elementi = siteTable[0].find_elements_by_class_name('_4rbun')[9:]
                elementi[0].click()
                sleep(3)
                try:
                    like = browser.find_elements_by_class_name("_8scx2.coreSpriteHeartOpen")[0]
                    like.click()
                    temp += 1
                    
                except(IndexError):
                    print("Already liked zio =)\n")
                    sleep(1)
                try:
                    click_fuori= browser.find_elements_by_class_name("_dcj9f")[0]
                    click_fuori.click()
                except(IndexError):
                    print("Post Eliminato\n")
                    break
                    sleep(1)
                #browser.get('https://www.instagram.com/explore/tags/'+query+'/?hl=it')
                sleep(20)
                
                print("Likes messi: %d " %(temp))
def blondie_2():
    temp = 0
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    browser.get('https://web.whatsapp.com/')
    input = raw_input("DID it ?")
    
    who = browser.find_element_by_class_name("jN-F5.copyable-text.selectable-text")
    who.send_keys("Fabrizio maldarizzi")
    
    stronzo = browser.find_element_by_class_name("_2EXPL")
    stronzo.click()
    print(stronzo.text)
    input = raw_input("Nome")
    gente = browser.find_elements_by_class_name("_1wjpf")
    
    for k in gente:
        if(k.text == input):
            k.click()
            sleep(1)
            break
    while temp<5000:
            chat = browser.find_element_by_class_name("_2S1VP.copyable-text.selectable-text")
            mex = "Spero che il tuo cell sia in carica e in silenzioso: %d" %(temp)
            temp +=1
            chat.send_keys(mex)
            invia = browser.find_element_by_class_name("_2lkdt")
            invia.click()
            sleep(1)
                
    
    
    
def blondie():
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    browser.get('https://www.instagram.com/accounts/login/?hl=it')
    
    loggin = raw_input("Loggo?")
    
    id = browser.find_elements_by_name("username")
    passw= browser.find_elements_by_name("password")
    
    id[0].send_keys("unsaid.citations")
    password = raw_input("Zio passa la password: ")
    passw[0].send_keys(str(password))
    
    button = browser.find_elements_by_tag_name("button")[0]
    button.click()
    
    
    sleep(5)
    temp =0
    while True:
        
        browser.get('https://www.instagram.com/angelicavezzoli/?hl=it')
        sleep(5)
        siteTable = browser.find_elements_by_tag_name("article")
        input=raw_input("parto?")
        for elementi in siteTable[0].find_elements_by_class_name('_e3il2')[12:]:#)"_e3il2")[9:]:#_mck9w._gvoze._tn0ps"):
            elementi.click()
            sleep(3)
            try:
                like = browser.find_elements_by_class_name("_8scx2.coreSpriteHeartOpen")[0]
                like.click()
                temp += 1
                    
            except(IndexError):
                print("Already liked zio =)\n")
                sleep(1)
            try:
                click_fuori= browser.find_elements_by_class_name("_dcj9f")[0]
                click_fuori.click()
            except(IndexError):      
                print("Post Eliminato\n")
                break
                sleep(1)
                #browser.get('https://www.instagram.com/explore/tags/'+query+'/?hl=it')
            sleep(3)
                
            print("Likes messi: %d " %(temp))
    
def follow_ig():
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    #browser.get('https://www.instagram.com/explore/?hl=it')
    browser.get('https://www.instagram.com/accounts/login/?hl=it')
    
    loggin = raw_input("Loggo?")
    
    id = browser.find_elements_by_name("username")
    passw= browser.find_elements_by_name("password")
    
    id[0].send_keys("unsaid.citations")
    password = getpass.getpass("Zio passa la password: ")
    passw[0].send_keys(str(password))
    
    button = browser.find_elements_by_tag_name("button")[0]
    button.click()
    
    
    sleep(5)
    queries=["like4like","l4l","f4f","photo","likeforlike", "inspiration", "motivation", "smile","follow4follow","cute", "quotes", "happy"]#"quote", "inspiration",
    temp =0
    while True:
        for query in queries:
        
            browser.get('https://www.instagram.com/explore/tags/'+query+'/?hl=it')
            #browser.get('https://www.instagram.com/valentina.jitariu/?hl=it')
            sleep(5)
            siteTable = browser.find_elements_by_tag_name("article")
    
            for _ in range(1):#)"_e3il2")[9:]:#_mck9w._gvoze._tn0ps"):
                elementi = siteTable[0].find_elements_by_class_name('_4rbun')[9:]
                elementi[0].click()
                sleep(3)
                try:
                    follow = browser.find_elements_by_class_name("_qv64e._iokts._4tgw8._njrw0   ")[0]
                    follow.click()
                    temp += 1
                    
                except(IndexError):
                    print("Already liked zio =)\n")
                    sleep(1)
                try:
                    click_fuori= browser.find_elements_by_class_name("_dcj9f")[0]
                    click_fuori.click()
                except(IndexError):
                    print("Post Eliminato\n")
                    break
                    sleep(1)
                #browser.get('https://www.instagram.com/explore/tags/'+query+'/?hl=it')
                sleep(20)
                
                print("Following new %d people" %(temp))

def unfollow_ig():
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    #browser.get('https://www.instagram.com/explore/?hl=it')
    browser.get('https://www.instagram.com/accounts/login/?hl=it')
    
    loggin = raw_input("Loggo?")
    
    id = browser.find_elements_by_name("username")
    passw= browser.find_elements_by_name("password")
    
    id[0].send_keys("unsaid.citations")
    password = getpass.getpass("Zio passa la password: ")
    passw[0].send_keys(str(password))
    
    button = browser.find_elements_by_tag_name("button")[0]
    button.click()
    sleep(2)
    a=0
    while True:
        browser.get('https://www.instagram.com/unsaid.citations/?hl=it')
        sleep(20)
        profile = browser.find_elements_by_class_name("_fd86t")[2]
        profile.click()
        sleep(4)
        buttons = browser.find_elements_by_class_name("_qv64e._t78yp._4tgw8._njrw0")
        for i in range(9):
            buttons[i].click()
            sleep(4)
            print("Unfollowed: %d\n"%(a))
            a+=1
        
    
def affiliate_marketing(url):
    
    logged=False
    
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    #browser.get('https://www.instagram.com/explore/?hl=it')
    browser.get(url)
    
    
    
    for i in range(5):
        button = browser.find_elements_by_class_name("reblog_button")[i]
        button.click()
        sleep(2)
        if logged != True:
            login_btn = browser.find_elements_by_id('signup_login_button')[0]
            login_btn.click()
            sleep(1)
            
            input_email = browser.find_element_by_id("signup_determine_email")
            input_email.send_keys("memesforages@gmail.com")
            sleep(0.5)
            next_btn = browser.find_elements_by_id("signup_forms_submit")[0]
            next_btn.click()
            sleep(4)
            try:
                next_btn2 = browser.find_elements_by_class_name("forgot_password_link")[0]
                next_btn2.click()
            except(ElementNotInteractableException):
                next_btn2 = browser.find_elements_by_class_name("forgot_password_link")[0]
                next_btn2.click()
            sleep(4)
            
           
            input = raw_input("metti la pass")
                #input_pass = browser.find_element_by_id("signup_password")
                
            
            
            btn_log= browser.find_element_by_id("signup_forms_submit")
            btn_log.click()
            logged = True
        
        
        sleep(4)
        tags_input = browser.find_elements_by_class_name("post-form--tag-editor")[0]
        tags_input.send_keys("ads")
        tags_input.send_keys(Keys.TAB)
        sleep(2)
        tags_input.send_keys("fashion, chic, clothes, tee, hooodie")
        
        
        drop_down = browser.find_elements_by_class_name("dropdown-area.icon_arrow_carrot_down.pinned-target")[0]
        drop_down.click()
        
        sleep(4)
        queue_option  = browser.find_elements_by_class_name("item-option")[1]
        queue_option.click()
        
        sleep(3)
        queue_btn  = browser.find_element_by_class_name("button-area.create_post_button")
        queue_btn.click()
        sleep(2)
        browser.get(url)
    browser.quit()
def insta_account():
    
    proxyIP = "127.0.0.1"
    proxyPort = 9150
 
    proxy_settings = {"network.proxy.type":1,
                      "network.proxy.socks": proxyIP,
                      "network.proxy.socks_port": proxyPort,
                      "network.proxy.socks_remote_dns": True,
                      }
    
    browser_sp = Browser('firefox', profile_preferences=proxy_settings,executable_path='/home/alex/Documents/Coder/geckodriver')
    browser_sp.visit("http://www.icanhazip.com")
    switchIP()
    sleep(2)
    browser_sp.visit("http://www.instagram.com/accounts/login/?hl=it")
    
    sleep(2)
    a_tags = browser_sp.find_by_tag("a")
    for a in a_tags:
        if a.text == "Iscriviti":
            a.click()
    
    email = get_temp_email()
    user = email.split("@")[0]+ "linky"
    browser_sp.fill("emailOrPhone", email)
    browser_sp.fill("fullName", "Pebblor El Munchy")
    browser_sp.fill("username", user)
    browser_sp.fill("password", "fuckthepoliS")
    buttons = browser_sp.find_by_tag("button")
    for button in buttons:
        if button.text=="Iscriviti":
            button.click()
    file_txt = open("users.txt", "a")
    file_txt.writelines(user+"\n")
    file_txt.close()
    browser_sp.close()
    
def get_temp_email():
    browser_email = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser_email.refresh()
    browser_email.get("https://robot-mail.com/msg")
    sleep(2)
    email = browser_email.find_element_by_class_name("address.what_to_copy")
    email_text = email.text
    browser_email.close()
    return email_text

def switchIP():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
def __main__():
   
    
        
        
    print("\nICSDI\n")
