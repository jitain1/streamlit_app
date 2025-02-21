import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from datetime import datetime

# --- Set Page Configuration ---
st.set_page_config(page_title="Student Data Dashboard", page_icon="📌", layout="wide")

# --- Styled Header Box (Including Logo & Centered Title) ---
st.markdown(
    """
    <div style='background-color:#0073e6; padding:15px; border-radius:10px; text-align:center;'>
        <h1 style='color:white; margin:0;'>📊 Student Data Dashboard</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Authenticate using Service Account JSON ---
creds = Credentials.from_service_account_file(
    "D:/streamlit_app/bigquery-demo-436010-099787ddf471.json",
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
gc = gspread.authorize(creds)

# --- Open Google Sheet (Corrected String) ---
spreadsheet = gc.open_by_key("1UMpZOBKxe3YghAbQFazyZAZgGcON7YVBDX6e-bUl8wI")

# --- Access "Report1" Sheet ---
worksheet = spreadsheet.worksheet("Report1")

# --- Load Data from Google Sheets ---
data = worksheet.get_all_values()
df = pd.DataFrame(data)
df.columns = df.iloc[0]  # Set first row as header
df = df.drop(0).reset_index(drop=True)

# --- Ensure Required Columns Exist ---
required_columns = [
    'Student Name', 'Gender', 'Class Level', 'Home State', 'Major', 'Extracurricular Activity'
]

for col in required_columns:
    if col not in df.columns:
        df[col] = ""

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Data")
selected_class = st.sidebar.selectbox("Select Class Level", ["All"] + sorted(df['Class Level'].unique()))
selected_major = st.sidebar.selectbox("Select Major", ["All"] + sorted(df['Major'].unique()))

# --- Apply Filters ---
filtered_df = df.copy()
if selected_class != "All":
    filtered_df = filtered_df[filtered_df['Class Level'] == selected_class]
if selected_major != "All":
    filtered_df = filtered_df[filtered_df['Major'] == selected_major]

# --- Display Data ---
st.subheader("📋 Student Records")
st.dataframe(filtered_df, use_container_width=True)

# --- Save Edited Data to Google Sheet ---
if st.button("💾 Save Updated Data"):
    try:
        worksheet.update([filtered_df.columns.values.tolist()] + filtered_df.values.tolist())
        st.success("✅ Data successfully saved to Google Sheets!")
    except Exception as e:
        st.error(f"❌ Error saving data: {e}")
