import pandas as pd

fifa=pd.read_csv("fifa_player.csv")

#fifa=fifa.head()


fifa_pivot=fifa.pivot(index="short_name",
                      columns="nationality",
                      values=["height_cm","weight_kg"])

print(fifa_pivot)