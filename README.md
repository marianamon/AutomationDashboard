# 🧪 Automation Dashboard

A simple and interactive **Test Automation Dashboard** built with [Streamlit](https://streamlit.io/), [Pandas](https://pandas.pydata.org/), and [Plotly](https://plotly.com/python/).  
It provides key insights into automation progress, functional coverage, and regression coverage using live data from an Excel file.

---

## 🚀 Features
- **KPIs at a glance**:
  - Total test cases
  - Automated cases
  - Pending cases
  - Non-automatable cases
  - Overall automation coverage (%)
- **Coverage charts**:
  - Pie chart of automation distribution
  - Bar chart of total test scope
  - Gauge indicators for:
    - Functional Coverage (% of critical modules covered)
    - Regression Coverage (% of regression cases automated)
- **Detailed data table** to explore test cases directly inside the app
- **Live data from Excel**:
  - Supports local file (`Automation_Dashboard.xlsx`)  
  - Or remote file via public **URL**

---

## 🛠️ Tech Stack
- **[Python 3.9+](https://www.python.org/)**
- **[Streamlit](https://streamlit.io/)** – Web framework for interactive dashboards
- **[Pandas](https://pandas.pydata.org/)** – Data processing
- **[Plotly](https://plotly.com/)** – Interactive visualizations

---

## 📂 Project Structure
automation_dashboard/
│── app.py # Main Streamlit app
│── requirements.txt # Dependencies for deployment
│── Automation_Dashboard.xlsx (optional, local testing)
│── README.md # Documentation

Install dependencies
pip install -r requirements.txt

3. Run locally
streamlit run app.py


The app will be available at http://localhost:8501.

🌐 Deploy to Streamlit Cloud

Push this repo to GitHub (including app.py, requirements.txt, and optionally your Excel file).

Go to Streamlit Community Cloud
 and sign in with GitHub.

Select your repo and deploy.

Your app will be live at:

https://<your-app-name>.streamlit.app

🔗 Data Source Options

Local file: Place Automation_Dashboard.xlsx in the repo root.

Remote URL: Update app.py with your file link:

url = "https://your-server.com/Automation_Dashboard.xlsx"
df = pd.read_excel(url, sheet_name=0)

📊 Example KPIs

Functional Coverage → Percentage of critical modules covered by automation.

Regression Coverage → Percentage of regression test cases automated.

Automation Coverage → Automated cases ÷ (Total cases – Not automatable).

✅ Requirements

Your requirements.txt should contain:

streamlit
pandas
plotly
openpyxl
