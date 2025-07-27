import pandas as pd
import joblib

def score_wallet(row):
    score = 500  # Base score out of 1000

    # ---------------- Deposit Behavior (Trust + Engagement) ----------------
    if row['n_deposits'] > 10:
        score += 100  # Active depositors are more trustworthy
    elif row['n_deposits'] < 2:
        score -= 50  # Too few deposits may indicate low engagement

    # ---------------- Borrow/Repay Behavior (Creditworthiness) ----------------
    if row['n_borrows'] > 0:
        if row['total_borrowed_usd'] > 0 and row['n_repays'] > 0:
            repay_ratio = row['n_repays'] / row['n_borrows']
            if repay_ratio >= 0.9:
                score += 150  # Very responsible borrower
            elif repay_ratio >= 0.5:
                score += 50   # Moderately responsible
            else:
                score -= 50   # Risky borrower
        elif row['n_repays'] == 0:
            score -= 150  # Took loans but never repaid

    # ---------------- Loan-to-Deposit Ratio (Overleveraging Risk) ----------------
    if row['total_deposited_usd'] > 0:
        loan_ratio = row['total_borrowed_usd'] / row['total_deposited_usd']
        if loan_ratio > 2:
            score -= 100  # Borrowed too much compared to deposits
        elif loan_ratio > 1:
            score -= 50   # Slightly risky leverage

    # ---------------- Liquidations (Financial Health) ----------------
    score -= row['n_liquidations'] * 100  # Penalize each liquidation heavily

    # ---------------- Activity Level (Loyalty Signal) ----------------
    if row['active_days'] > 20:
        score += 50  # Long-term users are more loyal and reliable

    # ---------------- Transaction Frequency (Bot Detection) ----------------
    if row['txn_per_day'] > 10:
        score -= 100  # May indicate bot or abnormal usage

    # ---------------- Normalize Final Score ----------------
    score = max(0, min(1000, score))  # Ensure within 0 to 1000
    return score

# Scoring using Self-Suopervised Tech 

# Load saved model
model = joblib.load(r"D:\Projects\aave_credit_score\app\models\credit_score_model.pkl")

def assign_credit_score(wallet_features_df):
    # Predict risk label
    risk_probs = model.predict_proba(wallet_features_df)[:, 1]

    # Score out of 1000
    scores = (1 - risk_probs) * 1000
    scores = scores.round().astype(int)

    return scores
