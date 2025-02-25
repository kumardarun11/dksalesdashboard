# 📊 KD11 Sales Dashboard
## 🔗 **Live Demo:** [KD11 Sales Dashboard](https://dksalesdashboard.streamlit.app/)
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

## 🎥 **Screenshots**

### 1️⃣ Monthly Sales Trend

![image](https://github.com/user-attachments/assets/12eda9a4-9a9b-418b-a9b5-5a64fdac91df)

### 2️⃣ Sales by Region

![image](https://github.com/user-attachments/assets/5bd52757-df77-433f-95e3-8576e336e1dd)

### 3️⃣ Sales by Category

![image](https://github.com/user-attachments/assets/0518375c-417e-4007-87cc-2f9410c55a36)

### 4️⃣ Top Selling Products

![image](https://github.com/user-attachments/assets/fde4ea02-d0fb-4469-a81e-4cc77ff214a4)

### 5️⃣ Profitability Trend

![image](https://github.com/user-attachments/assets/9f6ef55d-9a80-4a15-bf56-09fdd23c9b20)

### 6️⃣ Profitability Trend

![image](https://github.com/user-attachments/assets/d0e79aec-d67e-45f5-b041-019071afba0e)

### 7️⃣ Discount Impact on Sales

![image](https://github.com/user-attachments/assets/e980829f-400e-461f-9f8e-63c6215308d4)

### 8️⃣ Sales vs Profit Correlation

![image](https://github.com/user-attachments/assets/613563cf-19cd-46c9-84d5-28b21cf67dc4)


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

