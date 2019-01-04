import random
crosswordwords=open('crosswordwords.txt')
words=crosswordwords.read().split()
strwords=crosswordwords.read()
allwords=[] 
alphabets=[]
ans7=[]
lessans=[]
moreans=[]

for i in range (65,91):
    alphabets.append(chr(i))
for i in range (97,123):
    alphabets.append(chr(i))

def printerror():
    print('Error input !')
    exit()

def lowerall():
    for i in words:
        allwords.append(i.lower())

def wordinput():
    myhand=raw_input('Input your Alphabets : ')
    myhandlis=[]
    for i in myhand:
        if i not in alphabets:
            printerror()
        else:
            myhandlis.append(i)
    return myhandlis

def createwordssorted():
    wordssorted=[]
    for i in words:
        wordssorted.append(sorted(i))
    return wordssorted

def createwordsstrsorted():
    wordsstrsorted=[]
    for i in words:
        wordsstrsorted.append(''.join(sorted(i)))
    return wordsstrsorted

lowerall() 
words=allwords 
myhand=wordinput() 
myhandsorted=sorted(myhand)
myhandstrsorted=''.join(myhandsorted)
wordssorted=createwordssorted()
wordsstrsorted=createwordsstrsorted()

lis=[]
for i in myhandstrsorted:
    if i not in lis:
        lis.append(i)


def findbingowords():
    for i in wordssorted:
        if i==myhandsorted:
            ans7.append(words[wordssorted.index(i)])
            wordssorted[wordssorted.index(i)]=' '

def findotherwords():
    for i in range (len(wordsstrsorted)):   
        sign=True 
        for j in lis:
            if j in wordsstrsorted[i]:
                continue
            else:
                sign=False
                break       
        if sign == False:
            continue
        else:            
            if len(words[i])<10:
                moreans.append(words[i]) 
                wordsstrsorted[i]=' '

    for i in range (len(wordsstrsorted)):   
        sign=True 
        for j in range (len(wordsstrsorted[i])):
            if wordsstrsorted[i][j] in lis:
                continue
            else:
                sign=False
                break       
        if sign == False:
            continue
        else:
            if len(words[i])<10:
                lessans.append(words[i]) 
                wordsstrsorted[i]=' '

findbingowords()
findotherwords()

if len(moreans)>15:
    tmpmoreans=[]
    for i in range (15):
        tmpmoreans.append(moreans[random.randint(0,len(moreans)-1)])
    moreans=tmpmoreans

if len(lessans)>15:
    tmplessans=[]
    for i in range (15):
        tmplessans.append(lessans[random.randint(0,len(lessans)-1)])
    lessans=tmplessans

finalans7=[]
finalmoreans=[]
finallessans=[]
for i in ans7:
    a=i.upper()
    finalans7.append(a)
for i in moreans:
    a=i.upper()
    finalmoreans.append(a)
for i in lessans:
    a=i.upper()
    finallessans.append(a)

if len(finalans7)==0:
    print('Don\'t have bingo words.')
elif len(myhandsorted)==7:
    print('Bingo words !!! : '+str(finalans7))
else:
    print('Throw all these alphabets ! : '+str(finalans7))

if len(finalmoreans)==0:
    print('Don\'t have any more than 7 Alphabets words.')
else:
    print('May be bingo words ! : '+str(finalmoreans))

print('Other words : '+str(finallessans))












    
    




