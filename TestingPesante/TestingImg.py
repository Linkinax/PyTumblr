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


def PostaInstagram(Titolo, password):
    user = "unsaid.citations"
    passw= raw_input("Passowrd: ")
    oInstagramAPI = InstagramAPI(user, passw)
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
            print(frase+"\n")
            draw.text((30, 105+(100*botta)), frase,(255,255,255), font) 
            botta +=1
            img.save(str(0)+'.jpg')
            frase = "" 
    img = Image.open("0.jpg")
    draw = ImageDraw.Draw(img)
    print(frase+"\n")
    draw.text((30, 105+(100*botta)), frase,(255,255,255), font) 
    botta +=1
    img.save(str(0)+'.jpg')
        
   
if __name__ == '__main__':
    password = raw_input("Digita la password: ")
    cits = get_titoli_from_reddit('quotes')
    print("CIT: "+ cits[2]+ "\n")
    print ("Elementi: "+ str(cits.__len__()))
    for cit in cits:
        stampa(cit)
        autore = cit.split("-")
        PostaInstagram(cit+ " #quote #cit"+ "#"+autore[1], password)
    #PostaInstagram(cits[1] +" #quote")
    
        
        
        
        