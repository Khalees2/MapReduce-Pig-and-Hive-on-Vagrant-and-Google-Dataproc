import pandas as pd
import re

dataset = pd.read_csv("/Users/salmank/Documents/SEM2/CT/Assignment1/FirstAssignment/Data/raw/res4.csv")
dataset["Body"] = dataset.Body.apply(lambda x: re.sub('<.*?>|,|\n*|\t*|\r*|','', x))
dataset["Body"] = dataset.Body.apply(lambda x: re.sub(r"[^a-zA-Z]+",' ', x))
dataset["Title"] = dataset.Title.apply(lambda x: re.sub('<.*?>|,|\n*|\t*|\r*|','', x))
dataset["Title"] = dataset.Title.apply(lambda x: re.sub(r"[^a-zA-Z]+",' ', x))
dataset.to_csv("/Users/salmank/Documents/SEM2/CT/Assignment1/FirstAssignment/Data/cleaned/res4.csv",index=False)