'''
Created on Aug 27, 2018

@author: alex
'''


if __name__ == '__main__':
    
    compagni = { }
    previousName="CULO"
    with open("boys.txt") as openObj:
        for line in openObj:
            
            if(line.__contains__("added") or line.__contains__("created") or line.__contains__("- bibliografia: citi il saggio") or line.__contains__("changed the subject") or line.__contains__("se volete stampare la tesina")):
                continue
            try:
                name = line.split("- ")[1].split(":")[0]
                mex = line.split("- ")[1].split(":")[1]
                if( not compagni.keys().__contains__(name)):
                    compagni[name] = [0,0]
                compagni.update( { name : [compagni[name][0]+1, compagni[name][1]+ len(mex)] })
                previousName = name
            except IndexError:
                compagni.update( { previousName : [compagni[previousName][0]+1, compagni[previousName][1]+ len(line)] })
                continue
            
    max_mex = 0
    max_char = 0
    k_scelto_m =""
    k_scelto_c =""
    for k in compagni.keys():
        if (max_mex< compagni[k][0]):
            max_mex = compagni[k][0]
            k_scelto_m = k
        if (max_char< compagni[k][1]):
            max_char = compagni[k][1]
            k_scelto_c = k
        print k +"\t\t"+"Numero messaggi:"+str(compagni[k][0])+"\t\t Numero char:"+ str(compagni[k][1])
    
    print("\n")
    print(k_scelto_m+ " ha scritto " + str(compagni[k_scelto_m][0])+" messaggi")
    print(k_scelto_c+ " ha scritto piu' di tutti con: " + str(compagni[k_scelto_c][1])+" caratteri")
        
        
  
    
    
    
    pass