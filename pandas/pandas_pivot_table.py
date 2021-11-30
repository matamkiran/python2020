

import pandas as pd

fifa=pd.read_csv("fifa_player.csv")

#fifa=fifa.head()


fifa_pivot=fifa.pivot_table(index="short_name",
                          columns="club",
                          values="wage_eur"
                      )

print(fifa_pivot)