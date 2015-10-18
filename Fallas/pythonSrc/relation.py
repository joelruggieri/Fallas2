class Relation(object):
    def __init__(self, item,relation):
        self.item = item
        self.relation = relation       
    def __str__(self):
        return str(self.item) + str(self.relation)
