<h1 align="center">📊 sales-dashboard-ai-analysis</h1>

<p align="center">
  An interactive sales dashboard built from a 116-row retail CSV with AI assistance,<br>
  plus the validation steps that make the result trustworthy.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="Chart.js">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
</p>

---

## 🤖 Built with AI

This project was developed with AI assistance, and every figure was then checked against the raw data with a Python validation script.

<p align="center">
  <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Google%20AI%20Studio-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google AI Studio">
  <img src="https://img.shields.io/badge/ChatGPT-74AA9C?style=for-the-badge&logo=openai&logoColor=white" alt="ChatGPT">
  <img src="https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=claude&logoColor=white" alt="Claude">
</p>

> AI speeds up the build, but the numbers are only trusted after validation (`scripts/validate_data.py`).

---

## 🎯 What it shows

- 🔎 Filters by date, product and payment method, with KPI cards
- 📈 Sales over time (day, week or month; bars, line or cumulative)
- 🏆 Product ranking, payment split, day of week, price points and basket size
- 🔥 Product-by-payment heatmap and week-over-week change

🚀 **Live demo:**  [claude.ai] https://claude.ai/artifact/VRRRVVraAzo4ZVKBAwWshX

## 🖼️ Screenshots

<p align="center">
 <img width="1369" height="645" alt="Overview" src="https://github.com/user-attachments/assets/95a8e3f8-f128-4099-95e7-2c6e0cfe0b08" />
</p>
<p align="center">
  <img width="1369" height="649" alt="products_performances" src="https://github.com/user-attachments/assets/5eec26fb-df76-4d55-b358-5d7ffb4b7be3" />
</p>
<p align="center">
 <img width="1369" height="646" alt="products_by_Paiements" src="https://github.com/user-attachments/assets/9b3b08ea-9031-4ebd-a3af-fdc7ef054f84" />
</p>
<p align="center">
<img width="1369" height="301" alt="Week-Over-Week" src="https://github.com/user-attachments/assets/db983e38-d031-4e81-abdb-9d3f0bf7b69e" />
</p>
<p align="center">
<img width="1369" height="643" alt="Transactions" src="https://github.com/user-attachments/assets/b234cc6a-9e30-4866-8993-8dbdff9b9192" />
</p>

---

## 💡 Analysis notes

_Written from the full dataset (Aug 15 to Oct 7, 2025). They do not change with the filters._

| Theme | Key finding |
|---|---|
| 🧾 **Overview** | **$11,214** from **98 orders** and **116 items**, with sales on all **54 days**. Average order value is **$114.43**, and 80 of 98 orders contain a single item. |
| 💎 **Premium products carry revenue** | The three items priced at $100 or more (Premium Tailored Trousers, Tailored Wool Dress Trousers, Classic Denim Overalls) are **22% of items sold** but **33% of revenue**. |
| 📦 **Volume vs revenue leaders** | Premium Tailored Trousers lead on revenue ($1,575 from 9 units). Slim-Fit Denim Jeans and Classic Fit Chinos lead on units (13 each). Multi-Pocket Cargo Shorts are last on revenue ($580). |
| 💳 **Payment mix is balanced** | eWallet, cash, credit and debit each take 24% to 27% of items. Debit has the lowest revenue ($2,503) and the lowest average item price ($89, against $103 for credit). |
| 🔗 **Product by payment** | Corduroy trousers skew to eWallet (6 of 9), chinos to debit (7 of 13) and premium tailored trousers to credit (5 of 9). Each cell holds very few items, so treat these as leads to check, not conclusions. |
| 📉 **Weekly trend is flat** | The full weeks (Aug 18 to Oct 5) sit between $1,315 and $1,619. The +187% and -63% swings are artifacts of the partial first and last weeks. |
| 📅 **Day of week** | Tuesday is highest ($2,064) and Thursday lowest ($1,232). With about 8 occurrences of each weekday, this could be noise. |

---

## ▶️ Run locally

Open `index.html` in a browser (internet needed for the Chart.js CDN).

## 🛠️ Tech

JavaScript · Chart.js · Python (pandas) · AI-assisted development (Gemini, Google AI Studio, ChatGPT, Claude)

---

<p align="center">
  Made by <b>Rodrigue Awono</b> · Business Intelligence & Data Analyst → Data Engineering
</p>
