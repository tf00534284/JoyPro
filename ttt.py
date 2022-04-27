import pandas as pd

# col=["state","county","fips","trump16","clinton16","otherpres16","romney12","obama12","otherpres12","demsen16","repsen16","othersen16","demhouse16","rephouse16","otherhouse16","demgov16","repgov16","othergov16","repgov14","demgov14","othergov14","total_population","cvap","white_pct","black_pct","hispanic_pct","nonwhite_pct","foreignborn_pct","female_pct","age29andunder_pct","age65andolder_pct","median_hh_inc","clf_unemploy_pct","lesshs_pct","lesscollege_pct","lesshs_whites_pct","lesscollege_whites_pct","rural_pct","ruralurban_cc"]

# df = pd.read_csv("2018.csv",sep=",",usecols=col)
# print(df)

df = pd.read_csv("AK.csv",sep=",")
print(df)