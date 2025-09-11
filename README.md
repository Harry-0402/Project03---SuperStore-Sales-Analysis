# 📊 Superstore Sales Analysis – Power BI Project

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?logo=powerbi)
![pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green?logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📖 Table of Contents

1. [Overview](#-project-overview)
2. [Repository Structure](#-repository-structure)
3. [Workflow & Methodology](#️-workflow--methodology)

   * [Data Preprocessing (Python)](#1-data-preprocessing-python)
   * [Dashboard Development (Power-BI)](#2-dashboard-development-power-bi)
4. [How to Run](#-how-to-run-the-project)
5. [Key Insights](#-example-insights)
6. [Preview](#-dashboard-preview)
7. [Acknowledgements](#-acknowledgements)
8. [Author & Copyright](#-author--copyright)

---

## 📌 Project Overview

This project analyzes **Superstore sales data** to generate actionable insights on **sales, profit, customers, and product performance**.

* ✅ **Python (Pandas)** for preprocessing and feature engineering.
* ✅ **Power BI** for building interactive dashboards.
* ✅ Business KPIs like **Profit Margin, Revenue per Item, Sales Trends, Customer Analysis**.

---

## 📂 Repository Structure

```
Superstore-Sales-Analysis/
│── Sample-Superstore.cvs                # Raw dataset
│── Superstore_Sales_Analysis.xlsx       # Basic Excel Analysis
│── Preprocessing Script for Superstore Dataset.py  # Python preprocessing script
│── Superstore_Cleaned.csv               # Cleaned dataset (generated after running script)
│── Dashboard.pbix                       # Power BI dashboard file
│── Dashboard_Overlook.pdf               # Dashboard summary (PDF)
│── README.md                            # Project documentation
```

---

## ⚙️ Workflow & Methodology

### 1. **Data Preprocessing (Python)**

The preprocessing script handles data cleaning and transformation:

* 🔹 Convert `Order Date` & `Ship Date` → DateTime format.
* 🔹 Standardize categorical columns (`Region`, `Segment`, etc.).
* 🔹 Create new features:

  * `Profit Margin` (Profit ÷ Sales).
  * `Revenue Per Item` (Sales ÷ Quantity).
  * `Year`, `Month`, `Quarter`.
* 🔹 Remove duplicates (`Row ID`, `Order ID`).
* 🔹 Handle missing values (fill Postal Codes, drop nulls in Sales/Profit).
* 🔹 Export as `Superstore_Cleaned.csv`.

---

### 2. **Dashboard Development (Power BI)**

The **Power BI Dashboard** (`Dashboard.pbix`) visualizes KPIs and business insights across **three pages**.

**Page 1 – Sales Overview**

* 💰 **Total Sales**: ₹2.30M
* 📈 **Total Profit**: ₹286.40K
* 📊 **Profit Margin**: 12.47%
* 🛒 **Total Orders**: 5009
* 📉 Sales & Profit Trends (2014–2017).
* 🌍 Regional Sales & Profits (East, West, Central, South).
* 👥 Sales by Segment (Consumer, Corporate, Home Office).
* 🏆 Top 5 Customers by Sales.
* 📦 Sales by Category & Sub-Category.
* 🔍 Interactive filters: Year, Region, Category, State, City, Segment.

**Page 2 – Hierarchical Data Drill-Down**

* 🔍 **Sum of Sales hierarchy**: ₹22,97,200.86
  
      Category → Sub-Category → Region → State → City → Segment → Technology (₹8,36,154.03) → Phones (₹3,30,007.05) → East (₹1,00,614.98) → New York (₹47,502.62) → New York City (₹37,959.13) → Consumer (₹18,919.08)

* 💰 **Sum of Profit hierarchy**: ₹2,86,397.02

      Category → Sub-Category → Region → State → City → Segment → Technology (₹1,45,454.95) → Copiers (₹55,617.82) → West (₹19,327.24) → Washington (₹9,442.42) → Seattle (₹8,290.44) → Consumer (₹6,809.98)

**Page 3 – Key Influencers**

* 🔍 **AI-driven Key Influencers** visual.
* Highlights which factors most strongly affect **Sales increase or decrease**.
* Example: Sales increase when `Total Quantity Sold > 7`, or when `Discount` ranges between 0.2–0.5.
* Helps identify **business drivers** behind performance.

---

## 🚀 How to Run the Project

### 🔧 Prerequisites

* **Python 3.x**
* **pandas** library
* **Power BI Desktop**

### ▶️ Steps

1. Clone the repository:

   ```bash
   git clone <repo_url>
   cd Superstore-Sales-Analysis
   ```

2. Run the preprocessing script (update output path if needed):

   ```bash
   python "Preprocessing Script for Superstore Dataset.py"
   ```

3. Open `Dashboard.pbix` in **Power BI Desktop**.

4. Connect it to the `Superstore_Cleaned.csv`.

5. Interact with filters & explore insights.

---

## 📊 Example Insights

* 👥 **Consumer Segment** drives \~50% of total sales.
* 💻 **Technology Category** leads in revenue (₹836K).
* ☎️ **Phones & Chairs** are top-selling sub-categories.
* 🌍 **East & West regions** outperform Central in profit and sales.
* 🏆 Customers like *Sean Miller* and *Tamara Chapman* generate the highest sales.
* 📉 Discounts in the **0.2–0.5 range** significantly impact sales patterns.

---

## ☑ Dashboard Preview

<img width="1920" height="1080" alt="Screenshot 2025-09-11 201359" src="https://github.com/user-attachments/assets/3eddd0c5-13f2-4011-a96b-88fbc93af155" />
<img width="1920" height="1080" alt="Screenshot 2025-09-11 201455" src="https://github.com/user-attachments/assets/4bd5a8e9-3438-4df7-8c4e-2ff3a917dc0f" />
<img width="1920" height="1080" alt="Screenshot 2025-09-11 201504" src="https://github.com/user-attachments/assets/389a158a-f5c3-4168-b12e-1d81c487e73a" />

---

## 🙌 Acknowledgements

* Dataset: *Global Superstore Dataset*.
* Tools: **Python (Pandas)**, **Power BI**.

---

## 👨‍💻 Author & Copyright

* Author: Harish Chavan.
* © 2025 Harish Chavan. All Rights Reserved.
