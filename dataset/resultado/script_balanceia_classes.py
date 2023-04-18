import pandas as pd
import random

# load CSV file into a pandas dataframe
df0 = pd.read_csv('filtered_data_zeros.csv')
df1 = pd.read_csv('filtered_data_one.csv')

# determine the number of rows in the dataframe
num_rows0 = df0.shape[0]
num_rows1 = df1.shape[0]

if num_rows0 > num_rows1:
    n = num_rows0 - num_rows1

    # select n random row indices
    #Does random.sample() repeat elements?
    #No, the random.sample() function in Python's random module will not repeat elements by default.
    #The purpose of random.sample() is to generate a random subset of unique elements from a given population sequence without replacement.

    random_indices = random.sample(range(num_rows1), n)

    # select rows corresponding to the random indices
    random_rows = df1.iloc[random_indices]

    df1 = df1.append(random_rows)

    df0 = df0.drop(['INDEX'], axis=1)
    df1 = df1.drop(['INDEX'], axis=1)


    df1.to_csv("resultado/filtered_data_balanced_NoIndex_ones_.csv", index=False)
    df0.to_csv("resultado/filtered_data_balanced_NoIndex_zeros.csv", index=False)
    # print the selected rows
    print(df1)

else:
    n = num_rows1 - num_rows0

    # select n random row indices
    random_indices = random.sample(range(num_rows0), n)

    # select rows corresponding to the random indices
    random_rows = df0.iloc[random_indices]

    df0 = df0.append(random_rows)
    
    df0 = df0.drop(['INDEX'], axis=1)
    df1 = df1.drop(['INDEX'], axis=1)

    df1.to_csv("resultado/filtered_data_balanced_ones_.csv", index=False)
    df0.to_csv("resultado/filtered_data_balanced_zeros.csv", index=False)
    # print the selected rows
    print(df0)