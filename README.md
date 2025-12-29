# 🚴‍♀️ Cycle Store Sales Analysis | Power BI Dashboard

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2972/2972185.png" width="600" alt="Cycle Store Banner"/>

  <h3>📊 Sales, Customer & Inventory Intelligence Report</h3>

  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
  <img src="https://img.shields.io/badge/DAX-4285F4?style=for-the-badge&logo=microsoftpowerbi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Power%20Query-00B4D8?style=for-the-badge&logo=microsoftpowerbi&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQL-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
</div>

---

## 🎯 Project Overview

This project presents an **end-to-end sales analysis** of a **Cycle Store retail database** using **Power BI**.  
The dashboard focuses on **sales performance, customer behavior, product demand, store efficiency, staff contribution, and inventory health**.

The goal is to convert raw relational data into **actionable business insights** for decision-making.

---

## 🗂️ Dataset Information

The dataset represents a real-world retail scenario and consists of **9 interconnected tables**.

| Table Name | Description |
|----------|-------------|
| **brands** | Brand details of products |
| **categories** | Product category classification |
| **customers** | Customer demographic data |
| **orders** | Order-level transaction data |
| **order_items** | Item-level sales details |
| **products** | Product master information |
| **staffs** | Sales staff details |
| **stores** | Store location data |
| **stocks** | Inventory quantity by store |

---

## 🔗 Data Model & Relationships

- Categories → Products (1:M)  
- Brands → Products (1:M)  
- Customers → Orders (1:M)  
- Orders → Order Items (1:M)  
- Products → Order Items (1:M)  
- Stores → Staffs (1:M)  
- Stores → Stocks (1:M)  

✔ Star-schema inspired model  
✔ Optimized relationships  
✔ Date hierarchy used for time intelligence  

---

## 🧹 Data Cleaning & Transformation

Performed using **Power Query**:
- Removed duplicates and null values  
- Standardized column names & data types  
- Created calculated columns:
  - Order Year
  - Order Month
  - Revenue at item level  
- Ensured data integrity across tables  

---

## 🛠️ Technical Capabilities

### 📋 Data Processing Pipeline
```
Raw Data → Cleaning & Transformation → DAX Calculations → Interactive Dashboards → Business Insights
```

<table>
<tr>
<td width="25%">

### 🔧 **Data Preparation**
- Missing data handling
- Data type conversions
- ETL processes
- Quality validation

</td>
<td width="25%">

### 📊 **Analysis & KPIs**
- Business metrics design
- Performance indicators
- Trend analysis
- Comparative studies

</td>
<td width="25%">

### 🎨 **Visualization**
- Interactive dashboards
- Dynamic filtering
- Custom visuals
- Mobile responsive

</td>
<td width="25%">

### 💼 **Business Intelligence**
- Actionable insights
- Strategic recommendations
- Performance monitoring
- Decision support

</td>
</tr>
</table>

--- 
## 📈 Key Features

<div align="center">

| Feature | Capability | Business Value |
|---------|------------|----------------|
| **🔍 Real-time Analytics** | Live data connections | Up-to-date insights |
| **📊 Interactive Dashboards** | Dynamic filtering & drilling | Self-service analytics |
| **📱 Mobile Ready** | Responsive design | Anywhere access |
| **🎯 Custom KPIs** | Business-specific metrics | Targeted performance tracking |
</div>

--- 

📁 Repository Structure :

📦 Cycle-Store-Sales-Analysis\
├── 📂 data\
│   ├── brands.csv\
│   ├── categories.csv\
│   ├── customers.csv\
│   ├── orders.csv\
│   ├── order_items.csv\
│   ├── products.csv\
│   ├── staffs.csv\
│   ├── stores.csv\
│   └── stocks.csv\
├── 📂 dashboard-content\
│   ├── dashboard_overview.png\
│   ├── sales_analysis.png\
│   ├── customer_insights.png\
│   ├── product_performance.png\
│   └── inventory_analysis.png\
└── 📄 README.md

---


## 👩‍💻 Author

**Rashmi Sharma**  
_Data Analyst • Data Science • Python • Machine Learning_

## 📞 Connect

<div align="center">

[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rashmisharma6172610@gmail.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rashmi%20Sharma-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rashmi-sharma-745201395/)



[![Medium](https://img.shields.io/badge/Medium-@rashmisharma6172610-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@rashmisharma6172610)

---

<p align="center">
⭐ If you found this project helpful, please consider giving it a star!
</p>

<p align="center">
© 2025 Rashmi Sharma • Data Science & Machine Learning
</p>



