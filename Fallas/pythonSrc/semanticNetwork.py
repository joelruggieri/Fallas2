from relation import Relation
from action import Action
from category import Category
from attribute import Attribute

class SemanticNetwork(object):
    def __init__(self):
        self.relations = {}
    def __str__(self):
        return str(self.relations)
 
	def add(self, item):
		grafo.relations.update({item:[]})

	def link(self,item1,item2,relation):
		self.relations[item1].append(Relation(item2, relation))
    
	def belongs(self,action,category):
		link(self,action,category,"belongs")
		action.setCategory(category)
		
	
	def hasAttribute(self,category,attribute):
		link(self,category,attribute,"has attribute")
		category.setAttribute(attribute)	
		
		
	def isAn(self,item1,item2):
		link(item1,item2,"is an")
		
	def isA(self,item1,item2):
		link(item1,item2,"is a")
