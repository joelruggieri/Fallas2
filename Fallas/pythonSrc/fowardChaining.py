from rule import Rule

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def fowardChaining(knowledge, rules, objective):
	print objective
 	positiveRules = []
 	for rule in rules:
 		if rule.canBeApplied(knowledge):
 			positiveRules.append(rule)

 	if len(positiveRules) == 0:
	 	if (len(objective) == 1):
	 		return objective[0]
 		return knowledge

 			
 	objective = remove_values_from_list(objective, positiveRules[0].attributes[0])
 	objective = remove_values_from_list(objective, positiveRules[0].attributes[1])
 	knowledge.append(positiveRules[0].apply())
 	objective.append(positiveRules[0].apply())
 	
 	return fowardChaining(knowledge, rules, objective)	


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

# for x in rules:
# 	print x.name + " -------> " + x.apply()	

knowledge = ["VF", "VF", "C", "C", "C", "C"]
finalKnowledge = fowardChaining(knowledge, rules, knowledge)
print "RESULT "
print finalKnowledge
finalKnowledge = fowardChaining(finalKnowledge, rules, finalKnowledge)

print "RESULT "
print finalKnowledge