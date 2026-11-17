# sales-dashboard-ai-analysis
An interactive sales dashboard built from a 116-row retail CSV with AI assistance, plus the validation steps that make the result trustworthy.

## What it shows
- Filters by date, product and payment method, with KPI cards
- Sales over time (day, week or month; bars, line or cumulative)
- Product ranking, payment split, day of week, price points and basket size
- Product-by-payment heatmap and week-over-week change

**Live demo:** 

<img width="1369" height="604" alt="Overview" src="https://github.com/user-attachments/assets/5e3f9b46-d2d3-49fc-ac92-38017585637e" />
<img width="1369" height="324" alt="products_performances" src="https://github.com/user-attachments/assets/8588fbd8-16c4-4422-bd5a-eee6a5944cd1" />
<img width="1365" height="601" alt="Orders" src="https://github.com/user-attachments/assets/eeba6749-1e7a-44fa-a144-bd33f9c655e8" />

## Analysis notes

### Written from the full dataset (Aug 15 to Oct 7, 2025). They do not change with the filters.

**- Overview:** $11,214 from 98 orders and 116 items, with sales on every one of the 54 days. Average order value is $114.43, and 80 of 98 orders contain a single item.

**- Premium products carry revenue:** the three items priced at $100 or more (Premium Tailored Trousers, Tailored Wool Dress Trousers, Classic Denim Overalls) are 22% of items sold but 33% of revenue.

**- Volume and revenue leaders differ:** Premium Tailored Trousers lead on revenue ($1,575 from 9 units). Slim-Fit Denim Jeans and Classic Fit Chinos lead on units (13 each). Multi-Pocket Cargo Shorts are last on revenue ($580).

**- Payment mix is balanced:** eWallet, cash, credit and debit each take 24% to 27% of items. Debit has the lowest revenue ($2,503) and the lowest average item price ($89, against $103 for credit).

**- Product by payment patterns:** corduroy trousers skew to eWallet (6 of 9), chinos to debit (7 of 13) and premium tailored trousers to credit (5 of 9). Each cell holds very few items, so treat these as leads to check, not conclusions.

**- Weekly trend is flat:** the full weeks (Aug 18 to Oct 5) sit between $1,315 and $1,619. The +187% and -63% swings are artifacts of the partial first and last weeks.

**-Day of week:** Tuesday is highest ($2,064) and Thursday lowest ($1,232). With about 8 occurrences of each weekday, this could be noise.


## Run locally
Open `index.html` in a browser (internet needed for the Chart.js CDN). To check the numbers: `pip install pandas` then `python scripts/validate_data.py data/sales_data.csv`.


## Tech
JavaScript, Chart.js, Python (pandas), AI-assisted development (AI-Claude).
