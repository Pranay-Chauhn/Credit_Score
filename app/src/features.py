import json
import pandas as pd
from tqdm import tqdm
import os 


def load_data(path: str) -> pd.DataFrame:
    with open(path, 'r') as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # Convert amounts to numeric (float USD)
    df['amount'] = pd.to_numeric(df['actionData.amount'], errors='coerce')
    df['price'] = pd.to_numeric(df['actionData.assetPriceUSD'], errors='coerce')
    df['amount_usd'] = df['amount'] * df['price']
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    return df


def generate_wallet_features(df: pd.DataFrame) -> pd.DataFrame:
    feature_list = []

    for wallet, group in tqdm(df.groupby('userWallet'), desc="Processing wallets"):
        features = {
            'userWallet': wallet,
            'n_txns': len(group),
            'n_deposits': (group['action'] == 'deposit').sum(),
            'n_borrows': (group['action'] == 'borrow').sum(),
            'n_repays': (group['action'] == 'repay').sum(),
            'n_redeems': (group['action'] == 'redeemunderlying').sum(),
            'n_liquidations': (group['action'] == 'liquidationcall').sum(),
            'total_deposited_usd': group.loc[group['action'] == 'deposit', 'amount_usd'].sum(),
            'total_borrowed_usd': group.loc[group['action'] == 'borrow', 'amount_usd'].sum(),
            'unique_assets': group['actionData.assetSymbol'].nunique(),
            'active_days': (group['timestamp'].max() - group['timestamp'].min()).days + 1,
        }

        # Transactions per day
        features['txn_per_day'] = features['n_txns'] / max(1, features['active_days'])

        feature_list.append(features)

    return pd.DataFrame(feature_list)


if __name__ == "__main__":
    # Load and process
    file_path = "app\\data\\user-wallet-transactions.json"
    output_dir = "app\\output"
    output_path = os.path.join(output_dir,"wallet_features.csv")

    df = load_data(file_path)
    df = preprocess(df)

    # Feature engineering
    wallet_features = generate_wallet_features(df)

    # Save output
    wallet_features.to_csv(output_path, index=False)
    print("✅ Feature engineering completed. Output saved to output/wallet_features.csv")
