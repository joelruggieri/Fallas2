from relation import Relation

class SemanticNetwork:
	
	def __init__(self):
		self.relations = {}  
	
	def add(self, item):
		self.relations.update({item:[]})
		
	def link(self, item1, item2, relation):
		self.relations[item1].append(Relation(item2, relation))
	
	def belongs(self, action, category):
		self.link(action,category,"belongs")
		#action.setCategory(category)
		
	def appertain(self, attribute, kind):
		self.link(attribute,kind,"belongs")
		#attribute.setkind(kind)
		
	
	def hasAttribute(self, category, attribute):
		self.link(category,attribute,"has attribute")
		#category.setAttribute(attribute)	
		
		
	def isAn(self, item1, item2):
		self.link(item1,item2,"is an")
		
	def isA(self, item1, item2):
		self.link(item1,item2,"is a")
		
	def __str__(self):
		return str(self.relations)
		
	def getRelations(self):
		return self.relations
		
