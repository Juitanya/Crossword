crosswordwords=open('crosswordwords.txt')
words=crosswordwords.read().split()
allwords=[]
for i in words:
    if len(i)<=7:
        allwords.append(i)
words=allwords
x='hello'
print(x.upper())