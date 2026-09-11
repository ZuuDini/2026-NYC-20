with open('my_file.txt', mode = 'r+') as fo:
print(fo.read(3)) # prints ‘How’
print(fo.read(6))  #prints ' Pytho' 
print(fo.read(6)) #printss 'n Hand'
print(fo.readline()) # prints 'How Python Handles Files?'
print(fo.read())	
print(fo.readlines())
