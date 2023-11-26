import re 
s='hello how are 234 and 6578'
pat=input('enter any pattern:')
if re.search(pat,s):
	print('found')
else:
	print('not found')

