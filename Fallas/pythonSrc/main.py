from semanticNetwork import SemanticNetwork
from action import Action
from category import Category
from attribute import Attribute
from fundamental import Fundamental
from technical import Technical
from kind import Kind

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
semantic_network.add(galicia)
semantic_network.add(patagonia)

semantic_network.add(banking_sector)

semantic_network.add(fundamental)
semantic_network.add(technical)


#creamos las relaciones
for attr in fundamental_attributes:
	anAttribute = Attribute(attr)
	semantic_network.add(anAttribute)
	semantic_network.appertain(anAttribute,fundamental)
	semantic_network.hasAttribute(banking_sector,anAttribute)
	
for attr1 in technical_attributes:
	anAttribute1 = Attribute(attr1)
	semantic_network.add(anAttribute1)
	semantic_network.appertain(anAttribute1,technical)
	semantic_network.hasAttribute(banking_sector,anAttribute1)
	
	
semantic_network.belongs(galicia,banking_sector)


semantic_network.belongs(patagonia,banking_sector)





 


