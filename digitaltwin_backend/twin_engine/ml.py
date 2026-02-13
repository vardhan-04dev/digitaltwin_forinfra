import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor

# ---------------- LOAD FILE ----------------
# your file is pipe-formatted text, not true CSV
df = pd.read_csv("data.csv", header=None)

# split the single text column into real columns
df = df[0].str.split("|", expand=True)

# first row becomes header
df.columns = df.iloc[0]
df = df[1:]

# remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Columns detected:", df.columns.tolist())

# ---------------- RENAME FOR TWIN ENGINE ----------------
df = df.rename(columns={
    "Temp(C)": "temp",
    "Power(W)": "power",
    "Crowd": "crowd"
})

# keep only required columns
df = df[["temp", "power", "crowd"]]

# convert strings to numbers
df = df.astype(float)

# ---------------- CREATE TRAINING DATA ----------------
# 1 row = 1 second → 2 minutes = 120 rows ahead
STEP_AHEAD = 120

X = df.iloc[:-STEP_AHEAD].values
y = df.shift(-STEP_AHEAD).iloc[:-STEP_AHEAD].values

# ---------------- TRAIN MODEL ----------------
model = RandomForestRegressor(
    n_estimators=120,
    random_state=42
)

model.fit(X, y)

# ---------------- SAVE MODEL ----------------
joblib.dump(model, "model.pkl")

print("model.pkl created successfully")
