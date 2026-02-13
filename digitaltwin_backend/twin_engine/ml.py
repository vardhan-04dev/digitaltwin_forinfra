import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data.csv", header=None)

df = df.dropna(axis=1, how="all")

if isinstance(df.iloc[0,0], str):
    df = df.iloc[1:]


df = df.astype(float)


df = df[[1,2,3,4]]

print("Rows after cleaning:", len(df))

STEP_AHEAD = 30

X = df.iloc[:-STEP_AHEAD].values
y = df.shift(-STEP_AHEAD).iloc[:-STEP_AHEAD].values

print("Training samples:", len(X))

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("model.pkl created successfully")
