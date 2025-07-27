import pandas as pd
from app.src.scoring import score_wallet, assign_credit_score
import os

# ----------- File Paths -----------
WALLET_FEATURES_PATH = "app/data/wallet_features.csv"
INPUT_WALLETS_PATH = "D:/Projects/aave_credit_score/app/test/test.csv"
OUTPUT_PATH = "output/final_wallet_scores.csv"

# ----------- Ensure Output Directory -----------
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

def main():
    # Load all wallet features
    try:
        features_df = pd.read_csv(WALLET_FEATURES_PATH)
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Features file not found at {WALLET_FEATURES_PATH}")

    # Load list of wallet addresses to score
    try:
        wallets_to_score = pd.read_csv(INPUT_WALLETS_PATH)
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Input file not found at {INPUT_WALLETS_PATH}")
    
    if 'wallet_id' not in wallets_to_score.columns:
        raise ValueError("❌ Input CSV must contain 'wallet_address' column.")

    # Filter features for input wallets
    filtered_df = features_df[features_df['userWallet'].isin(wallets_to_score['wallet_id'])].copy()
    
    if filtered_df.empty:
        raise ValueError("❌ None of the provided wallet addresses were found in the features file.")

    # Apply rule-based scoring
    filtered_df['rule_score'] = filtered_df.apply(score_wallet, axis=1)

    # Apply model-based (self-supervised) credit scoring
    credit_scores = assign_credit_score(filtered_df.drop(columns=['userWallet']))
    filtered_df['model_score'] = credit_scores['credit_score']

    # Final output
    result_df = filtered_df[['userWallet', 'rule_score', 'model_score']]
    result_df.to_csv(OUTPUT_PATH, index=False)

    print(f"✅ Scoring completed successfully. Results saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()