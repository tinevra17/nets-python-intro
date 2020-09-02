import re 

dictionary = {}

with open('declaration.txt','r') as file:    
    for line in file: 
        line = re.sub(r'[^\w\s]', '', line.lower()) 
        for word in line.split(): 
            if(word in dictionary):
                dictionary[word] += 1
            else:
                dictionary.update( {word : 1} )

sortedDict = dict( sorted(dictionary.items(), key=lambda x: x[0].lower()) )


f = open("key.txt", "w")

for keys,values in sortedDict.items():
    f.write('{} {}'.format(keys,values))
    f.write('\n')
f.close() 