def Filas_null(df,number):
    import pandas as pd
    df["Nulls%"]= df.isnull().sum(axis=1)/len(df.columns)*100
    df.drop(df[df["Nulls%"]>=number].index, inplace = True)
    df.drop(["Nulls%"], axis = 1, inplace = True)
    return df


def Clean_values(df,column,clean_word,contain_list):
    import numpy as np
    word = "|".join(contain_list)
    df[column] = np.where(df[column].str.contains(word,case=False)==True, clean_word, df[column])
    return df

def Clean_values_other(df,column,contain_list):
    import numpy as np
    word = "|".join(contain_list)
    df[column] = np.where(df[column].str.contains(word,case=False)==True, df[column], "Other")
    return df

def num_extract(df,column,number):
    df[column] = df[column].str.extract(r'(\d{'+ str(number)+'})')
    return df

def No_blank(df,column):
    import re
    df[column] = df[column].apply(lambda x: re.sub('\A\s|\Z\s',"",x))
    return df

def Numerizar(df,column,item,new_column):
    import numpy as np
    df[new_column] = np.where(df[column] == item,1,0)
    