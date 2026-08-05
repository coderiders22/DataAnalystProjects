# Data Analyst Projects

Data analyst projects built on a real Kaggle dataset 

## How every project is built
All 5 projects share one architecture, so once you understand one, you understand all of them:

- **SQL-first.** The actual analysis lives in each project's `queries.sql` as named, commented
  DuckDB queries — window functions, CTEs, percentiles, RFM, cohort analysis. This is the part
  worth reading closely.
- **A thin Python wrapper (`db.py`).** ~70 lines per project: loads the data into DuckDB, parses
  `queries.sql`, and exposes `run_query(name, **params)`.
- **One notebook (`analysis.ipynb`).** Runs each named query, charts it, and explains the finding
  in plain language — including the honest, sometimes counterintuitive ones (see below).
  Fully executed, so you can read the outputs on GitHub without running anything.
- **One dashboard (`app.py`).** A Streamlit app calling the *exact same* named queries as the
  notebook — nothing is duplicated between "the analysis" and "the live app."
- **A project README** with the problem statement, dataset info, how to run it, the real findings,
  and a screenshot of the dashboard.

Machine learning (clustering, regression) only shows up in project 4, where SQL genuinely isn't the
right tool — everywhere else, the aggregation/ranking/filtering logic stays in SQL on purpose,
since that's the skill most DA portfolios under-demonstrate.

## The 5 projects

| # | Project | Difficulty | Est. time | Best for |
|---|---------|-----------|-----------|---------|
| 1 | [Zomato Restaurant Analysis](./01-zomato-restaurant-analysis) | Beginner | First portfolio project, EDA fundamentals |
| 2 | [Flipkart Price Analysis](./02-flipkart-price-analysis) | Intermediate | Pricing strategy, business acumen |
| 3 | [Supply Chain & Inventory Analysis](./03-supply-chain-analysis) | Intermediate | Operations focus, supply chain optimization |
| 4 | [FIFA Player Performance Analysis](./04-fifa-player-analysis) | Intermediate-Advanced | Clustering, multivariate analysis, ML intro |
| 5 | [Olist E-Commerce Dashboard](./05-olist-ecommerce-dashboard) | Advanced | Complete DA workflow, capstone / interview showcase |
