

import streamlit as st
import plotly.express as px
import pandas as pd

# Set page config
st.set_page_config(layout="wide")

# Custom CSS for improved styling
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f0f0;
        }
        .sidebar .sidebar-content .sidebar-section {
            margin-bottom: 20px;
        }
        .sidebar .sidebar-content .stButton {
            background-color: #2E8B57;
            color: #ffffff;
            font-weight: bold;
        }
        .sidebar .sidebar-content .stTextInput {
            background-color: #ffffff;
            color: #000000;
        }
        .main .block-container {
            padding: 20px;
        }
        .main .stPlotlyChart {
            max-width: 100%;
        }
        footer {
            text-align: center;
            margin-top: 20px;
            color: #808080;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Title
st.title("AI in LPM: Strategic Alignment MVP")

# Sidebar
st.sidebar.header("Settings")
project_name = st.sidebar.text_input("Enter Project Name", "Project ABC")
resource_capacity = st.sidebar.number_input("Resource Capacity", min_value=1, max_value=100, value=50)
risk_threshold = st.sidebar.slider("Risk Threshold", min_value=0, max_value=100, value=50)
budget = st.sidebar.number_input("Project Budget ($)", min_value=0, value=10000)
actual_costs = st.sidebar.number_input("Actual Costs ($)", min_value=0, value=8000)

# Main content
st.subheader("Project Overview")
st.write(f"Project Name: {project_name}")
st.write(f"Resource Capacity: {resource_capacity}")
st.write(f"Risk Threshold: {risk_threshold}%")

# Automated Resource Allocation Suggestions (Dummy Example)
if st.sidebar.button("Generate Resource Allocation Suggestions"):
    suggestions = {"Resource A": 25, "Resource B": 30, "Resource C": 45}
    st.write("Automated Resource Allocation Suggestions:")
    st.write(suggestions)

# Resource Allocation
st.subheader("Resource Allocation")
resource_chart_data = {'Resource A': 30, 'Resource B': 20, 'Resource C': 50}
resource_chart = st.bar_chart(resource_chart_data)

# Roadmap Planning with Enhanced Visualization
st.subheader("Roadmap Planning")
st.write("AI-Driven Roadmap Recommendations:")
st.write("- Adjust timeline for Milestone 1")
st.write("- Allocate additional resources for Task X")

# Enhanced Roadmap Visualization
timeline_data = {'Task': ['Task 1', 'Task 2', 'Task 3', 'Task 4'],
                 'Start Date': ['2024-06-01', '2024-06-15', '2024-07-01', '2024-07-15'],
                 'End Date': ['2024-06-10', '2024-06-30', '2024-07-10', '2024-07-31']}
df_timeline = pd.DataFrame(timeline_data)

fig_timeline = px.timeline(df_timeline, x_start='Start Date', x_end='End Date', y='Task', color='Task')
fig_timeline.update_layout(title='Project Roadmap Timeline', xaxis_title='Timeline')
roadmap_chart = st.plotly_chart(fig_timeline)

# AI-driven Risk Prediction and Analysis (Dummy Example)
st.subheader("Risk Management")
risk_chart_data = {'Risk Type 1': 25, 'Risk Type 2': 50, 'Risk Type 3': 10}
risk_chart = st.line_chart(risk_chart_data)

if st.sidebar.button("Predict Project Risks"):
    predicted_risks = {"Risk Type 1": "Low", "Risk Type 2": "Medium", "Risk Type 3": "Low"}
    st.write("Predicted Project Risks:")
    st.write(predicted_risks)

# Performance Analytics with Enhanced Visualizations
st.subheader("Performance Analytics")
st.write("Key Performance Indicators (KPIs):")

# Historical KPI Trends
kpi_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            'KPI 1': [80, 85, 90, 88, 85],
            'KPI 2': [70, 75, 72, 80, 78]}
df_kpi = pd.DataFrame(kpi_data)

fig_kpi = px.line(df_kpi, x='Month', y=['KPI 1', 'KPI 2'], title='Historical KPI Trends')
fig_kpi.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
performance_chart = st.plotly_chart(fig_kpi)

# Intelligent Task Prioritization (Dummy Example)
st.subheader("Task Prioritization")
if st.sidebar.button("Prioritize Tasks"):
    prioritized_tasks = ["Task X", "Task Y", "Task Z"]
    st.write("Prioritized Tasks:")
    for task in prioritized_tasks:
        st.write(task)

# Collaboration Tools with File Uploads and Task Assignment
st.subheader("Collaboration Tools")
st.text_area("Team Discussions", "Enter your comments here...")

# File Uploads
uploaded_file = st.file_uploader("Upload Files", type=['pdf', 'docx'])

# Task Assignment
assigned_task = st.text_input("Assign Task", "Task Name")

# Footer
st.markdown("© 2024 International Business Consultants, LLC.")

