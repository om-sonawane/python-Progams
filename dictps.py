letter='''Dear <|Name|>,
Greeting from abc coding hourse. I AM happy to tell you about you selection

you are selected!

date:<|Date|>
'''
name= input ("Enter your Name")
name= input ("Enter Date\n")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)