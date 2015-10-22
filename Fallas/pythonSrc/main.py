from semanticNetwork import SemanticNetwork
from action import Action
from category import Category
from attribute import Attribute
from fundamental import Fundamental
from technical import Technical
from kind import Kind
from relation import Relation

def profundidadPrimero(grafo,elementoInicial,relation, funcion, elementosRecorridos = []):	
	funcion(elementoInicial,relation)
	if relation.getItem() in elementosRecorridos:
		return
	
	elementosRecorridos.append(relation.getItem())
	for vecino in grafo.relations[relation.getItem()]:
		profundidadPrimero(grafo,relation.getItem(),vecino, funcion, elementosRecorridos)
         
def imprimir (origin,relation):
    if origin != None:
		print origin + " " + relation.getRelation() + " " + relation.getItem()


#definicion de atributos
fundamental_attributes = ["ganancia operativa","roe","roa"]
technical_attributes = ["macd"]

#definicion de categoria
banking_sector =  Category("Bancario")

#definicion de las acciones
galicia = Action("Galicia")
patagonia = Action("Patagonia")

#definicion de indicadores
fundamental = Fundamental(3)
technical = Technical(3)


# red semantica
semantic_network = SemanticNetwork()

#incorporamos los elementos
semantic_network.add(galicia.getName())
semantic_network.add(patagonia.getName())

semantic_network.add("Sector")
semantic_network.add(banking_sector.getName())
semantic_network.isA(banking_sector.getName(),"Sector")

semantic_network.add("fundamental")
semantic_network.add("technical")

semantic_network.add("Tipo de Indicador")
semantic_network.isA("fundamental","Tipo de Indicador")
semantic_network.isA("technical","Tipo de Indicador")


semantic_network.add("Atributo")
#creamos las relaciones
for attr in fundamental_attributes:
	anAttribute = Attribute(attr)
	semantic_network.add(anAttribute.getName())
	semantic_network.appertain(anAttribute.getName(),"fundamental")
	semantic_network.hasAttribute(banking_sector.getName(),anAttribute.getName())
	semantic_network.isAn(anAttribute.getName(),"Atributo")
	
for attr1 in technical_attributes:
	anAttribute1 = Attribute(attr1)
	semantic_network.add(anAttribute1.getName())
	semantic_network.appertain(anAttribute1.getName(),"technical")
	semantic_network.hasAttribute(banking_sector.getName(),anAttribute1.getName())
	semantic_network.isAn(anAttribute1.getName(),"Atributo")
	
semantic_network.add("Accion")
semantic_network.belongs("Accion","Sector")
semantic_network.belongs(galicia.getName(),banking_sector.getName())
semantic_network.isAn(galicia.getName(),"Accion")


semantic_network.belongs(patagonia.getName(),banking_sector.getName())
semantic_network.isAn(patagonia.getName(),"Accion")

#del semantic_network.getRelations()["Sector"]

for node in semantic_network.getRelations():
	#print "es una relacion " + relations
	profundidadPrimero(semantic_network,None,Relation(node,""),imprimir)



