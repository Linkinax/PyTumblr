'''
Created on Mar 12, 2018

@author: alex
'''
import PIL
import getpass
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from Poster.Funzioni_PyTumblr import get_titoli_from_reddit, get_quotes
from InstagramAPI import InstagramAPI
import stampa_dio
from time import sleep

def PostaInstagram(Titolo, password):
    user = "unsaid.citations"
    oInstagramAPI = InstagramAPI(user, password)
    oInstagramAPI.login()  # login

    photo_path = '/home/alex/Documents/Coder/TestingPesante/0.jpg'
    caption = Titolo
    oInstagramAPI.uploadPhoto(photo_path, caption=caption)
def stampa(stringa):
    num=0
    
    img = Image.open("sfondo_quotes4.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("TravelingTypewriter.otf" , 115)
            
    parole = stringa.split(" ")
    frase = ""
    conta_parole=0
    botta =0 
    
    for parola in parole:
        frase += parola+ " "
        conta_parole+=1 
        if(len(frase)>=24):
            conta_parole -= 1
            frase.replace(parola+" ", "")
            #img = Image.open("0.jpg")
            draw = ImageDraw.Draw(img)
            #print(frase+"\n")
            draw.text((30, 105+(100*botta)), frase,(255,255,255), font) 
            botta +=1
            img.save(str(0)+'.jpg')
            frase = ""
                
    #per srivere l'ultima riga: 
    img = Image.open("0.jpg")
    draw = ImageDraw.Draw(img)
    #print(frase+"\n")
    draw.text((30, 105+(100*botta)), frase,(255,255,255), font) 
    botta +=1
    img.save(str(0)+'.jpg')
def author(stringa):
    if(len(stringa)>0):
        if(stringa[0] == ' '):
            return stringa[1:].replace("-", "" )
        else:
            return stringa.replace("-", '')
   
if __name__ == '__main__':
    password = getpass.getpass("Digita la password: ")
    
    cits = get_quotes()
    for cit in cits:                   
        pezzi = cit.split('-')
        if len(pezzi)>1:
            if len(pezzi[1])<35:
                print("Vuoi postare: "+cit)
                risposta= raw_input("y/n: ")
                if risposta=='y':
                    stampa(cit)
                    PostaInstagram(pezzi[0]+ " #quote #amen #quoteoftheday #life #instaquotes #wisdom #true #like4like #follow4follow #sayings #motivational #motivationalquotes #dailyquotes #inspiration #famouswords #quotation #citation #words #said #cit "+"#"+str(author(pezzi[1])).replace(" ", ''), password)                 
                else:
                    print("Ok non posto quella quote e.e\n")      
    
    
                    
                    
                    