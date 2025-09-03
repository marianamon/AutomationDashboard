import subprocess
import sys
# install plotly if missing
subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly", "pandas", "openpyxl"])
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Load data ---
df = pd.read_excel("Automation_Dashboard.xlsx", sheet_name=0)

# --- Initialize optional metrics ---
functional_coverage = None
regression_coverage = None

# --- Main metrics ---
total_cases = df.shape[0] 
automated = df[df["Automation status"].isin(["Automated - E2E", "Automated - Component"])].shape[0]
to_be_automated = df[df["Automation status"] == "To be automated"].shape[0]
not_automated = df[df["Automation status"] == "Will not automate"].shape[0]
total_cases_valid = total_cases - not_automated # Exclude non-automatable cases from coverage calculation
coverage = (automated / total_cases_valid) * 100  if total_cases > 0 else 0

# --- Functional Coverage ---
if "Critical Module" in df.columns:
    critical_modules = df[df["Critical Module"] == "Yes"]["Funcionality"].unique()
    covered_modules = df[
        (df["Critical Module"] == "Yes") &
        (df["Automation status"].isin(["Automated - E2E", "Automated - Component"]))
    ]["Funcionality"].unique()
    
    if len(critical_modules) > 0:
        functional_coverage = (len(covered_modules) / len(critical_modules)) * 100
    else:
        functional_coverage = 0

# --- Regression Coverage ---
if "Regression" in df.columns:
    total_regression = (df["Regression"] == "Yes").sum()
    automated_regression = df[
        (df["Regression"] == "Yes") &
        (df["Automation status"].isin(["Automated - E2E", "Automated - Component"]))
    ].shape[0]
    
    if total_regression > 0:
        regression_coverage = (automated_regression / total_regression) * 100
    else:
        regression_coverage = 0

# --- Dashboard ---
st.title("Automation Dashboard")

# KPIs principales
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Cases", total_cases)
col2.metric("Automated", automated)
col3.metric("Pending", to_be_automated)
col4.metric("Not Automatable", not_automated)
col5.metric("Coverage", f"{coverage:.2f}%")

# --- Side by side charts (centered and wider) ---
# Columnas con proporciones para centrar
left_spacer, col1, col2, right_spacer = st.columns([0.1, 2, 2, 0.1])

with col1:
    # Pie Chart - Automation Coverage (donut style, labels outside)
    fig_pie = px.pie(
        names=["Automated", "To be automated"],
        values=[automated, to_be_automated],
        title="Automation Coverage",
        hole=0.4  # convierte en donut, da más espacio
    )
    fig_pie.update_traces(
        textinfo="percent+label",  # porcentaje + etiqueta
        textposition="outside",   # mueve los labels afuera
        pull=[0.05, 0]            # opcional: resalta el primer slice
    )
    fig_pie.update_layout(
        margin=dict(t=50, b=50, l=50, r=50),  # más márgenes
        showlegend=True
    )
    st.plotly_chart(fig_pie, use_container_width=True)


with col2:
    # Bar Chart - Total Test Scope
    fig_bar = px.bar(
        x=["Total Test Cases", "Automated (E2E + Component)", "To be automated", "Will not automate"],
        y=[total_cases, automated, to_be_automated, not_automated],
        text=[total_cases, automated, to_be_automated, not_automated],
        title="Total Test Scope"
    )
    fig_bar.update_traces(textposition="outside", marker_color="royalblue")
    fig_bar.update_layout(yaxis_title="Count", xaxis_title="", showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)


# --- Gauge charts for Functional & Regression Coverage ---
if functional_coverage is not None or regression_coverage is not None:
    st.subheader("Coverage KPIs")
    col6, col7 = st.columns(2)

    if functional_coverage is not None:
        fig_fc = go.Figure(go.Indicator(
            mode="gauge+number",
            value=functional_coverage,
            title={"text": "Functional Coverage: Percentage of critical modules automated"},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green"}}
        ))
        col6.plotly_chart(fig_fc, use_container_width=True)

    if regression_coverage is not None:
        fig_rc = go.Figure(go.Indicator(
            mode="gauge+number",
            value=regression_coverage,
            title={"text": "Regression Coverage: Percentage of regression cases automated"},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "orange"}}
        ))
        col7.plotly_chart(fig_rc, use_container_width=True)

# --- Data Table ---
st.subheader("Detailed Data")
st.dataframe(df)







