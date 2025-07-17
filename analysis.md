# Wallet Score Analysis

This document summarizes the results of the wallet scoring system after processing all user wallets.

---

##  Score Distribution

Below is the distribution of wallet scores across 10 buckets:

![Score Distribution](./output/score_distribution.png)

| Score Range | Description |
|-------------|-------------|
| 0–99        | Very poor wallets: high risk, almost no repayments, many liquidations |
| 100–199     | Poor wallets: rare repayments, very low deposits |
| 200–299     | Subpar: some deposits, minimal borrow/repay activity |
| 300–399     | Average activity, no liquidations but low repay ratio |
| 400–499     | Slightly below optimal behavior |
| 500–599     | Baseline good users with decent activity |
| 600–699     | Active users with good deposit/borrow behavior |
| 700–799     | Very healthy wallets, near-full repayment ratio |
| 800–899     | Highly responsible wallets, long-term usage |
| 900–1000    | Top-tier users: high deposits, full repayment, low risk |

---

##  Behavioral Summary by Score Range

This is based on `score_behavior_by_range.csv` output:

- **0–199**:
  - Very low deposits
  - High liquidation count
  - No or very low repayments
  - Bot-like behavior (high txn/day)

- **200–499**:
  - Moderate deposits
  - Some borrow but low repayment ratio
  - Moderate liquidation or inactivity

- **500–799**:
  - Healthy number of deposits
  - Good repay ratio (0.5–0.9)
  - Low liquidations
  - Active usage

- **800–1000**:
  - High deposits and borrow volumes
  - Repay ratio close to 1
  - Zero or minimal liquidations
  - Steady, non-bot-like activity

---

##  Output Files

- `wallet_scores.csv`: Final scores assigned to each wallet
- `score_distribution.png`: Histogram of wallet scores
- `score_behavior_by_range.csv`: Average metrics for each score range

---

##  Conclusion

This scoring model helps us clearly segment wallet users based on their on-chain behavior. It can be integrated into DeFi applications for credit risk profiling, loyalty scoring, or targeted incentives.
