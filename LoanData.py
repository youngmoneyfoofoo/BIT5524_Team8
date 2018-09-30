#adopted from https://www.kaggle.com/pragyanbo/a-hitchhiker-s-guide-to-lending-club-loan-data 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import warnings
import gc
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
#%matplotlib inline

start_df = pd.read_csv('/Users/khyoung/Downloads/lending-club-loan-data/loan.csv', low_memory=False)

df = start_df.copy(deep=True)
print(df.head())

print(df.shape)
print(df.columns)