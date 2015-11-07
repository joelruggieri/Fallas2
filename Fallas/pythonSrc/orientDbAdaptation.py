import pyorient

client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "root")
cluster_info = client.db_open( "semantic_network", "root", "root" )

print("se crean los atributos:")

client.command("insert into Attribute ( 'name','value') values( 'ganancia operativa','N')")
client.command("insert into Attribute ( 'name','value') values( 'roe','N')")
client.command("insert into Attribute ( 'name','value') values( 'roa','N')")
client.command("insert into Attribute ( 'name','value') values( 'macd','N')")

attributes = client.command("select from Attribute")
for anAttribute in attributes:
    print(anAttribute.name)
    
print("")    
print("se crean la categoria:")

client.command("insert into Category ('name') values('Bancario')")

categories = client.command("select from Category")
for aCategory in categories:
    print(aCategory.name)

print("")
print("se crean las acciones:")

client.command("insert into Action ('name','decision') values( 'Galicia','N')")
client.command("insert into Action ('name','decision') values( 'Patagonia','N')")

actions = client.command("select from Action")
for anAction in actions:
    print( anAction.name)

print("")
print("se crean los indicadores:")

client.command("insert into Indicator ('name','terms','long_term_weighting','short_term_weighting') values( 'Fundamental','3','1.5','1')")
client.command("insert into Indicator ('name','terms','long_term_weighting','short_term_weighting') values( 'Technical','3','1','1.5')")

indicators = client.command("select from Indicator")
for indicator in indicators:
    print( indicator.name)
    
    
### creamos la arista appertain
client.command('create class Appertain extends E')

print("")
print("relacionamos los attributos con los indicadores")
appertain_edges = client.command(
    "create edge Appertain from ("
    "select from Attribute where name = 'ganancia operativa'"
    ") to ("
    "select from Indicator where name = 'Fundamental'"
    ")"
)

appertain_edges = client.command(
    "create edge Appertain from ("
    "select from Attribute where name = 'roe'"
    ") to ("
    "select from Indicator where name = 'Fundamental'"
    ")"
)

appertain_edges = client.command(
    "create edge Appertain from ("
    "select from Attribute where name = 'roa'"
    ") to ("
    "select from Indicator where name = 'Fundamental'"
    ")"
)

appertain_edges = client.command(
    "create edge Appertain from ("
    "select from Attribute where name = 'macd'"
    ") to ("
    "select from Indicator where name = 'Technical'"
    ")"
)

### obtenemos todos los indicadores fundamentales
print("")
print("indicadores fundamentales:")
fundamental_attributes = client.command("select expand( in( Appertain )) from Indicator where name = 'Fundamental'")
for anAttribute in fundamental_attributes:
    print(anAttribute.name)
    
### obtenemos todos los indicadores tecnicos
print("")
print("indicadores tecnicos:")
fundamental_attributes = client.command("select expand( in( Appertain )) from Indicator where name = 'Technical'")
for anAttribute in fundamental_attributes:
    print(anAttribute.name)
   
### creamos la arista hasAttribute
client.command('create class HasAttribute extends E')

print("")
print("relacionamos el sector bancario con los attributos")
hasAnAttribute_edges = client.command(
    "create edge HasAttribute from ("
    "select from Category"
    ") to ("
    "select from Attribute"
    ")"
)

### obtenemos todos los indicadores tecnicos
print("")
print("atributos del sector Bancario")
category_attributes = client.command("select expand( out( HasAttribute )) from Category where name = 'Bancario'")
for category_attribute in category_attributes:
    print(category_attribute.name + " que es un indicador de tipo:")
    indicators_type = client.command("select expand( out( Appertain )) from Attribute where name = '"+ category_attribute.name +"'")
    for indicator_type in indicators_type:
		print(indicator_type.name)
    
    
### creamos la arista Belongs
client.command('create class Belongs extends E')

print("")
print("relacionamos las acciones con el sector Bancario")
belongs_edges = client.command(
    "create edge Belongs from ("
    "select from Action"
    ") to ("
    "select from Category where name = 'Bancario'"
    ")"
)

### obtenemos las acciones del sector bancario
print("")
print("acciones que pertenecen al sector bancario:")
actions = client.command("select expand( in( Belongs )) from Category where name = 'Bancario'")
for action in actions:
    print(action.name)

client.command('delete vertex Attribute')
client.command('delete vertex Category')
client.command('delete vertex Action')
client.command('delete vertex Indicator')


client.command('drop class Appertain')
client.command('drop class HasAttribute')
client.command('drop class Belongs')


