s=input('Enter the string')
s=s.replace('a','2')
s=s.replace('e','4')
s=s.replace('i','6')
s=s.replace('o','8')
s=s.replace('u','10')
s=s.replace('A','2')
s=s.replace('E','4')
s=s.replace('I','6')
s=s.replace('O','8')
s=s.replace('U','10')
l=len(s)//2
s1=s[:l]
s2=s[l:].upper()
print(s1+s2)
