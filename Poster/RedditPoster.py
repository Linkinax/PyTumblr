'''
Created on 25 apr 2016

@author: linky
'''
import requests
from  .Funzioni_PyTumblr import get_urls_from_reddit
import pytumblr
from time import sleep
from .Funzioni_PyTumblr import get_nsfw_urls_from_reddit
from .Funzioni_PyTumblr import get_titoli_from_reddit
from Funzioni_PyTumblr import smart_reblog_adv


class RedditBlog():
    '''
    classdocs
    '''
    def __init__(self, c_key, s_key, token, sec_token, API_key, nome_blog, querry, tags):
        '''
        Constructor
        '''
        
        self.stuff = get_urls_from_reddit(querry)
        self.tags = tags
        
        #Autorizzazioni per tumblr
        self.Customer_key = c_key
        self.Secret_key = s_key
        self.Token = token
        self.Secre_token= sec_token
        self.API_key= API_key
        self.name = nome_blog
        
        self.client = pytumblr.TumblrRestClient(self.Customer_key, self.Secret_key, self.Token, self.Secre_token )
        
        
    def posta(self):
        print('Ci sono %d elementi\t %s'  % (len(self.stuff), self.name))
        for k in self.stuff:
            minilista =  k.split('\t')
            try:
            #self.client.create_photo(self.name,state="published", tags=self.tags, source=minilista[0], caption= minilista[1])
                self.client.create_photo(self.name,state="queue", tags=self.tags, source=minilista[0], caption= minilista[1])
                print("vorrei postaare: %s\t %s"%(minilista[0], minilista[1]))
                print( "Fatto")
            except (requests.exceptions.ConnectionError):
                print("Dio Merda, Errore loro\n")
            sleep(2)
        print( 'ENDED')
        
    def posta_quotes(self):
        cits = get_titoli_from_reddit('quotes')
        sources = []
        for k in cits:
            sources.append(k)

        tagsss = ['quote', 'cit', 'citation', 'famous words']
        print('Ci sono %d elementi\t %s'  % (len(cits), self.name))
        
        for cit in cits:
            self.client.create_quote(self.name,state="queue",tags=self.tags, caption=cit)
            print ("Fatto")
        print ("Finished")
    def reblog_adv(self):
        lista_url = "https://thenaturalscenery.tumblr.com/tagged/14871e7"
        
        lista_items = smart_reblog_adv(lista_url)
        id_p = lista_items[0].split("/")[0]
        key_p= lista_items[0].split("/")[1]
        self.client.like( id=id_p, reblog_key=key_p)
class RedditBlog_nsfw():
    '''
    classdocs
    '''
    def __init__(self, c_key, s_key, token, sec_token, API_key, nome_blog, query, tags):
        '''
        Constructor
        '''
        
        self.stuff = get_nsfw_urls_from_reddit(query)
        self.tags = tags
        
        #Autorizzazioni per tumblr
        self.Customer_key = c_key
        self.Secret_key = s_key
        self.Token = token
        self.Secre_token= sec_token
        self.API_key= API_key
        self.name = nome_blog
        
        self.client = pytumblr.TumblrRestClient(self.Customer_key, self.Secret_key, self.Token, self.Secre_token )
        
        
    def posta(self):
        print('Ci sono %d elementi\t %s'  % (len(self.stuff), self.name))
        for k in self.stuff:
            minilista =  k.split('\t')
            self.client.create_photo(self.name,state="published", tags=self.tags, source=minilista[0], caption= minilista[1])
            print ("Fatto")
            sleep(2)
        print ('ENDED')