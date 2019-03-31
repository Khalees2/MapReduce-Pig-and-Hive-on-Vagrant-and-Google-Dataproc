import pandas as pd
dataOne = pd.read_csv('/Users/salmank/Documents/SEM2/CT/Assignment1/FirstAssignment/Data/cleaned/res1.csv')
dataTwo = pd.read_csv('/Users/salmank/Documents/SEM2/CT/Assignment1/FirstAssignment/Data/cleaned/res2.csv')
dataThree = pd.read_csv('/Users/salmank/Documents/SEM2/CT/Assignment1/FirstAssignment/Data/cleaned/res3.csv')
dataFour = pd.read_csv('/Users/salmank/Documents/SEM2/CT/Assignment1/FirstAssignment/Data/cleaned/res4.csv')
final = pd.concat([dataOne,dataTwo,dataThree,dataFour])
final.to_csv("/Users/salmank/Documents/SEM2/CT/Assignment1/FirstAssignment/Data/final.csv")
final = pd.read_csv("/Users/salmank/Documents/SEM2/CT/Assignment1/FirstAssignment/Data/final.csv")
null_column_check=final.columns[final.isnull().any()]
final[null_column_check].isnull().sum()