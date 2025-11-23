import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
df=pd.read_excel("Data")

train_val_df, test_df = train_test_split(
    df,
    test_size=0.1,
    stratify=df[['M', 'P', 'T']],
    random_state=42
)
train_df, val_df = train_test_split(
    train_val_df,
    test_size=0.115,
    stratify=train_val_df[['M', 'P', 'T']],
    random_state=42
)
train_df.to_csv('train_set.csv', index=False)
val_df.to_csv('validation_set.csv', index=False)
test_df.to_csv('test_set.csv', index=False)
