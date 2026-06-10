# 🦠 Pakistan COVID-19 Tracking Dashboard

An interactive, localized data visualization web application built with **Streamlit**, **Pandas**, and **Plotly Express**. This dashboard eliminates global data noise to provide a high-performance, deep dive into the historical progression of the COVID-19 pandemic specifically within Pakistan.

---

## Features

* **Data Cleaning & Imputation:** Implements advanced data engineering strategies like time-series and zero imputation to handle real-world reporting gaps seamlessly.
* **Noise Reduction via Smoothing:** Visualizes trends using **7-day rolling averages** (`new_cases_smoothed` & `new_deaths_smoothed`) to eliminate erratic weekend reporting spikes and expose true pandemic waves.
* **High-Performance Architecture:** Optimized by slicing a massive 92 MB global dataset down to a lightweight, Pakistan-specific localized CSV, backed by Streamlit’s native caching mechanisms (`@st.cache_data`).
* **Fully Interactive Visualizations:** Built with Plotly Express, featuring hover tooltips, click-and-drag panning, and dynamic zoom capabilities.

---

## Tech Stack

* **Frontend Framework:** Streamlit (Web Application UI)
* **Data Manipulation & Engineering:** Python 3, Pandas, NumPy
* **Interactive Data Visualization:** Plotly Express
* **Development Environment:** Jupyter Notebook (`.ipynb`) for prototyping & VS Code for assembly

---

## Dataset Information

The data utilized in this project is sourced from the gold-standard **Our World in Data (OWID)** COVID-19 public repository, reflecting official metrics compiled from the World Health Organization (WHO) and Johns Hopkins University.

Key metrics tracked include:
* Cumulative Confirmed Cases & Running Mortality Tallies (`total_cases`, `total_deaths`)
* Raw Daily Influx (`new_cases`, `new_deaths`)
* 7-Day Smoothed Trendline Dimensions (`new_cases_smoothed`, `new_deaths_smoothed`)

---