import os
print("Welcome to SILENT-AUCTION Programme")
count=1
data={}
bid_list=[]
while count>0:
    name=str(input("Enter your name:"))
    age=int(input("Enter your age:"))
    bid=int(input("Enter your bid:"))
    data[name]={"age":age,"bid":bid}
    user=str(input(("Any more bidders if yes type 'yes' or if no type 'no' :"))).lower()
    if user=="yes":
        os.system('cls')
        count+=1
    elif user=="no":
            count=0

for i in data:
    bid_list.append(data[i]["bid"])
    
maximum=max(bid_list) 

for i in data:
    if data[i]["bid"]==maximum:
        winner=str(i)
        print(f"Auction winner is {winner} with a bid {maximum}")
    else:
        pass    


               
         
                   
