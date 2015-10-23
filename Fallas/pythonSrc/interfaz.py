class Interfaz:

	# realValues [gcia_op, pe, roa, roe, bv, ep, plazo]
	def __init__(self, realValues):
		self.realValues 		= realValues
		self.translateValues 	= []

	def translate(self):
		self.translateValues.append( self.translateGciaOp())
		self.translateValues.append( self.translatePe())
		self.translateValues.append( self.translateRoa())
		self.translateValues.append( self.translateRoe())
		self.translateValues.append( self.translateBv())
		self.translateValues.append( self.translateEp())
		return self.translateValues


	def translateGciaOp(self):

		if self.realValues[0] < 15.2:
			return "VF"
		if self.realValues[0] < 22.5:
			return "V"
		if self.realValues[0] < 29.3:	
			return "N"
		if self.realValues[0] < 33.1:	
			return "C"
		return "CF"	

	def translatePe(self):
		if self.realValues[1] < 8.5:
			return "CF"
		if self.realValues[1] < 12.1:
			return "C"
		if self.realValues[1] < 16.7:	
			return "N"
		if self.realValues[1] < 19:	
			return "V"
		return "VF"

	def translateRoa(self):
		
		if self.realValues[0] < 0.7:
			return "VF"
		if self.realValues[0] < 1.25:
			return "V"
		if self.realValues[0] < 2.5:	
			return "N"
		if self.realValues[0] < 4:	
			return "C"
		return "CF"	

	def translateRoe(self):
		if self.realValues[0] < 15:
			return "VF"
		if self.realValues[0] < 21:
			return "V"
		if self.realValues[0] < 32:	
			return "N"
		if self.realValues[0] < 50:	
			return "C"
		return "CF"	
	def translateBv(self):
		if self.realValues[1] < 3.3:
			return "CF"
		if self.realValues[1] < 9:
			return "C"
		if self.realValues[1] < 18:	
			return "N"
		if self.realValues[1] < 22:	
			return "V"
		return "VF"

	def translateEp(self):
		if self.realValues[1] < 3.8:
			return "CF"
		if self.realValues[1] < 5.4:
			return "C"
		if self.realValues[1] < 13:	
			return "N"
		if self.realValues[1] < 18:	
			return "V"
		return "VF"