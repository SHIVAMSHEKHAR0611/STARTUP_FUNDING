"""
Even after putting so much effort in finding the probable investors, 
it didn't turn out to be helpful for your friend. So you went to your 
investor friend to understand the situation better and your investor friend 
explained to you about the different Investment Types and their features. 
This new information will be helpful in finding the right investor. Since your friend 
startup is at an early stage startup, the best-suited investment type would be - 
Seed Funding and Crowdfunding. Find the top 5 investors who have invested in a 
different number of startups and their investment type is Crowdfunding or Seed Funding. 
Correct spelling of investment types are - "Private Equity", "Seed Funding", 
"Debt Funding", and "Crowd Funding". Keep an eye for any spelling mistake. 
You can find this by printing unique values from this column. 
There are many errors in startup names. Ignore correcting all, just handle the important ones 
- Ola, Flipkart, Oyo and Paytm.
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
startup = pd.read_csv("startup_funding.csv")
df = startup.copy()

# removing row's having nan's in Investors name column..
df.dropna(subset = ["InvestorsName"],inplace = True) 

# replacing the wrong word with the correct word.. ex: OYO as Oyo etc..
df["StartupName"].replace("Flipkart.com","Flipkart",inplace = True)  
df["StartupName"].replace("Ola Cabs","Ola",inplace = True)
df["StartupName"].replace("Olacabs","Ola",inplace = True)
df["StartupName"].replace("Oyorooms","Oyo",inplace = True)
df["StartupName"].replace("OyoRooms","Oyo",inplace = True)
df["StartupName"].replace("OYO Rooms","Oyo",inplace = True)
df["StartupName"].replace("Oyo Rooms","Oyo",inplace = True)
df["StartupName"].replace("Paytm Marketplace","Paytm",inplace = True)


# Checking and correcting spelling checks of investment types
df.InvestmentType.loc[df.InvestmentType == 'Crowd funding'] = 'Crowd Funding'
df.InvestmentType.loc[df.InvestmentType == 'PrivateEquity'] = 'Private Equity'
df.InvestmentType.loc[df.InvestmentType == 'SeedFunding'] = 'Seed Funding'


# replacing the undisclosed investors name by null values ..
df["InvestorsName"].replace("Undisclosed Investors","",inplace = True) 
df["InvestorsName"].replace("Undisclosed investors","",inplace = True)


# keeping only those rows having investment type seed funding and crowd funding..
df = df[(df["InvestmentType"] == "Seed Funding") | (df["InvestmentType"] == "Crowd Funding")]  


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
plt.title('Seed / Crowd Investors')
plt.xlabel("Investors", fontsize=16)   # labels of x-axis
plt.ylabel("Number of Startups With Seed and Crowd Fundings", fontsize=13)  # labels of y_axis
plt.xticks(rotation = 0) # rotating names in x-axis
for i in range(len(inv)):
    a = str(inv[i]) 
    y = int(val[i])
    plt.text(a , y , val[i])
plt.show()




"""
# creating a dictionary to maintain the number of times the investors name appeared...
d = {}  

# traversing through the investor names..to see the number of times the names appeared..
# if it contains multiple names ..then spliting it ..and traversing through each names separately..
for i in df["InvestorsName"].values:  
    if "," in i:  
        for j in i.strip().split(','):
            d[j.strip()] = d.get(j.strip(),0) + 1
    else:
        d[i.strip()] = d.get(i.strip(),0) + 1

# deleting the NULL key from dictionary        
del d[""]
# sorting the keys in reverse order(descending to aescending) according to the values...
d1 = sorted(d, key=d.get , reverse=True)[0:5]  

# printing the top 5 investors...funded maximum number of times...
for i in d1:  
    print(i)


#----------- PLOTTING GRAPH -----------#



# getting values and investors name for plotting graph
val = [] 
inv = []
for keys , values in d.items() :
    for i in range(5):
        if keys == d1[i]:
            inv.append(keys)
            val.append(values)

# formatting the graph
val = (np.array(val))*10
plt.scatter(inv , val/10 , s = val/5 , c=val  )
plt.plot(inv,val/10)
plt.title('Seed / Crowd Investors')
plt.xlabel("Investors", fontsize=16)   # labels of x-axis
plt.ylabel("Number of Startups With Seed and Crowd Fundings", fontsize=13)  # labels of y_axis
plt.xticks(rotation = 0) # rotating names in x-axis
plt.show()

"""