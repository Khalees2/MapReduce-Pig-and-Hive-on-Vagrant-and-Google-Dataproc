#!/usr/bin/env python
import pandas as pd
data = pd.read_csv("files/51816.txt", sep = '\t',header=None, names=("Words","TF-IDF"))
data["Words"]=data["Words"].str.split(" ",n=1,expand=True)
print(data.head(10).sort_values(by=['TF-IDF'],ascending=False))
