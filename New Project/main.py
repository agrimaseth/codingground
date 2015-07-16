import string
import re

with open('Newfile.py', 'r') as f, open ('query.py','r') as q, open('out.txt', 'w') as out:
 
 read_query = q.read()
 query_list = [g.lower() for g in map(string.strip, re.split("(\W+)", read_query)) if len(g) > 0 and not re.match("\W",g)]
 
 read_data = f.read()
 tokens=[e.lower() for e in map(string.strip, re.split("(\W+)", read_data)) if len(e) > 0 and not re.match("\W",e)]
 
 for query in query_list:
    print query
    indices = (i for i,word in enumerate(tokens) if word==query)
    neighbors = []
    for ind in indices:
     neighbors.append(tokens[ind-3:ind]+tokens[ind+1:ind+4])
    for line in neighbors:
        strs="\n".join(str(x)+" "+ query + " l1" for x in line)
        out.write(strs+"\n")
      
    print neighbors
    
f.close()
q.close()
out.close()
#print out.closed

