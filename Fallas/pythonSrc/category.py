from attribute import Attribute

class Category:

	def __init__(self,name):
		self.name = name
		self.attributes = []

    
   
	def setAttribute(self,attribute):
		self.attributes.append(attribute)
   
	def getAttibutes(self):
		return self.attributes
		
	def getName(self):
		return self.name
        

        
