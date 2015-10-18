from relation import Relation

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
		link(semantickNetwork,action,category,"belongs")
	
	def hasAttribute(self,category,attribute):
		link(semantickNetwork,category,attribute,"hasAttribute")
