import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("online_shoppers_intention.csv")

# Encode categorical columns
encoders = {}
for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Split features and target
X = df.drop("Revenue", axis=1)
y = df["Revenue"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save everything
bundle = {
    "model": model,
    "encoders": encoders,
    "feature_order": X.columns.tolist()
}

with open("shopper_tree.pkl", "wb") as f:
    pickle.dump(bundle, f)

print("✅ .pkl file created successfully!")