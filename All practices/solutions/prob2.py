input='Bangladesh is a reverine country'
s=input.split()
s.reverse()
output=[]
for w in s:
    output.append(w)
output=" ".join(output)
print(output)