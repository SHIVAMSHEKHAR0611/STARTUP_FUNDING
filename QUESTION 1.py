"""
Your Friend has developed the Product and he wants to establish the product startup and
he is searching for a perfect location where getting the investment has a high chance. 
But due to its financial restriction, he can choose only between three 
locations -  Bangalore, Mumbai, and NCR. As a friend, you want to help your friend 
deciding the location. NCR include Gurgaon, Noida and New Delhi. Find the location 
where the most number of funding is done. That means, find the location where startups 
has received funding maximum number of times. Plot the bar graph between location and 
number of funding. Take city name "Delhi" as "New Delhi". Check the case-sensitiveness 
of cities also. That means, at some place instead of "Bangalore", "bangalore" is given. 
Take city name as "Bangalore". For few startups multiple locations are given, one Indian
and one Foreign. Consider the startup if any one of the city lies in given locations.
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import csv

# reading data from startup_funding.csv file
startup = pd.read_csv("startup_funding.csv")  

# creating a copy of startup dataframe...
df = startup.copy()  

# removing row's having nan's in city location column
df.dropna(subset = ["CityLocation"],inplace = True)  

# replacing the wrong word with the correct one..
df["CityLocation"].replace("bangalore","Bangalore",inplace = True)  
df["CityLocation"].replace("Delhi","New Delhi",inplace = True)

# dictionary to maintain the number of fundings in the provided locations...
dic = {}   

# traversing through all the locations and maintaining the number of times the provided 
# locations fetched...using if elif and else..
for i in df["CityLocation"]: 
    if "Bangalore" in i.strip().split('/'):
        dic["Bangalore"] = dic.get("Bangalore",0) + 1  
    elif "Mumbai" in i.strip().split('/'):
        dic["Mumbai"] = dic.get("Mumbai",0) + 1
    elif "New Delhi" in i.strip().split('/') or "Noida" in i.strip().split('/') or "Gurgaon" in i.strip().split('/') :
        dic["NCR"] = dic.get("NCR",0) + 1
    
print(dic)
# sorting the keys in reverse order(descending to aescending) according to the values...
cities = sorted(dic, key=dic.get , reverse=True)  

# list for cities with max number of fundings
fund = []  

# traversing through the cities...and created a new list of values...in sorted format 
for i in cities:  
    fund.append(dic[i])
    
# printing the city having most number of fundings    
print(cities[0]) 



#----------- PLOTTING GRAPH -----------#



# ploting the bar graph....cities vs no of fundings..
plt.bar(cities,fund,width = 0.4,color = "cyan" , edgecolor = "blue")  
plt.xlabel("Locations" , fontsize=16)   # labels of x-axis
plt.ylabel("Number of Fundings" , fontsize=16)  # labels of y_axis
plt.xticks(rotation = 0) # rotating names in x-axis
plt.title('Location Recieving Number of Funding')
# printing number of fundings corresponding to the cities.
for i in range(len(cities)):
    a = str(cities[i]) 
    y = int(fund[i])
    plt.text(a , y , fund[i])

plt.show()
