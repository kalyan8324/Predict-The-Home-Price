import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams["figure.figsize"] = (20,10)

# LOAD FILE INTO CSV 
readfile = "/home/maren/Downloads/Python-project/Bengaluru_House_Data.csv"
df = pd.read_csv(readfile)
# CLEANING DATA
df1 = df.drop(['availability','society', 'balcony','area_type'],axis='columns')
#  HANDLE NOT AVAILABLE DATA 
df1.isnull().sum()
df3 = df1.dropna()
df3.isnull().sum()
#  FEATURE ENG 
df3['bhk'] = df3['size'].apply(lambda x: x.split(' ')[0])
def is_float(x):
    try:
        return float(x)
    except:
        return False
    return True
# df3[~df3['total_sqft'].apply(is_float)].head(10) 
# CONVERT 2 ELEMENTS TO AVG ELEMENTS 
def convert_sqft_to_num(x):
    token = x.split('-')
    if len(token) == 2:
        return (float(token[0])+float(token[1]))/2
    try:
        return float(x)
    except:
        return None
    
df4 = df3.copy()
df4.total_sqft = df4.total_sqft.apply(convert_sqft_to_num)
df4 = df4[df4.total_sqft.notnull()]
# FEATURE ENG 
# PRICE PER SQURE FEET CONVERTION 
df5 = df4.copy()
df5['price_per_sqft'] = df5['price']*100000/df5['total_sqft']
df5_stats = df5['price_per_sqft'].describe()
print(df5_stats)
df5.to_csv("bhp.csv",index=False)

#  strip is to remove spaces starting and ending points 
df5.location = df5.location.apply(lambda x:x.strip())
location_stats = df5['location'].value_counts(ascending=False)

#  we are manipulating location if location is less or equal 10 then we are creating as locatioon name others 
location_less_then_10 = location_stats[location_stats <= 10]
df5.location = df5.location.apply(lambda x : 'others' if x in location_less_then_10 else x)

#  REMOVAL OF OUTLIER 
# print(df5.head())
# print(df5[df5.total_sqft / df5.bhk < 300])
# print(type(df5.total_sqft) , " =  " ,  type(df5.bhk))
print(df5.head())
# df6 = df5[df5.total_sqft /df5.bhk < 300]
# df6.price_per_sqft.describe()

def plot_scatter_chart(df,location):
    bhk2 = df[(df.location == location) & (df.hnk == 2)]
    bhk3 = df[(df.location == location) & (df.hnk == 3)]
    matplotlib.rc_params['figure.figsize'] = (15,10)
    plt.scatter(bhk2.total_sqft, bhk2.price,color='blue' , label='2 BHK' ,s = 50)
    plt.scatter(bhk3.total_sqft,bhk3.price,marker='+', color='green',label='3 BHK', s=50)
    plt.xlabel("Total Square Feet Area")
    plt.ylabel("price in lacks")
    plt.title(location)
    plt.legend()
print(plot_scatter_chart(df5,"Hebbal"))
# print(df6.price_per_sqft.describe())