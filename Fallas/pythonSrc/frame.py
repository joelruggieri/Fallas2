class Frame:

	# realValues [gcia_op, pe, roa, roe, bv, ep, plazo]
	def __init__(self, slots):
		self.slots 				= slots
		self.slotValues 		= [None]*self.slots.len
		self.isNeededProcedure	= [None]*self.slots.len
		self.isAddedProcedure	= [None]*self.slots.len
		self.isRemovedProcedure	= [None]*self.slots.len


	def defaultIsNeededProcedure(self, slotName):
		print slotName + " is needed and I dont exist. No accion Set"
		return null
	
	def defaultIsAddedProcedure(self, slotName):
		print slotName + " is added and already exist. No accion Set"
		return null

	def defaultIsRemovedProcedure(self, slotName):
		print slotName + " is removed. No accion Set"
		return null

	def getSlotValue(self, slotName):
		index = self.slots.indexOf(slotName)
		if(self.slotValues[index] != None):
			return self.slotValues[index]
		if ( self.isNeededProcedure[index] != None):
			return self.isNeededProcedure[index](slotName)
		return self.defaultIsNeededProcedure(slotName)

	def setSlotValue(self, slotName, value):
		index = self.slots.indexOf(slotName)
		if(self.slotValues[index] == None):
			if ( self.isAddedProcedure[index] != None):
				return self.isAddedProcedure[index](slotName, value)
			return self.defaultIsAddedProcedure(slotName)

		self.slotValues[index] = value
	
	def removeSlotValue(self, slotName):
		index = self.slots.indexOf(slotName)
		if(self.slotValues[index] != None):
			if ( self.isRemovedProcedure[index] != None):
				return self.isRemovedProcedure[index](slotName)
			return self.defaultIsRemovedProcedure(slotName);
