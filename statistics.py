import requests as rq
import matplotlib.pyplot as plt
import statistics
a=input("Enter your Codeforces Handle: ")
res1=rq.get("https://codeforces.com/api/user.rating?handle={}".format(a))
temp= res1.json()['result']
ratings=[]
change=[]
for i in temp:
    ratings.append( i['rank'])
    change.append( i['newRating']-i['oldRating'])
x=[]
for i in range( len(temp)):
    x.append(i+1)
plt.bar(x,ratings)
print("Handle's Average Ranking is:{} ".format( statistics.mean(ratings)))
print("Handle's Standard Devitation is:{}".format( statistics.pstdev(ratings)))
plt.xlabel("Contest Number")
plt.ylabel("Ranking")
plt.show()

barlist=plt.bar(x,change)
for i in range(len(x)):
    if( change[i]>0):
        barlist[i].set_color('g')
    elif( change[i]<0):
        barlist[i].set_color('r')
    else:
        barlist[i].set_color('b')
print("Handle's Average Rating Change is:{}".format( statistics.mean(change)))
print("Handle's Standard Devitation is:{}".format( statistics.pstdev(change)))
plt.xlabel("Contest Number")
plt.ylabel("Rating Change")
plt.show()