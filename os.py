myDict ={
    "fast":"in a quick manner",
     "harry":"A CODER",
     "marks":[1,2,5],
     "anotherdict": {'harry':'player'}
}

#print (myDict ['fast'])
#print (myDict ['harry'])
myDict['marks']= [45,78]
print(myDict['marks'])
print(myDict['anotherdict']['harry'])
#dictonary method
print(myDict.keys())#print keys of the dictonary
print(myDict.values())
print(myDict.items())
updateDict={
    "lovish:friend"
}
myDict.update(updateDict)
print(myDict)