import pandas as pd

df = pd.DataFrame({
    'a':[1, 2],
    'b':[3, 4]
})

grp = df.groupby('b')
print(grp.describe())

