import pandas as pd

data = {
    'name' : ['rejin','anita'],
    'gender': ['m','f'],
    'age' : [21,22]
}

df = pd.DataFrame(data)
print(df)