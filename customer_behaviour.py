import pandas as pd 
df =  pd.read_csv('C:/Users/gaura/OneDrive/Desktop/customer_shopping_behavior.csv')
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)
# for see the all columns


# Top 5 rows in Table
print(df.head())

# information of table
print(df.info())

# To check summary satistics

# note :- descibe given us to only numbrical column


# count  3900.000000  ...         3900.000000
# mean   1950.500000  ...           25.351538
# std    1125.977353  ...           14.447125
# min       1.000000  ...            1.000000
# 25%     975.750000  ...           13.000000
# 50%    1950.500000  ...           25.000000
# 75%    2925.250000  ...           38.000000
# max    3900.000000  ...           50.000000
print(df.describe())


# Note2:- If we want all categorical columms 
print("All categorical columns")
print(df.describe(include='all'))


# Check the missing values
print(df.isnull().sum())


# 
df['Review Rating'] =df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))
print(df.isnull().sum())


# convert into lower case and replace string name with '_' use the command 
# df.columns = df.columns.str.lower()
# df.columns = df.columns.str.replace(' ','_')
print('replace name " " to _ ')

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns ={'purchase_amount_(usd)':'purchase_amount'})

print(df.columns)


# create a column age_group

labels = ['Young Adult','Adult','Middle-Age','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels =labels)

# ✅ Step 2: Understanding pd.qcut()
# pd.qcut() is a function from pandas.
# 📌 Full form: Quantile Cut
# It divides data into equal-sized groups (based on number of observations).

'''
q =4

This tells pandas to divide the data into 4 quantiles.

Since 4 groups → these are called quartiles.

Each group will contain approximately 25% of the data.

So:

First 25% → Young Adult

Next 25% → Adult

Next 25% → Middle-Age

Last 25% → Senior
'''
print(df[['age','age_group']].head(10))


# create column purchase_frequence_days

frequency_mapping ={
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quaterly':90,
    'Bi-weekly':14,
    'Annually':365,
    'Every 3 Month':90
}



df['purchase_frequence_days'] = df['frequency_of_purchases'].map(frequency_mapping)

print(df[['purchase_frequence_days','frequency_of_purchases']].head(10))



#check columns discount_appiled and promo_code_used
print(df[['discount_applied','promo_code_used']].head(10))

print('True & False :')

print((df['discount_applied'] == df['promo_code_used']).all())


df =df.drop('promo_code_used',axis=1)

print(df.columns)