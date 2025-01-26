#zip the lidt
d1 = {'a','b','c'}
d2 = {1,2,3}
d3 = list(zip(d1, d2))
print(d3)

l1 = [1,2,3,4]
l2 = [40,30,20,10]

for a,b in zip(l1, l2[::-1]):
    print(a,b)
