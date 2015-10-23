from rule import Rule
from interfaz import Interfaz

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def backwardChaining(knowledge, rules, promise):
	
 	positiveRules = []
 	for rule in rules:
 		if rule.promiseOk(promise, knowledge):
 			positiveRules.append(rule)

 	if len(positiveRules) == 0:
 		return knowledge

 	if (not positiveRules[0].canBeApplied(knowledge)):
 		newKnowledge = backwardChaining(positiveRules[0].attributes, rules, promise)
 		for x in newKnowledge:
 			knowledge.append(x)
 	else:
 		knowledge.append(positiveRules[0].attributes[0])
 		knowledge.append(positiveRules[0].attributes[1])
 		return knowledge	


def ruleScript(attr1,attr2):
	if attr1 == attr2:
		return attr1
	
	if attr1 == "VF":
		if attr2 == "V":
			return "V"
		if attr2 == "N":
			return "V"
		if attr2 == "C":
			return "VD"
		if attr2 == "CD":
			return "VD"
		if attr2 == "VD":
			return "V"
		return "N"
	
	if attr1 == "V":
		if attr2 == "N":
			return "VD"
		if attr2 == "C":
			return "N"
		if attr2 == "CF":
			return "CD"					
		if attr2 == "CD":
			return "VD"					
		if attr2 == "VD":
			return "VD"					

	if attr1 == "CF":
		if attr2 == "C":
			return "C"
		if attr2 == "N":
			return "C"
		if attr2 == "V":
			return "CD"
		if attr2 == "VD":
			return "CD"
		if attr2 == "CD":
			return "C"

	if attr1 == "C":
		if attr2 == "N":
			return "CD"
		if attr2 == "VD":
			return "N"
		if attr2 == "CD":
			return "CD"

	return 	ruleScript(attr2, attr1)	

def chargeRules():
	rules = []
	possibleValues = ["VF", "V", "N", "C", "CF"]

	for attr1 in possibleValues:
		for attr2 in possibleValues:
			rule = Rule( attr1 + "-" + attr2, [attr1, attr2], ruleScript)
			rules.append(rule)

	return rules



rules = chargeRules()

knowledge = Interfaz([12, 15, 19, 14, 12.5, 13.6, 0.5]).translate()
#knowledge = ["VF", "VF", "VF", "VF", "VF", "VF"]
finalKnowledge = backwardChaining(knowledge, rules, "VF")
print "RESULT "
print finalKnowledge
