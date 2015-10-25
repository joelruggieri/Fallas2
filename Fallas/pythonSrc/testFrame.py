from frame import Frame


def getCommon(tipo, valor):
	return valor


def setCommon(obj, index, valor):
	obj[index] = valor

def removeCommon(obj, index):
	obj[index] = None


slots = ["gcia_op", "pe", "roa", "roe", "bv", "ep", "plazo"]
frame  = Frame(slots)
value = frame.getSlotValue("gcia_op")
print value

frame.isNeededProcedure[0] = getCommon

value = frame.getSlotValue("gcia_op")
print value

value = frame.setSlotValue("gcia_op", 0.5)
print value

frame.isAddedProcedure[0] = setCommon

value = frame.setSlotValue("gcia_op", 0.5)
print value

value = frame.getSlotValue("gcia_op")
print value


value = frame.removeSlotValue("gcia_op")
print value

frame.isRemovedProcedure[0] = removeCommon


value = frame.removeSlotValue("gcia_op")
print value

value = frame.getSlotValue("gcia_op")
print value