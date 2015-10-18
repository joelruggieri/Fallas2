from attribute import Attribute
from category import Category

class Action:

	def __init__(self,name):
		self.category 	= None
		self.name = name
		self.decision 	= 	"N"
		self.attributes = []
		
		
	def setCategory(self,category):
		for attribute in category.getAttibutes():
			name = attribute.getName()
			anAtttribute = Attribute(name,"N")
			self.attributes.append(anAttribute)
    
   
   def setDesicion(self,decision):
        self.decision = desicion
        
	def defineValueForAttribute(self,attribute,value):
		for attribute in self.attributes:
			name = attribute.getName()
			if name == attribute:
			attribute.setValue(value)
        
       
	
