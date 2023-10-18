import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 700)

# q0 read the nba.csv file
df4 = pd.read_csv("nba.csv")
#q1 show first 10 line
print(df4.head(10))
#q2 what is the total number of row?
print(df4.index)
#q3 what is the average salary of whole players?
print("Average Salary:", df4["Salary"].mean())
#q4 what is the highest salary? and player's info
print(df4[df4["Salary"] == df4["Salary"].max()])
#q5 what is the highest salary player's info and name
print(df4[df4["Salary"] == df4["Salary"].max()][["Name", "Salary"]])
#q6 show the name,age and team of the players between 20-25 age and sort values as desc for ages
print(df4[(df4["Age"] >= 20) & (df4["Age"] <= 25)][["Name", "Team", "Age"]].sort_values("Age", ascending=False))
#q7 What is the team of John Holland?
print(df4[df4["Name"] == "John Holland"]["Team"])
#q8 what is the average salary of each team?
print(df4.groupby("Team").agg({"Salary": "mean"}).sort_values("Salary", ascending=True))
#q9 What is the number of team (do not allow the duplicate)
print("Number of Team:", df4["Team"].nunique())
#10 What is the total players for each team?
print(df4["Team"].value_counts(ascending=True))
#11 show the rows when "and" exist in their names
df4.dropna(inplace=True)
print(df4[df4["Name"].str.contains("and")])
#12 find the average weight of players according to each team with one way and sort values as descending order of weight
print(df4.groupby("Team").agg({"Weight": "mean"}).sort_values("Weight",ascending=False))
#13 Find the average,max and min salary for each position with 1 way
print(df4.pivot_table("Salary","Position",aggfunc=["mean", "max", "min"]))
#14 Find the min, max and average weight and than create a new binned_age colum divide by 3 and write to new column
#labels = ["Thin","Normal","Fat"]
print(df4["Weight"].max())
print(df4["Weight"].min())
print(df4["Weight"].mean())
df4["binned_weight"] = pd.qcut(df4["Weight"], 3, labels=["Thin", "Normal", "Fat"])
print(df4.head(7))
#seperate Weight for three piece as min mean and max values of Weight and create a new column name is binned_weight2
bin = [df4["Weight"].min()-1,df4["Weight"].mean(), df4["Weight"].max()]
label = ["Normal", "Fat"]
df4["binned_weight2"] = pd.cut(df4["Weight"], [df4["Weight"].min()-1, df4["Weight"].mean(), df4["Weight"].max()], labels=label)
print(df4.head(7))

#15 Find the richest and the poorest player info
print(df4[df4["Salary"] == df4["Salary"].max()])
print(df4[df4["Salary"] == df4["Salary"].min()])
#16 Find the richest player whose Position is C
print(df4[df4["Position"] == "C"].sort_values("Salary", ascending=False).iloc[0])
#17 Find the first 5 richest players whose position is SG or PG
print(df4[(df4["Position"] == "SG") | (df4["Position"] == "PG")].sort_values("Salary", ascending=False).iloc[0:5])
#18 Find the last 5 richest players whose position is SG or PG
print(df4[(df4["Position"] == "SG") | (df4["Position"] == "PG")].sort_values("Salary", ascending=True).iloc[0:5])
#19 Show all information of "Chris" in their names and sort as desc according to their salaries

#20 What is the average Salary according to Team, Position and binned_weight2?
print(df4.pivot_table(values="Salary", index="Team", columns=["Position", "binned_weight2"], aggfunc="mean"))

#21 what is the average salary when according to Team, position is PG and Weight is greater than 200?
print(df4[(df4["Position"] == "PG") & (df4["Weight"] > 200)].groupby("Team").agg({"Salary": "mean"}))

#22 what is the average salary when according to Team, position is PG or SG and Weight is greater than 200 and less than 215?
print(df4[(df4["Weight"] >= 200) & (df4["Weight"] <= 215) &
      ((df4["Position"] == "PG") | (df4["Position"] == "SG"))].groupby("Team").agg({"Salary": "mean"}))

#23 Show the average salary for each team:
#With matplotlib:
data = df4.groupby("Team").agg({"Salary": "mean"})
data.plot(kind="bar", color="green")
plt.title("Average Salary per Team")
plt.xlabel("Team")
plt.ylabel("Average Salary")
plt.grid()
plt.xticks(rotation=45)
print(plt.show())
#with seaborn:
sns.barplot(x="Team", y="Salary", data=df4, estimator="mean", palette="viridis")
plt.title("Average Salary per Team")
plt.xlabel("Team")
plt.ylabel("Average Salary")
plt.grid()
plt.xticks(rotation=45)
print(plt.show())