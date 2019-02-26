'''
Created on Aug 26, 2018

@author: alex
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from __builtin__ import raw_input
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':
    
    browser = webdriver.Firefox(executable_path='/home/alex/Documents/Coder/geckodriver')
    browser.refresh()
    browser.get('https://web.whatsapp.com/')
    input = raw_input("Hvae you finished to prepare it ?")
    temp =0;
    print("Imma scroll\n")
    while temp<300:
        if temp%20 ==0:
            print(temp)
        browser.execute_script("document.getElementsByClassName('_2nmDZ')[0].scrollTop = -750;")
        sleep(1)
        temp +=1
        
    print("Menghia oh!\n")
    mexs = browser.find_elements_by_class_name("vW7d1")
    print("NUmero mex analizzati: " +str(len(mexs)))
    #{"nome" : [numMex, charTot] }
    stronzi_UG = { }
    for i in range(0,len(mexs)):
        try:
            membro_mex = BeautifulSoup(mexs[i].get_attribute('innerHTML'), "lxml")
            #print(membro_mex)
            membro = membro_mex.find_all("span", attrs={'class': "_2a1Yw _1OmDL"})
            if(len(membro)>0):
                #print("found:\t "+ str(membro[0].getText()))
                if(not stronzi_UG.keys().__contains__(membro[0].getText())):
                    stronzi_UG[membro[0].getText()] = [0,0]
                mexText = membro_mex.find_all("span", attrs= {"class": "selectable-text"})
                if(len( mexText)>0):
                    #print mexText[0].getText()
                    stronzi_UG.update( {membro[0].getText() : [ stronzi_UG[membro[0].getText()][0]+1  , stronzi_UG[membro[0].getText()][1]+ len(mexText[0].getText()) ]})
                else:
                    pass
            else:
                pass
        except NoSuchElementException:
            print("Infiltrato?!  ")
            inp = raw_input("debs")
    
    print("\n Vediamo i risultati \n")
    for k in stronzi_UG.keys():
        print(k +"\t Numero di messaggi:"+ str(stronzi_UG[k][0])+"\t\t\t"+str(stronzi_UG[k][1])+" char inviati")
    print("Finished!")
    #print("Riccardo gay capo degli ebrei")
    browser.close()