#union

#syntax:variable.union(variable)

a={1,2,3,4}
b={5,2,7,8}
print(a.union(b))

#intersection

#Syntax:variable.intersection(variable)

a={1,2,3,4}
b={5,2,7,8}
print(a.intersection(b))


#intersection update

#Syntax:set1.intersection.update(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint

#syntax:set1.isdisjoint(set2)

a={'a'}
b={'d'}
print(a.isdisjoint(b))

a={'a'}
b={'a'}
print(a.isdisjoint(b))

#difference

#syntax:set1.difference(set2)

a={'Navya','Rajesh','Mahalya','Aravind'}
b={'Navya','Aravind'}
print(a.difference(b))

#symmetric

#syntax:set1.symmetric difference(set2)

a={'Navya','Rajesh','Mahalya','Aravind'}
b={'Rajesh','Mahalya'}
print(a.symmetric_difference(b))

#symmetric difference update

#syntax:set1.symmetric difference update(set2)

a={'Navya','Rajesh','Mahalya','Aravind'}
b={'Rajesh','Mahalya'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset

#syntax:set1.issubset(set2)

a={'Navya','Rajesh','Mahalya','Aravind'}
b={'Rajesh','Mahalya'}
print(a.issubset(b))

a={'Navya','Rajesh','Mahalya','Aravind'}
b={'Rajesh','Mahalya','Navya','Aravind'}
print(a.issubset(b))

#issuperset

#syntax:set1.issuperset(set2)
a={'Navya','Rajesh','Mahalya','Aravind'}
b={'Rajesh'}
print(a.issuperset(b))
