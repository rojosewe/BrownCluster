'''
Created on Mar 12, 2013

@author: rojosewe
'''

f = open('/home/rojosewe/Documents/ANLP/en/en-clean-1k.txt', 'r')
d = open('/home/rojosewe/Documents/ANLP/simp1k.txt', 'w')

sentence = ""
co = 0
for line in f:
    tokensxline = line.split(" ")
    token = tokensxline[0]
    if token.isspace():
        d.write("%s\n" % sentence)
        sentence = ""
        co = co + 1
        print co
    sentence = sentence + token + " " 
