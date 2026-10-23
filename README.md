# 📊 YouTube Data Visualization Dashboard

An interactive, modular web dashboard built with **Python**, **Plotly Express**, and **Streamlit** to explore and analyze YouTube trends using real-world Kaggle datasets.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Plotly](https://img.shields.io/badge/Plotly-Express-green)

---

## 🚀 Key Features

* **Interactive Visualizations:** Built using **Plotly Express** for dynamic zooming, panning, and rich hover details.
* **Sidebar Filtering:** Filter data dynamically by YouTube category IDs to isolate specific trends.
* **KPI Metric Cards:** Instantly view high-level summaries including total videos analyzed, total views, and total likes.
* **Clean Modular Architecture:** Separates dashboard layout (`app.py`) from visualization logic (`visualizer.py`) for easy scalability.

---

## 📈 Visualizations Included

1. **Views vs. Likes Scatter Plot:** Log-scale scatter plot showcasing audience engagement, with bubble sizes representing comment counts and color coding by category.
2. **Average Views per Category:** Bar chart comparing average viewership performance across different YouTube categories.
3. **Engagement Rate Distribution:** Box plot tracking the distribution of engagement rates `((Likes + Comments) / Views)` per category.
4. **Time Series Trend:** Interactive line chart tracking total views over publication dates with a built-in date range slider.

---

## 📂 Project Structure

```text
youtube_dashboard/
├── requirements.txt      # Required Python packages
├── youtube_data.csv      # Kaggle YouTube dataset (not tracked in git if large)
├── visualizer.py         # Plotly Express chart generation functions
└── app.py                # Main Streamlit web application
