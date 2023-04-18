import numpy as np
import pandas as pd

df = pd.read_table('TRNcod.xls')

filtered_df_zeros = df[df['IND_BOM_1_2'] == 0]
filtered_df_ones = df[df['IND_BOM_1_2'] == 1]

# print the filtered dataframe
# print(filtered_df)

filtered_df_zeros.to_csv("resultado/filtered_data_zeros.csv", index=False)
filtered_df_ones.to_csv("resultado/filtered_data_one.csv", index=False)