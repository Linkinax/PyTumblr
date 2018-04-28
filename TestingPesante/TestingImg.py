'''
Created on Mar 12, 2018

@author: alex
'''
import PIL

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from Funzioni_PyTumblr import get_titoli_from_reddit
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
    
    if(stringa[0] == ' '):
        return stringa[1:].replace("-", "" )
    else:
        return stringa.replalce("-", '')
   
if __name__ == '__main__':
    password = raw_input("Digita la password: ")
    cits = get_titoli_from_reddit('quotes')
    print ("Elementi: "+ str(cits.__len__()))
    #PostaInstagram(cits[1] +" #quote")"
                    
    for cit in cits:                   
        #print("CIT: "+ cit+ "\n")
        pezzi = cit.split('."')
        if len(pezzi)>1:
            if len(pezzi[1])<35:
                print("Vuoi postare: "+pezzi[0])
                risposta= raw_input("y/n: ")
                if risposta=='y':
                    stampa(cit)
                    PostaInstagram(pezzi[0]+ " #quote #amen #quoteoftheday #life #instaquotes #wisdom #true #like4like #follow4follow #sayings #motivational #motivationalquotes #dailyquotes #inspiration #famouswords #quotation #citation #words #said #cit "+"#"+str(author(pezzi[1])).replace(" ", ''), password)                 
                else:
                    print("Ok non posto quella quote e.e\n")      
                    
                    
                    
                    