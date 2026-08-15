# Real Estate Market Analysis

A data analysis project exploring residential property listings to uncover pricing trends,
locality-level insights, and the impact of RERA approval, construction status, and builder
reputation on price.

## What's in this repo

- **`main.py`** — Loads and cleans `data.csv`, then answers a series of analytical
  questions about the property market using `pandas`, and visualizes relationships with
  `matplotlib` / `seaborn`.
- **`data.csv`** — Raw property listing dataset (price, area, rate per sqft, locality,
  builder, RERA approval status, BHK count, etc.).
- **`real_estate_analysis.pptx`** — Presentation summarizing the findings.
- **`requirements.txt`** — Python dependencies needed to run the analysis.

## Questions explored

1. Which is the costliest flat in the dataset?
2. Which locality has the highest average price?
3. Which locality has the highest rate per square foot?
4. Do ready-to-move properties cost more than under-construction properties?
5. Do RERA-approved properties command a price premium?
6. How does area (sqft) impact property price?
7. Which BHK configuration is the most expensive on a per-square-foot basis?
8. Which property type (apartment, floor, plot, etc.) is the costliest?
9. Do certain builders consistently price higher than others?
10. Are larger homes always more expensive per square foot?

## Getting started

Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/real-estate-analysis.git
cd real-estate-analysis
pip install -r requirements.txt
```

Run the analysis:

```bash
python main.py
```

This will print answers to each question in the terminal and display two scatter plots
(area vs. price, and area vs. rate per square foot).

## Data cleaning notes

The script performs the following cleaning steps before analysis:
- Normalizes column names (lowercase, underscores, trimmed whitespace)
- Removes duplicate rows
- Strips commas and casts `price`, `area`, and `rate_per_sqft` to numeric types
- Standardizes categorical fields (`status`, `flat_type`)
- Maps `rera_approval` text values to boolean (`True` / `False`)

## Tech stack

- Python
- pandas
- matplotlib
- seaborn

## License

Feel free to adapt this note once you decide on a license (e.g. MIT) for the repo.
