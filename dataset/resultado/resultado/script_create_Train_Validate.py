import pandas as pd
import random

def shuffle_dataframe(dataframe):
    # obtem a quantidade de linhas no dataframe
    num_rows = dataframe.shape[0]
    #cria uma lista de tamanho 'num_rows' com numeros aleatorios entre 0 e 'num_rows', sem repeticao
    random_indices = random.sample(range(num_rows), num_rows)

    #pega as linhas do dataframe de acordo com os indices
    random_rows = dataframe.iloc[random_indices]

    #cria um novo dataframe com os elementos indexados de maneira aleatoria
    dataframe_shuffled = pd.DataFrame()
    dataframe_shuffled = pd.concat([dataframe_shuffled, random_rows])

    return dataframe_shuffled

# load CSV file into a pandas dataframe
df0 = pd.read_csv('./filtered_data_balanced_NoIndex_zeros.csv')
df1 = pd.read_csv('./filtered_data_balanced_NoIndex_ones_.csv')

df0_shuffled = shuffle_dataframe(df0)
df1_shuffled = shuffle_dataframe(df1)

print("for_train")
index_list = []
#o tamanho de df0_shuffled precisa ser igual ao de df1_shuffled
for index in range(int(df0_shuffled.shape[0] * 0.75)):
    index_list.append(index)

df0_train_rows = df0_shuffled.iloc[index_list]
df1_train_rows = df1_shuffled.iloc[index_list]

df_train = pd.DataFrame()
df_train = pd.concat([df0_train_rows, df1_train_rows])
df_train = shuffle_dataframe(df_train)
df_train.to_csv("resultado/df_train.csv", index = False)

print("for_validate")
index_list = []
for index in range(int(df0_shuffled.shape[0] * 0.75), df0_shuffled.shape[0]):
    index_list.append(index)

df0_validate_rows = df0_shuffled.iloc[index_list]
df1_validate_rows = df1_shuffled.iloc[index_list]

df_validate = pd.DataFrame()
df_validate = pd.concat([df0_validate_rows, df1_validate_rows])
df_validate = shuffle_dataframe(df_validate)
df_validate.to_csv("resultado/df_validate.csv", index = False)

