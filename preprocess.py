import json
import pandas as pd
import matplotlib.pyplot as plt

jsonname="agc29"

f=open(f"../data/{jsonname}.json")
js = json.load(f)

attendnum=[]
rates=[]

#問題名の取得
tasknames=[task["TaskScreenName"] for task in js["TaskInfo"]]

#データフレーム作成
df=pd.DataFrame()
df.columns=[]

values=[]
for userdata in js["StandingsData"]:
    value=[]
    #print(userdata["UserName"])
    value.append(userdata["Competitions"])
    value.append(userdata["OldRating"])

    for task in tasknames:
        if task not in userdata["TaskResults"]:
            value.append(0)
        else:
            value.append(userdata["TaskResults"][task]["Status"])
    
    values.append(value)

output=pd.DataFrame(values)
colname=["attendnum","OldRating"]
colname.extend(tasknames)
output.columns=colname
output.to_csv(f"preprocessed_{jsonname}.csv",index=False)