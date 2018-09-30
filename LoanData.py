#adopted from https://www.kaggle.com/pragyanbo/a-hitchhiker-s-guide-to-lending-club-loan-data 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import warnings
import xlrd
import jinja2
import gc
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
#%matplotlib inline

start_df = pd.read_csv('/Users/khyoung/Downloads/lending-club-loan-data/loan.csv', low_memory=False)

df = start_df.copy(deep=True)
print(df.head())

print(df.shape)
print(df.columns)

df_description = pd.read_excel('/Users/khyoung/Downloads/lending-club-loan-data/LCDataDictionary.xlsx').dropna()
df_description.style.set_properties(subset=['Description'], **{'width': '1000px'})
print(df_description)


def null_values(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'})
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
    print("Dataframe has " + str(df.shape[1]) + " columns.\n"
                                                "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")
    return mis_val_table_ren_columns


# missing values
miss_values = null_values(df)
miss_values.head(20)

print(miss_values)

target_list = [1 if i=='Default' else 0 for i in df['loan_status']]

df['TARGET'] = target_list
print(df['TARGET'].value_counts())

df.drop('loan_status',axis=1,inplace=True)

# Number of each type of column
df.dtypes.value_counts().sort_values().plot(kind='barh')
plt.title('Number of columns distributed by Data Types',fontsize=20)
plt.xlabel('Number of columns',fontsize=15)
plt.ylabel('Data type',fontsize=15)
