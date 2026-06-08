def algonex(text):
    emptydict={}
    for nisha in text:
        if nisha in emptydict:
            emptydict[nisha]+=1
        else:
            emptydict[nisha]=1
    return emptydict
print(algonex("ALGONEX"))
# 2ND QUESTION ANSWER 
def duplicatefinder(t):
    emptylist=[]
    dictionary={}
    for id in t:
        if id in dictionary:
            dictionary[id]+=1
            if id not in emptylist:
                emptylist.append(id)
        else:
            dictionary[id]=1
    return emptylist
print(duplicatefinder([101,101,102,102,103,103,104]))
# 3RD QUESTION ANSWER
employees=[
    ("john",50000),
    ("david",70000),
    ("ssmith",40000),
    ("alice",90000)
]
highest=max(employees)
print(highest)
lowest=min(employees)
print(lowest)
#average=sum(employees)
#print(average)
#4TH QUESTION 
print([i**2 for i in range(1,1001) if i%2==0])
#5TH QUESTION ANSWER
students=[
    ("john",85),
    ("david",92),
    ("ssmith",78),
    ("alice",95)
]
sortstudents=sorted(students,key=lambda x:x[1],reverse=True)
print(sortstudents)
#6TH QUESTION
def bankreport(transactions):
    totalcredit=0
    totaldebit=0
    for i in transactions:
        if amount>0:
            totalcredit=i
        else:
            totaldebit=i
    finalbalance=totalcredit-totaldebit
    return totalcredit,totaldebit,finalbalance
transactions=[1000,-200,500,-100,2000,-500]
#print(f"total credit={totalcredit}")
#print(f"total debit={totaldebit}")
#print(f"total balance={finalbalance}")
#7TH QUESTION ANSWER
numbers=[1,2,3,4,5,6,7,8,9,10]
#result=list(map(lambda x:x*2,filter( X:x%2==0,numbers))
#print(result)


