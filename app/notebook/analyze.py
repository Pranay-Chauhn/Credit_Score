import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load scored wallets
df = pd.read_csv("app//output//final_wallet_scores.csv")

# Create score bins
bins = list(range(0, 1100, 100))  # 0-1000 in steps of 100
labels = [f"{i}-{i+99}" for i in bins[:-1]]
df['score_range'] = pd.cut(df['score'], bins=bins, labels=labels, right=False)

# Plot score distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='score_range', palette='viridis')
plt.title('Wallet Score Distribution')
plt.xlabel('Score Range')
plt.ylabel('Number of Wallets')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("app/output/score_distribution.png")
plt.close()

# Group statistics by score range
grouped = df.groupby("score_range").mean(numeric_only=True)
grouped.to_csv("app/output/score_behavior_by_range.csv")

print("✅ Score analysis completed. Distribution plot and behavior summary saved.")