def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None
		
lex = {'direction': ['north', 'south', 'east', 'west', 'down', 'up', 
						'left', 'right', 'back'],
		   'verb': ['go', 'stop', 'kill', 'eat'],
		   'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
		   'noun': ['door', 'bear', 'princess', 'cabinet']
}
		   		   
		   	

def scan(str):
	#scan user input and return list of tuples of (TOKEN, WORD) pairing
	
	result = []
	words = str.split()
	for word in words:
		not_in_lex = True
		for key in lex.keys():
			if word.lower() in lex[key]:
				temp_tup = (key, word)
				not_in_lex = False
				break
			else:
				pass
				
		if not_in_lex:
			if convert_number(word) == None:
				temp_tup = ('error', word)
			else:
				temp_tup = ('number', convert_number(word))
				
		result.append(temp_tup)
	
	return result
	
#scan("bear ISS 33")