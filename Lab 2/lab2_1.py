dict={}
sentence = "Manipal Institute of Technology"
x=sentence.split()
for i in range(0, len(x)):
    dict.update({i: x[i]})
print(len(dict))


