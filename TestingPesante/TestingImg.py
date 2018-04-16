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


def PostaInstagram(Titolo):
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
    font = ImageFont.truetype("GreatVibes-Regular.otf" , 150)
            
    parole = stringa.split(" ")
    frase = ""
    botta =0 
    while(num<len(parole)):
        frase += parole[num]+" "
        num +=1
        if num%8==0: #numero di parole stampate per riga
            
            #img = Image.open("0.jpg")
            draw = ImageDraw.Draw(img)
            print(frase+"\n")
            draw.text((30, 105+(130*botta)), frase,(255,255,255), font) 
            botta +=1
            img.save(str(0)+'.jpg')
            frase = "" 
if __name__ == '__main__':
    
    cits = get_titoli_from_reddit('quotes')
    print ("Elementi: "+ str(cits.__len__()))
    stampa(cits[0])
    PostaInstagram(cits[0] +" #quote")
    
        
        
        
        