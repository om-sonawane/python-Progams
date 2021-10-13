def remove_and_split(string, world):
    newStr= string.replace(world,"")
    return newStr.strip()

this="   harry is good    "
n= remove_and_split(this,"harry")
print(n)
#print(this)

#print(this.strip())