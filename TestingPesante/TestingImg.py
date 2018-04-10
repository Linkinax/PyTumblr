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

def PostaInstagram():
    oInstagramAPI = InstagramAPI("unsaid.citations", "verdesmeraldo")
    oInstagramAPI.login()  # login

    photo_path = '/home/alex/Documenti/LOL/C0D3rPAzZ0/Baws/Al/PyTumblr_project/TestingPesante/0.jpg'
    caption = ":)"
    oInstagramAPI.uploadPhoto(photo_path, caption=caption)
if __name__ == '__main__':
    
    cits = get_titoli_from_reddit('quotes')
    print ("Elementi: "+ str(cits.__len__()))
    k =0
    
    for cit in cits:  
        if(len(cit)>44):
            s=40
            try:
                while(cit[s]!=   (' ') or ''):
                    s+=1
            except(IndexError):
                print("Hai beccato na quote sfigata zio")
            
            img = Image.open("sfondo_quotes4.jpg")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("GreatVibes-Regular.otf" , 150)
            draw.text((30, 435),cit[0:s],(255,255,255),font=font)#<---- Worka!
            draw.text((30, 595),cit[s:],(255,255,255),font=font)
            img.save(str(k)+'.jpg')
            k +=1
        else:
            img = Image.open("sfondo_quotes.jpg")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("GreatVibes-Regular.otf" , 72)
            draw.text((30, 475),cit,(0,0,0),font=font)#<---- Worka!
            img.save(str(k)+'.jpg')
            k +=1
    #PostaInstagram()
            
    
    pass