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
    
    while(((num<len(parole)%9)!=0)):
        frase += parole[num]+" "
        num +=1
        if num%10==0:
            print(frase+"\n")
            draw.text((30, 305+(130*num)), frase,(255,255,255), font) 
            frase = "" 
    img.save(str(num)+'.jpg')
if __name__ == '__main__':
    
    cits = get_titoli_from_reddit('quotes')
    print ("Elementi: "+ str(cits.__len__()))
    for k in cits:
        print(k+"\t DIO porco: "+str(len(k)) +"\n")
        stampa(k)
    
        
        
        
        