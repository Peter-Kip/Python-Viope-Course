def testme(userinput):
	if len(userinput) < 6 or userinput.isdigit():
		return False
	elif len(userinput) < 6 or userinput.isalpha():
		return False
	else:
		return True 
