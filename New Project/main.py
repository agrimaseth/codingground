import string
import re
import nltk
with open('Newfile.py', 'r') as f, open('out.txt', 'w') as out:
 read_data = f.read()
 tokens=[e.lower() for e in map(string.strip, re.split("(\W+)", read_data)) if len(e) > 0 and not re.match("\W",e)]
 indices = (i for i,word in enumerate(tokens) if word=="place")
 neighbors = []
 for ind in indices:
  neighbors.append(tokens[ind-3:ind]+tokens[ind+1:ind+4])
 for line in neighbors:
        strs="\n".join(str(x)+" place" + "l1" for x in line)
        out.write(strs+"\n")
      
print neighbors
f.close()
out.close()
#print out.closed
print f.closed
