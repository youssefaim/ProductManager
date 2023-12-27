from composition import Composition
from produit import Produit
from elementaire import Elementaire
from compose import Compose
from collections import namedtuple ,defaultdict,deque

# Creating instances of Elementaire and Composition
TOMATO = Elementaire("TOMATO", "P001", 15)
EGG = Elementaire("EGG", "P002", 1.5)
co1 = Composition(TOMATO , 2)
co2 = Composition(EGG, 1.5)

# Creating an instance of Compose
BM = Compose("BM", "P003", 5 , 15 ,[co1, co2])



listeproduit = [TOMATO, EGG, BM]
def afficher(listeproduit) :
    for i in listeproduit :
        if type(i) == Elementaire : 
            print("le prix de", i.Getnom , "est :" , i.GetprixAchat)

        else : 
            prix = 0
            for e in i.Getliste :
                prix += e.Getproduit.GetprixAchat
            print("le prix de ", i.Getnom , "est :", prix)
    
afficher(listeproduit)
descrption = namedtuple("description",["produit", "details"] )
d1 = descrption(TOMATO.Getnom,TOMATO.__str__())
d2 = descrption(EGG.Getnom,EGG.__str__())
p1 = descrption(BM.Getnom,BM.__str__())

print("THe details of product is :", d1.details)
d1 = {}
d2 = {}
d3 = {}
listeDescription = defaultdict()

listeDescription[1] = d1
listeDescription[2] = d2
listeDescription[3] = d3  

DeqDescription = {}
DeqDescription = deque()

DeqDescription.append(d1)  
DeqDescription.append(d2)  
DeqDescription.append(d3)




