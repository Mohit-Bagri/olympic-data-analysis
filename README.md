# 🏅 Olympic Data Analysis Web App

An interactive **Streamlit-based dashboard** to explore **120+ years of Olympic Games data**.  
This project visualizes how sports, athletes and countries have evolved over time — helping you discover key trends and success patterns in the Olympics.

---
## 🌍 Live App

🚀 **Check it out here:**  
🔗 [Olympic Data Analysis on Streamlit Cloud](https://mohit-bagri-olympic-data-analysis-app-dlgs6c.streamlit.app/)

---

## 🧠 Objectives

- Build a **data-driven web app** using Streamlit.  
- Analyze Olympic history — athletes, sports, events and medals.  
- Visualize performance trends of **countries** and **athletes** across years.  
- Strengthen Python, Pandas and Matplotlib/Seaborn visualization skills.  
- Learn how to design a clean & responsive Streamlit dashboard.

---

## 📂 Project Workflow

### 🔹 1. Data Preparation
- Cleaned and merged **Athlete Events** and **NOC Regions** datasets.  
- Handled missing values and standardized country names.  
- Created helper functions for filtering, grouping and summarizing data.

### 🔹 2. Streamlit Dashboard Setup
- Built with `streamlit` and `matplotlib/seaborn`.  
- Added dropdowns and sidebar filters for:
  - Year  
  - Country  
  - Sport  
  - Medal Type

### 🔹 3. Key Analysis Features
- **Overall Statistics:**  
  Total number of editions, nations, athletes, events, and sports.
  
- **Medal Tally:**  
  Year-wise and country-wise medal breakdowns.

- **Country-wise Analysis:**  
  Trend of medals over time, most successful athletes from a country.

- **Athlete-wise Analysis:**  
  Distribution of athlete ages, performance by sport, and gender comparison.


---

## 🧰 Technologies Used

- **Python 3**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Streamlit**

---

## 📂 Project Structure
```
Olympic-web-app/
│
├── app.py
├── helper.py
├── preprocess.py
├── athlete_events.csv
├──  noc_regions.csv
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

1. Clone this repository:

    ```bash
    git clone https://github.com/Mohit-Bagri/Olympic-web-app.git
    ```

2. Navigate to the folder:

    ```bash
    cd Olympic-web-app
    ```

3. Activate the virtual environment (if applicable):

    ```bash
    source .venv/bin/activate     # Mac / Linux
    .venv\Scripts\activate        # Windows
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

---

## 📈 Future Enhancements
- Add a **search filter** for specific athletes or events.  
- Include **interactive charts** using Plotly.  
- Add a **world map visualization** for medal distribution.  
- Enhance UI/UX with custom CSS and animations.  
- Deploy on **Streamlit Cloud** or **Render** for public access.

---
