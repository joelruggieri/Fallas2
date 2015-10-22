from kind import Kind

class Fundamental(Kind):

	def __init__(self,term):
		Kind.__init__(self,term)
		if term <= 2:
			self.weighting = 1
		else:
			self.weighting = 1.5
	

    
   
   
