# app/main.py
import os
from app.src.features import load_data, preprocess, generate_wallet_features
from app.src.scoring import score_wallet
import pandas as pd

def main(file_path = "app\\data\\user-wallet-transactions.json"):
    # Path
    file_path = file_path
    output_dir = "app\\output"
    os.makedirs(output_dir, exist_ok=True)
    data_output_path = os.path.join(output_dir,"wallet_features.csv")

    # Step 1: Load + preprocess
    df = load_data(file_path)
    df = preprocess(df)

    # Step 2: Feature engineering
    wallet_features = generate_wallet_features(df)
    
    # Save output
    wallet_features.to_csv(data_output_path, index=False)
    print("✅ Feature engineering completed. Output saved to output/wallet_features.csv")

    # Step 3: Scoring
    wallet_features['score'] = wallet_features.apply(score_wallet, axis=1)

    # Step 4: Save results
    score_output_path = os.path.join(output_dir,"final_wallet_scores.csv")
    wallet_features.to_csv(score_output_path, index=False)
    print(f"✅ All done. Output saved at {score_output_path}")

if __name__ == "__main__":
    main() # enter the path of your json data here eg: main("app\\test.json").
