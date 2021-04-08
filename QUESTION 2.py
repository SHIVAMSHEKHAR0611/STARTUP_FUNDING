"""
Even after trying for so many times, your friend’s startup could not find the investment. 
So you decided to take this matter in your hand and try to find the list of investors who 
probably can invest in your friend’s startup. Your list will increase the chance of your 
friend startup getting some initial investment by contacting these investors. 
Find the top 5 investors who have invested maximum number of times 
(consider repeat investments in one company also). In a startup, multiple investors might have invested. 
So consider each investor for that startup. Ignore undisclosed investors.
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
startup = pd.read_csv("startup_funding.csv")
df = startup.copy()

# dropping rows having Investors name as nan..
df.dropna(subset = ["InvestorsName"],inplace = True)  

# creating a dictionary to maintain the number of times the investors name appeared
d = {}  

# traversing through the investor names and counting the number of times their names appeared
for i in df["InvestorsName"].values:  
    # if it contains multiple names ..then spliting it ..and traversing through each names separately
    if "," in i: 
        for j in i.strip().split(','):
            d[j.strip()] = d.get(j.strip(),0) + 1
    else:
        d[i.strip()] = d.get(i.strip(),0) + 1

# deleting investor names which were undisclosed        
del d['Undisclosed']

# sorting the keys in reverse order(descending to aescending) according to the values...
d1 = sorted(d, key=d.get , reverse=True)[0:5]  

# printing the top 5 investors...funded maximum number of times...
for i in d1:
    print(i , d[i])



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
plt.title('Top 5 Investors')
plt.xlabel("Investors", fontsize=16)   # labels of x-axis
plt.ylabel("Number of Fundings", fontsize=16)  # labels of y_axis
plt.xticks(rotation = 0) # rotating names in x-axis
plt.show()

