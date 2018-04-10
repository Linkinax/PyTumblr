import pytumblr
from .RedditPoster import RedditBlog as rb
from .Funzioni_PyTumblr import get_titoli_from_reddit
from .Funzioni_PyTumblr import get_urls_from_reddit

class Quotes(rb):
    def __init__(self, c_key, s_key, token, sec_token, API_key, nome_blog, querry, tags):
        '''
        E' uguale alla classe RedditBlog solo che ha un metodo in piu'
        '''
        
        #self.stuff = get_urls_from_reddit(querry)
        self.tags = tags
        
        #Autorizzazioni per tumblr
        self.Customer_key = c_key
        self.Secret_key = s_key
        self.Token = token
        self.Secre_token= sec_token
        self.API_key= API_key
        self.name = nome_blog
        
        self.client = pytumblr.TumblrRestClient(self.Customer_key, self.Secret_key, self.Token, self.Secre_token )

    def posta_reddit_quotes(self):
        cits = get_titoli_from_reddit('quotes')
        print('Ci sono %d elementi\t %s'  % (len(cits), self.name))
        
        for i in range(len(cits)):
            #cerco i trattini nella cit: bla bla bla - Autore
            #splitto la stringa in 2 pezzi, pezzo[0] = citazione, pezzo[1] = Autore

            pezzi = cits[i].split('-')
            if len(pezzi)>1:
                if len(pezzi[1])<15:
                    self.client.create_quote(self.name,state="queue",tags=self.tags, quote=pezzi[0], source=pezzi[1])
                    print ("Fatto")
        print ("Finished")
        