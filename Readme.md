# DeFi Wallet Scoring System

This project implements a rule-based scoring pipeline to evaluate DeFi wallet behavior on lending protocols such as Aave. It processes wallet activity from JSON data to assign interpretable trust/risk scores ranging from 0 to 1000.

## Project Structure

app/
├── output/ # Stores outputs
│ ├── wallet_features.csv # Extracted features per wallet
│ └── wallet_scores.csv # Final wallet scores
├── src/
│ ├── features.py # Feature engineering logic
│ ├── load.py # Data loading/saving utils
│ └── scoring.py # Rule-based scoring logic
└── main.py # Optional pipeline runner (future)


## What the Project Does

### Feature Engineering (`features.py`)
- Parses Aave protocol JSON activity logs
- Aggregates wallet-level features:
  - Number and amount of deposits, borrows, and repayments
  - Liquidation count
  - Borrow-to-deposit ratio
  - Active days vs. bot-like frequency
  - Inactivity flags

### Rule-Based Scoring (`scoring.py`)
- Applies transparent rules to assign scores:
  - Rewards consistent repayment and responsible borrowing
  - Penalizes risky behavior and liquidation events
  - Detects bot-like or inactive wallets
- Final score between 0 (high risk) and 1000 (high trust)

## Requirements

- Python 3.8 or higher
- pandas

Install dependencies:

pip install -r requirements.txt

## How to Use
1. Create and Setup env
    - python -m venv .venv
    - .\.venv\Scripts\activate
    - pip install -r requirements.txt
2. Place your JSON data from Aave in the appropriate directory.
3. In main.py, enter the path in main function at line 34.
4. In terminal run :
    - python -m app.main
5. Review outputs:
    - `app/output/wallet_features.csv`
    - `app/output/wallet_scores.csv`
6. Run analyze.py 
    - to get analysis 
## Applications

- DeFi wallet segmentation
- Airdrop eligibility scoring
- Decentralized credit risk modeling
- Bot wallet detection

## Data Source

This project assumes JSON data structured similarly to Aave’s publicly available on-chain lending activity.

## Future Work

- Integrate historical token prices for USD normalization
- Add percentile-based scoring to normalize across cohorts
- Deploy scoring as an API or web dashboard

## Contributors

- Pranay Chauhan — Data Scientist and AI eng  

