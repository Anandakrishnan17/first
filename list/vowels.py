sen="pythonDjango"
vowels=[]
nonvowels=[]
for i in sen:
    if i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u':
        vowels.append(i)
    else:
        nonvowels.append(i)
print("Vowels",vowels)
print("Non Vowels",nonvowels)            