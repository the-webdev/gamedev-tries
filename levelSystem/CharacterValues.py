class CharacterValues:
	dict_additiveValues = {}
	dict_startValues = {}
	def setAdditiveValues(dict_arg):
		if type(dict_arg) == type({'key':'val'}):
			self.dict_additiveValues = dict_arg
		else:
			throw TypeError("FALSCHER TYP!")
	def setStartValues(dict_argg):
		if type(dict_arg) == type({'key':'val'}):
			self.dict_startValues = dict_argg
		else:
			throw TypeError("FALSCHER TYP!")
	