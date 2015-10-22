

class Attribute:

	def __init__(self,name):
		self.name 	= name
		self.value 	= 	"N"
		self.kind = None
    
   
	def setValue(self,value):
	   self.value = value
        
	def getName(self):
		return self.name
	   
	def setkind(self,kind):
		self.kind = kind
	
