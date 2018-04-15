'''
Created on Apr 15, 2018

@author: alex
'''
def StampaDio(stringa, botta=36):
    es = "I used to have horrible cars that would always end up broken down on the highway. When I tried to flag someone down, nobody stopped. But if I pushed my own car, other drivers would get out and push with me. If you want help, help yourself - people like to see that."
    n=0
    botta = 34
    
    
    parole = es.split(" ")
    frase = ""
    
    print("\n")
    while(n<len(parole)):
        frase += parole[n]+" "
        n +=1
        if n%10==0:
            print("\n"+frase+"\n")
            frase = ""
        
    
    print(stringa)