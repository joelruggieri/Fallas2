class Frame:

	# realValues [gcia_op, pe, roa, roe, bv, ep, plazo]
	def __init__(self, slots):
		self.slots 				= slots
		self.slotValues 		= [None]*len(self.slots)
		self.isNeededProcedure	= [None]*len(self.slots)
		self.isAddedProcedure	= [None]*len(self.slots)
		self.isRemovedProcedure	= [None]*len(self.slots)


	def defaultIsNeededProcedure(self, slotName, value):
		print slotName + " is needed and It doesnt exist. No accion Set"
		return None
	
	def defaultIsAddedProcedure(self, slotName):
		print slotName + " is added and already exist. No accion Set"
		return None

	def defaultIsRemovedProcedure(self, slotName):
		print slotName + " is removed. No accion Set"
		return None

	def getSlotValue(self, slotName):
		index = self.slots.index(slotName)
		if(self.slotValues[index] != None):
			return self.slotValues[index]
		if ( self.isNeededProcedure[index] != None):
			return self.isNeededProcedure[index](slotName, self.slotValues[index])
		return self.defaultIsNeededProcedure(slotName, self.slotValues[index])

	def setSlotValue(self, slotName, value):
		index = self.slots.index(slotName)
		if(self.slotValues[index] == None):
			if ( self.isAddedProcedure[index] != None):
				return self.isAddedProcedure[index](self.slotValues, index, value)
			return self.defaultIsAddedProcedure(slotName)

		self.slotValues[index] = value
	
	def removeSlotValue(self, slotName):
		index = self.slots.index(slotName)
		if(self.slotValues[index] != None):
			if ( self.isRemovedProcedure[index] != None):
				return self.isRemovedProcedure[index](self.slotValues, index)
			return self.defaultIsRemovedProcedure(slotName);
