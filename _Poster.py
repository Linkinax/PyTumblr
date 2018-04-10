import Funzioni_PyTumblr
import pytumblr
from time import sleep

class _poster():
    def __init__(self, c_key, s_key, token, sec_token, API_key, nome_blog, querry_tumblr):
        self.stuff = Funzioni_PyTumblr.get_stuff_from_tumblr(querry_tumblr)

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

        pass
    def posta(self):
        """ questa f() posta su tumblr gli elementi presi dal dizionario {"url" : [tags]}"""
        self.filtra()

        for k in self.stuff.keys():
            if(len(self.stuff[k]) > 2):  # <- verifico che ci siano tag!
                # Filtro, per evitare i repost
                self.client.create_photo(self.name, state="queue", tags=self.stuff[
                                         k], source=k)  # <--- FUCK YEAH WORKA!!!!
                print ("Postato qualcosa by" + "\t" + self.name + "\n")
                sleep(2)

    def filtra(self):
        """ Filtro i post con alcuni TAG"""

        for k in self.stuff.keys():
            for f in self.FiltroTag:
                try:
                    if(f in self.stuff[k]):
                        print(k + " FUCK\t  GGWP, PERICOLO SCAMPATO!!!")
                        try:
                            del self.stuff[k]
                        except KeyError:
                            print ("Errore 0")
                            pass
                except KeyError:
                    print("Errore 1")
                    pass
    def Troll(self):
        print ('DIO MERDA')


