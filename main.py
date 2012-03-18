# coding: UTF-8
from levelSystem import CharacterLvl, CharacterValues
#Variablen
charVals = CharacterValues.CharacterValues()


#Werte für Charater-Entwicklung definieren
additiveVal = {
	'HEALTH': 5.25,
	'AD': 3.75,
	'AP': 4.23,
	'MRES': 3.542,
	'ARMOR': 7.8
}
startVal = {
	'HEALTH': 20,
	'AD': 4,
	'AP': 1.5,
	'MRES': 5.4,
	'ARMOR': 7.8
}

#Werte für Charater-Entwicklung festlegen
charVals.setStartValues(startVal)
charVals.setAdditiveValues(additiveVal)

#Levels Einbinden
charLvl = CharacterLvl.CharacterLvl(charVals)

#Level-Statistiken von 1 bis 20 ausgeben lassen
for i in range(1,20):
	print 'Stats bei LVL: '+(str)(i)
	print charLvl.calculate(i)