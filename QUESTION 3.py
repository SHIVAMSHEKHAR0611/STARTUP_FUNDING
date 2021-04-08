"""
After re-analysing the dataset you found out that some investors have invested in the 
same startup at different number of funding rounds. So before finalising the previous 
list, you want to improvise it by finding the top 5 investors who have invested in 
different number of startups. This list will be more helpful than your previous list 
in finding the investment for your friend startup. Find the top 5 investors who have 
invested maximum number of times in different companies. That means, if one investor
has invested multiple times in one startup, count one for that company. 
There are many errors in startup names. Ignore correcting all, just handle the important ones
- Ola, Flipkart, Oyo and Paytm.
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
startup = pd.read_csv("startup_funding.csv")
df = startup.copy()

# dropping rows having Investors and startup name as nan..
df.dropna(subset = ["StartupName","InvestorsName"],inplace = True)  


# replacing the wrong word with the correct word.. ex: OYO as Oyo etc..
df["StartupName"].replace("Flipkart.com","Flipkart",inplace = True)  
df["StartupName"].replace("Ola Cabs","Ola",inplace = True)
df["StartupName"].replace("Olacabs","Ola",inplace = True)
df["StartupName"].replace("Oyorooms","Oyo",inplace = True)
df["StartupName"].replace("OyoRooms","Oyo",inplace = True)
df["StartupName"].replace("OYO Rooms","Oyo",inplace = True)
df["StartupName"].replace("Oyo Rooms","Oyo",inplace = True)
df["StartupName"].replace("Paytm Marketplace","Paytm",inplace = True)


# firstly created a dictionary for each investor names and maintained a set to counter duplicity
# meaning that each key (investor's name) having a value set (names of stratup's in which they invested)
# set is taken as a value to avoid count of multiple investment in a single startup by an investor
# in the set , there are startup names in which investor's had already invested
# in case there are multiple investors for a single startup so here used split function to split that 
# and traversed through each name separately as asked in the question. 

dic = {}
for i in df.index:
    e = df["InvestorsName"][i].strip()
    if "," in e:
        for j in e.strip().split(','):
            if j.strip() in dic:
                dic[j.strip()].add(df["StartupName"][i].strip())
            else:
                s = set()
                dic[j.strip()] = s
                dic[j.strip()].add(df["StartupName"][i].strip())
    else:
        el = e.strip()
        if el in dic: 
            dic[el].add(df["StartupName"][i].strip())
        else:
            s = set()
            dic[el] = s
            dic[el].add(df["StartupName"][i].strip())


# created a dictionary where key is investor's name and value is count of startup's in which they had invested..
d1 = {}  
for i in dic:
    if i == "":
        continue
    d1[i] = len(dic[i])
    
# sorting the keys according to there values in descending order..and taking the top 5 investors from the group    
d2 = sorted(d1, key=d1.get , reverse=True)[0:5]  
for i in d2:
    print(i , d1[i])


#----------- PLOTTING GRAPH -----------#



# getting values and investors name for plotting graph
val = [] 
inv = []
for keys , values in d1.items() :
    for i in range(5):
        if keys == d2[i]:
            inv.append(keys)
            val.append(values)

# formatting the graph
val = (np.array(val))*10
plt.scatter(inv , val/10 , s = val/5 , c=val  )
plt.plot(inv,val/10)
plt.title('Top Investors in Different Companies')
plt.xlabel("Investors", fontsize=16)   # labels of x-axis
plt.ylabel("Investments in Number of Startups", fontsize=16)  # labels of y_axis
plt.xticks(rotation = 0) # rotating names in x-axis
for i in range(len(inv)):
    a = str(inv[i]) 
    y = int(val[i])
    plt.text(a , y , val[i])
plt.show()
