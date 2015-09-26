class Rule:

	def __init__(self, name, attributes, evaluateScript):
		self.name 		= name
		self.attributes = attributes
		self.script 	= evaluateScript
		self.executed 	= False

	def canBeApplied(self, knowledge):
		if (self.executed):
			return False

		for attr in self.attributes:
			if (attr not in knowledge):
				return False
		return True


	def promiseOk(self, promise, knowledge):
		return self.script(self.attributes[0], self.attributes[1]) == promise

	def apply(self):
		self.executed = True
		return self.script(self.attributes[0], self.attributes[1])
