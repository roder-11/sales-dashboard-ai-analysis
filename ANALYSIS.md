# Analysis notes

Period: 2025-08-15 to 2025-10-07 (54 days, sales on every day). Source: `data/sales_data.csv`.

| Metric | Value |
|---|---|
| Revenue | $11,214 |
| Orders | 98 |
| Items sold | 116 |
| Average order value | $114.43 |
| Orders with one item | 80 of 98 |

## Findings
1. **Premium products carry revenue.** Premium Tailored Trousers, Tailored Wool Dress Trousers and Classic Denim Overalls (all $100 or more) are 22% of items but 33% of revenue ($3,655).
2. **Volume and revenue leaders differ.** Premium Tailored Trousers lead on revenue ($1,575, 9 units). Slim-Fit Denim Jeans and Classic Fit Chinos lead on units (13 each). Multi-Pocket Cargo Shorts are last on revenue ($580).
3. **Payment mix is balanced.** eWallet 31 items, cash 29, credit 28, debit 28. Debit has the lowest revenue ($2,503) and average item price ($89, against $103 for credit).
4. **Product by payment.** Corduroy trousers skew to eWallet (6 of 9), chinos to debit (7 of 13), premium tailored trousers to credit (5 of 9). Counts are tiny, so these are leads to test.
5. **Weekly revenue is flat.** Full weeks (Aug 18 to Oct 5) range from $1,315 to $1,619. The +187% and -63% swings come from the partial first and last weeks.
6. **Day of week.** Tuesday is highest ($2,064), Thursday lowest ($1,232). With about 8 occurrences per weekday this may be noise.

## Limits
About 8 weeks of data, one unit per row, and no cost, customer or discount fields. Margin, retention and seasonality cannot be analysed.
