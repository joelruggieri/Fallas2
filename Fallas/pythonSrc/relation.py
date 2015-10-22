class Relation(object):
    def __init__(self, item,relation):
        self.item = item
        self.relation = relation       
    
    def __str__(self):
        return  "relation: " + "'" + str(self.relation)+ "'" + " node: " + str(self.item)
    def getRelation(self):
		return self.relation
    def getItem(self):
		return self.item
	
