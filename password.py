import string
import random
s=[]
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
len=int(input("Enter password length:"))
s.append(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)
pas=("".join(s[0:len]))
print(pas)