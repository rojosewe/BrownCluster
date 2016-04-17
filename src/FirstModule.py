'''
Created on Mar 1, 2013

@author: rojosewe
'''
# -*- coding: UTF-8 -*- 

def count1gram(token, dict1):
    if token in dict1:
        if len(token.strip()) > 0:
            dict1[token] = dict1[token] + 1
    else:
        dict1[token] = 1
    return dict1           
                        
def count2gram(token, dict2, sentence):
    if len(sentence) > 0:
        last = sentence[len(sentence) - 1]
        name = last + "|||" + token
        if len(token.strip()) > 0 and len(last.strip()) > 0:
            if name in dict2:
                dict2[name] = dict2[name] + 1
            else:
                dict2[name] = 1
    return dict2

def count3gram(token, dict3, sentence):
    if len(sentence) > 2:
        last = sentence[len(sentence) - 1]
        secondtolast = sentence[len(sentence) - 2]
        if len(token.strip()) > 0 and len(last.strip()) > 0 and len(secondtolast.strip()) > 0: 
            name = secondtolast + "|" + last + "|" + token
            if name in dict3:
                dict3[name] = dict3[name] + 1
            else:
                dict3[name] = 1
    return dict3

def count4gram(token, dict4, sentence):
    if len(sentence) > 3:
        last1 = sentence[len(sentence) - 1]
        last2 = sentence[len(sentence) - 2]
        last3 = sentence[len(sentence) - 3]
        if len(token.strip()) > 0 and len(last1.strip()) > 0 and len(last2.strip()) > 0 and len(last3.strip()) > 0:   
            name = last3 + "|" + last2 + "|" + last1 + "|" + token
            if name in dict4:
                dict4[name] = dict4[name] + 1
            else:
                dict4[name] = 1
    return dict4

def count5gram(token, dict5, sentence):
    if len(sentence) > 4:
        last1 = sentence[len(sentence) - 1]
        last2 = sentence[len(sentence) - 2]
        last3 = sentence[len(sentence) - 3]
        last4 = sentence[len(sentence) - 4]
        
        if len(token.strip()) > 0 and len(last1.strip()) > 0 and len(last2.strip()) > 0 and len(last3.strip()) > 0  and len(last4.strip()) > 0:   
            name = last4 + "|" + last3 + "|" + last2 + "|" + last1 + "|" + token
            if name in dict5:
                dict5[name] = dict5[name] + 1
            else:
                dict5[name] = 1
    return dict5

def printGram(dictio, title):  
    counter = 0
    one = 0
    two = 0
    more = 0
    
    bigv = [0,0,0,0,0,0]
    bigk = ["","","","","",""]
    
    for k in dictio.keys():
        counter = dictio[k]
        if counter == 1:
            one = one + 1
        elif counter == 2:
            two = two + 1
        else:
            more = more + 1
            
        endv = list(bigv)
        endk = list(bigk)
        n = 0
        done = False
        for i in range(6):
            if counter > bigv[i] and not done:
                endv = bigv[0:i] + [counter] + bigv[i:]
                endk = bigk[0:i] + [k] + bigk[i:]
                break  
        bigk = list(endk[:6])
        bigv = list(endv[:6])
    print title
    print "1="+str(one)
    print "2="+str(two)
    print "3>="+str(more)
    print "most repeated" 
    for i in range(6):
        print str(i)+"- " + bigk[i] + ": " + str(bigv[i])
    print ""

dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
dict5 = {}

f = open('/home/rojosewe/Documents/ANLP/en/en-clean-4M.txt', 'r')

sentence = []
co = 0
for line in f:
    tokensxline = line.split(" ")
    token = ""
    if len(tokensxline) == 4:
        token = tokensxline[0]
    else:
        sentence = []
        co = co + 1
        if co % 1000 == 0:
            print co
    # dict1 = count1gram(token, dict1)
    # dict2 = count2gram(token, dict2, sentence)
    # dict3 = count3gram(token, dict3, sentence)
    dict4 = count4gram(token, dict4, sentence)
    #dict5 = count5gram(token, dict5, sentence)
    sentence.append(token)

#printGram(dict1, "1-gram")
#dict1.clear()
#printGram(dict2, "2-gram")
#dict2.clear()
#printGram(dict3, "3-gram")
#dict3.clear()
printGram(dict4, "4-gram")
dict4.clear()
#printGram(dict5, "5-gram")
#dict5.clear()
        
f.close() 
