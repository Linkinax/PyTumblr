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

<<<<<<< HEAD
def PostaInstagram(Titolo):
    user = "unsaid.citations"
    passw= raw_input("Passowrd: ")
    oInstagramAPI = InstagramAPI(user, passw)
    oInstagramAPI.login()  # login

    photo_path = '/home/alex/Documenti/LOL/C0D3rPAzZ0/Baws/Al/PyTumblr_project/TestingPesante/0.jpg'
    caption = Titolo
    oInstagramAPI.uploadPhoto(photo_path, caption=caption)
def stampa(stringa):
    k =1
    num_img =0
    first_space=0
    
    img = Image.open("sfondo_quotes4.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("GreatVibes-Regular.otf" , 150)
            
    while(first_space<len(stringa)):
        first_space=40*k
        if(first_space < len(stringa)): 
            try:
                while(first_space*k<len (stringa)):
                    if(stringa[first_space]!=  ( (' ') or '')):
                        first_space = first_space*k + 1 #becco il primo spazio per andare a capo
                    else:
                        break
            except(IndexError):
                print("Hai beccato na quote sfigata zio")
            draw.text((30, 305+(130*k)),stringa[(k-1)*first_space:first_space*k],(255,255,255),font=font)#<---- Worka!
            print(str(k) +'\t')

            k +=1
            num_img +=1
            
        else:
            
            draw.text((30, 435*k),stringa,(255,255,255),font=font)#<---- Worka!
            
            k +=1
            num_img +=1
    img.save(str(num_img)+'.jpg')
if __name__ == '__main__':
    
    cits = get_titoli_from_reddit('quotes')
    print ("Elementi: "+ str(cits.__len__()))
    for k in cits:
        stampa(k)
=======
def PostaInstagram():
    oInstagramAPI = InstagramAPI("unsaid.citations", "verdesmeraldo")
    oInstagramAPI.login()  # login

    photo_path = '/home/alex/Documenti/LOL/C0D3rPAzZ0/Baws/Al/PyTumblr_project/TestingPesante/0.jpg'
    caption = ":)"
    oInstagramAPI.uploadPhoto(photo_path, caption=caption)
if __name__ == '__main__':
    
    cits = get_titoli_from_reddit('quotes')
    print ("Elementi: "+ str(cits.__len__()))
    k =1
    
    for cit in cits:  
        if(len(cit)>44):#per le cazzo di quotes kilometiche
            first_space=40
            if(first_space * k < len(cit)): 
                try:
                    while(cit[first_space*k]!=   (' ') or ''):
                        first_space = first_space*k + 1 #becco il primo spazio per andare a capo
                except(IndexError):
                    print("Hai beccato na quote sfigata zio")
                img = Image.open("sfondo_quotes4.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("GreatVibes-Regular.otf" , 150)
                draw.text((30, 435),cit[(k-1)*first_space:first_space*k],(255,255,255),font=font)#<---- Worka!
                draw.text((30, 595),cit[first_space*k:],(255,255,255),font=font)
                img.save(str(k)+'.jpg')
                k +=1
        else:
            img = Image.open("sfondo_quotes.jpg")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("GreatVibes-Regular.otf" , 72)
            draw.text((30, 475),cit,(0,0,0),font=font)#<---- Worka!
            img.save(str(k)+'.jpg')
            k +=1
>>>>>>> b02b1e022a9ea2f25d2727b23dfd30df6e513707
    #PostaInstagram()
            
    
    pass