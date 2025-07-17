import json
import pandas as pd

file_path = "app\\data\\user-wallet-transactions.json"


#Path to your json file
with open(file_path, "r") as f :
    data = json.load(f)

# Convert to DataFrame
df = pd.json_normalize(data)
df.head()



# Display basic info
print("Total transactions:", len(df))
print("\nSample rows:")
df.head(1)
df.columns

# Unique wallet count
wallet_counts = df['userWallet'].nunique()
print(f"\nUnique wallets found: {wallet_counts}")

# Actions overview
print("\nAction type counts:")
print(df['action'].value_counts())

# User Unique Wallet

df['userWallet'].unique()
