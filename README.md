# 📊 DK Sales Dashboard

## 🚀 Overview

DK Sales Dashboard is an **interactive sales analysis tool** built with **Streamlit, Pandas, and Plotly**.\
It allows businesses to **visualize sales trends, analyze profit margins, and explore product performance** using an intuitive dashboard.

### 🎯 **Key Features**

- 📈 **Sales & Profit Trends**: View monthly sales and profitability over time.
- 🌍 **Regional Analysis**: Compare sales performance across different regions.
- 📂 **Category Insights**: See which product categories generate the most revenue.
- 🛒 **Top-Selling Products**: Identify the best-performing products.
- 🔖 **Discount Impact**: Analyze how discounts affect sales.
- 📊 **Sales vs Profit Correlation**: Visualize the relationship between sales and profit.

---

## ⚙️ **Installation & Setup**

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/dk-sales-dashboard.git
cd dk-sales-dashboard
```

### **2️⃣ Install Dependencies**

Make sure you have **Python 3.8+** installed.\
Then, install the required Python libraries:

```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Application**

```sh
streamlit run app.py
```

This will open the **interactive dashboard in your web browser**.

---

## 📂 **Project Structure**

```
dk-sales-dashboard/
│── sales_data.csv      # Sample sales dataset
│── app.py              # Streamlit dashboard code
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
```

---

## 🚀 **Deployment on Streamlit Cloud**

You can **host this dashboard for free** on **Streamlit Cloud**.

### **Steps to Deploy**

1. **Push your project to GitHub**:
   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. **Go to **[**Streamlit Cloud**](https://share.streamlit.io/) and sign in.
3. **Click "Deploy an App"** → Select your GitHub repository.
4. Set the **Main file path** to:
   ```
   app.py
   ```
5. Click **Deploy** 🎉.

---

## 🎯 **Usage Instructions**

- Use the **sidebar filters** to explore data by **Year, Month, Region, and Category**.
- View **monthly sales and profit trends** using **interactive charts**.
- Analyze **discount impact on sales** and **top-selling products**.
- Use the **Sales vs Profit correlation graph** to identify the best-performing products.

---

## 🛠 **Troubleshooting & FAQs**

#### **Q1: "ModuleNotFoundError: No module named 'plotly'"**

✅ Run:

```sh
pip install -r requirements.txt
```

or install manually:

```sh
pip install plotly pandas streamlit
```

#### **Q2: "Error: sales\_data.csv not found"**

✅ Ensure `sales_data.csv` is in the same directory as `app.py`.\
If missing, re-download it or generate a new dataset.

#### **Q3: "Deployment not working on Streamlit Cloud"**

✅ Make sure:

- Your repository is **public**.
- You have **pushed all required files** (`app.py`, `sales_data.csv`, `requirements.txt`).
- `requirements.txt` includes:
  ```
  streamlit
  pandas
  plotly
  ```

---

## 🏆 **Contributing**

Feel free to **contribute improvements, new features, or bug fixes**!

1. **Fork the repository**.
2. **Create a new branch** (`feature-xyz`).
3. **Commit your changes** and submit a **Pull Request**.

---

## 📜 **License**

This project is **open-source** and free to use.

---

## 👨‍💻 **Author**

Developed by **D ARUN KUMAR**\
📧 Contact: [*kumardarun11@gmail.com*](mailto\:kumardarun11@gmail.com)\
🔗 LinkedIn: **www.linkedin.com/in/kumardarun11**

