import itertools
combos=0
alphabets=['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
keywords = [''.join(i) for i in itertools.product(alphabets, repeat = 50)]
print(len(keywords))
with open("list.txt","w") as f:
    f.write(keywords)
