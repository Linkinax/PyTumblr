'''
Created on 27 mar 2016

@author: linky
'''
import Funzioni_PyTumblr
import pytumblr
from time import sleep
from _Poster import _poster as ps


class Poster(ps):
    '''
    classdocs

    Questa classe avra' il compito di gestire la ricezione delle immagini da postare
    '''

    def __init__(self, c_key, s_key, token, sec_token, API_key, nome_blog, querry_tumblr, tags):
        '''
        Constructor
        '''
        self.stuff = Funzioni_PyTumblr.get_stuff_from_tumblr(querry_tumblr)
        self.tags = tags

        self.FiltroTag = ['art', 'myart', 'my art', 'own', 'own edit', 'myown']
        # Autorizzazioni per tumblr
        self.Customer_key = c_key
        self.Secret_key = s_key
        self.Token = token
        self.Secre_token = sec_token
        self.API_key = API_key

        self.name = nome_blog
        self.query = querry_tumblr
        self.client = pytumblr.TumblrRestClient(self.Customer_key, self.Secret_key, self.Token, self.Secre_token)

    def posta(self):
        """ questa f() posta su tumblr gli elementi presi dal dizionario {"url" : [tags]}"""
        self.filtra()

        for k in self.stuff.keys():
            if(len(self.stuff[k]) > 2):  # <- verifico che ci siano tag!
                # Filtro, per evitare i repost
                self.client.create_photo(self.name, state="queue", tags=self.stuff[
                                         k], source=k)  # <--- FUCK YEAH WORKA!!!!
                print( "Postato qualcosa by" + "\t" + self.name + "\n")
                sleep(2)

    def filtra(self):
        """ Filtro i post con alcuni TAG"""

        for k in list(self.stuff.keys()):
            for f in self.FiltroTag:
                try:
                    if(f in list(self.stuff[k])):
                        print(k + " FUCK\t  GGWP, PERICOLO SCAMPATO!!!")
                        try:
                            del self.stuff[k]
                            
                        except KeyError:
                            print ("NOn ho potuto eliminare la chiave\n")
                            pass
                except KeyError:
                    print("Provo a passare roba POTENZIALMENTE CIT eliminata")
                    pass

    def likes(self):

        #infos = Funzioni_PyTumblr.smart_likes(Funzioni_PyTumblr.get_querry())
        infos = Funzioni_PyTumblr.smart_likes(Funzioni_PyTumblr.get_searching_tags(self.tags))


        for k in infos:
            self.client.like(k[0], k[1])
        print ("Messi %d Likes" % (len(infos)))

    def reblog(self):
        lista = Funzioni_PyTumblr.smart_reblog(self.query)

        for k in lista:
            self.client.reblog(self.name, id=k[0], reblog_key=k[1], tags=k[2])
        print ("Reblogged: %d posts" % (len(lista)))

    def posta_quotes(self):
        cits = Funzioni_PyTumblr.get_titoli_from_reddit('quotes')
        tagsss = ['quote', 'cit', 'citation', 'famous words']
        print('Ci sono %d elementi\t %s' % (len(cits), self.name))

        for cit in cits:
            self.client.create_quote(
                self.name, state="queue", tags=tagsss, quote=cit)
            print ("Fatto")
        print ("Finished")
