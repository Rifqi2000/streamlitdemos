import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# Database connection function
def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_demografi"
    )
    query = "SELECT * FROM demografi_dummy_updated"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# # Streamlit app
# st.title("Visualisasi Data Demografi")

# # Fetch data
# df = get_data()

# # Display raw data
# st.subheader("Data Demografi")
# st.dataframe(df)

# # Selectbox for filtering
# region_choice = st.selectbox("Pilih Wilayah", df["Region"].unique())
# kecamatan_choice = st.selectbox("Pilih Kecamatan", df[df["Region"] == region_choice]["Kecamatan"].unique())
# month_choice = st.selectbox("Pilih Bulan", df["Bulan"].unique())

# # Filter data based on selection
# filtered_df = df[(df["Region"] == region_choice) & (df["Kecamatan"] == kecamatan_choice)]
# filtered_df_month = df[(df["Region"] == region_choice) & (df["Kecamatan"] == kecamatan_choice) & (df["Bulan"] == month_choice)]

# # Visualizations
# st.subheader("Grafik Populasi per Bulan")
# fig1 = px.line(filtered_df, x="Bulan", y="Populasi", title="Tren Populasi per Bulan")
# st.plotly_chart(fig1)

# st.subheader("Jumlah Kelahiran dan Kematian per Bulan")
# fig2 = px.bar(filtered_df, x="Bulan", y=["Jumlah Kelahiran", "Jumlah Kematian"],
#               title="Jumlah Kelahiran dan Kematian per Bulan", barmode='group')
# st.plotly_chart(fig2)

# st.subheader("Distribusi Laki-laki dan Perempuan")
# fig3 = px.pie(filtered_df, names=["Laki-laki", "Perempuan"], values=[filtered_df["Laki-laki"].sum(), filtered_df["Perempuan"].sum()],
#               title="Distribusi Laki-laki dan Perempuan")
# st.plotly_chart(fig3)

# st.subheader("Rasio Kelahiran terhadap Populasi")
# filtered_df["Rasio Kelahiran"] = (filtered_df["Jumlah Kelahiran"] / filtered_df["Populasi"]) * 100
# fig4 = px.line(filtered_df, x="Bulan", y="Rasio Kelahiran", title="Rasio Kelahiran terhadap Populasi (%)")
# st.plotly_chart(fig4)

# st.subheader("Rasio Kematian terhadap Populasi")
# filtered_df["Rasio Kematian"] = (filtered_df["Jumlah Kematian"] / filtered_df["Populasi"]) * 100
# fig5 = px.line(filtered_df, x="Bulan", y="Rasio Kematian", title="Rasio Kematian terhadap Populasi (%)")
# st.plotly_chart(fig5)

# st.subheader("Perbandingan Populasi antar Kecamatan dalam Wilayah")
# average_pop = df[df["Region"] == region_choice].groupby("Kecamatan")["Populasi"].mean().reset_index()
# fig6 = px.bar(average_pop, x="Kecamatan", y="Populasi", title="Rata-rata Populasi antar Kecamatan dalam Wilayah")
# st.plotly_chart(fig6)

# st.subheader("Tren Pertumbuhan Populasi")
# filtered_df["Pertumbuhan Populasi"] = filtered_df["Populasi"].diff()
# fig7 = px.line(filtered_df, x="Bulan", y="Pertumbuhan Populasi", title="Tren Pertumbuhan Populasi")
# st.plotly_chart(fig7)

# st.subheader("Perbandingan Kelahiran dan Kematian per Kecamatan")
# agg_birth_death = df.groupby("Kecamatan")[["Jumlah Kelahiran", "Jumlah Kematian"]].sum().reset_index()
# fig8 = px.bar(agg_birth_death, x="Kecamatan", y=["Jumlah Kelahiran", "Jumlah Kematian"], 
#               title="Perbandingan Kelahiran dan Kematian per Kecamatan", barmode='group')
# st.plotly_chart(fig8)

# # Visualizations based on selected month
# st.subheader(f"Visualisasi Data untuk Bulan {month_choice}")
# fig9 = px.bar(filtered_df_month, x="Kecamatan", y="Populasi", title=f"Populasi di Bulan {month_choice}")
# st.plotly_chart(fig9)

# fig10 = px.bar(filtered_df_month, x="Kecamatan", y=["Jumlah Kelahiran", "Jumlah Kematian"],
#                title=f"Jumlah Kelahiran dan Kematian di Bulan {month_choice}", barmode='group')
# st.plotly_chart(fig10)

# Streamlit app settings
st.set_page_config(page_title="Visualisasi Data Demografi", layout="wide")
st.title("📊 Visualisasi Data Demografi")

# Fetch data
df = get_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Data")
region_choice = st.sidebar.selectbox("Pilih Wilayah", df["Region"].unique())
kecamatan_choice = st.sidebar.selectbox("Pilih Kecamatan", df[df["Region"] == region_choice]["Kecamatan"].unique())
month_choice = st.sidebar.selectbox("Pilih Bulan", df["Bulan"].unique())

# Filter data based on selection
filtered_df = df[(df["Region"] == region_choice) & (df["Kecamatan"] == kecamatan_choice)]
filtered_df_month = df[(df["Region"] == region_choice) & (df["Kecamatan"] == kecamatan_choice) & (df["Bulan"] == month_choice)]

# Display raw data
st.subheader("📋 Data Demografi")
st.dataframe(filtered_df, use_container_width=True)

# Responsive layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("📈 Grafik Populasi per Bulan")
    fig1 = px.line(filtered_df, x="Bulan", y="Populasi", title="Tren Populasi per Bulan")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📊 Rasio Kelahiran terhadap Populasi")
    filtered_df["Rasio Kelahiran"] = (filtered_df["Jumlah Kelahiran"] / filtered_df["Populasi"]) * 100
    fig4 = px.line(filtered_df, x="Bulan", y="Rasio Kelahiran", title="Rasio Kelahiran terhadap Populasi (%)")
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    st.subheader("📊 Jumlah Kelahiran dan Kematian per Bulan")
    fig2 = px.bar(filtered_df, x="Bulan", y=["Jumlah Kelahiran", "Jumlah Kematian"],
                  title="Jumlah Kelahiran dan Kematian per Bulan", barmode='group')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📊 Rasio Kematian terhadap Populasi")
    filtered_df["Rasio Kematian"] = (filtered_df["Jumlah Kematian"] / filtered_df["Populasi"]) * 100
    fig5 = px.line(filtered_df, x="Bulan", y="Rasio Kematian", title="Rasio Kematian terhadap Populasi (%)")
    st.plotly_chart(fig5, use_container_width=True)

st.subheader("📍 Perbandingan Populasi antar Kecamatan dalam Wilayah")
average_pop = df[df["Region"] == region_choice].groupby("Kecamatan")["Populasi"].mean().reset_index()
fig6 = px.bar(average_pop, x="Kecamatan", y="Populasi", title="Rata-rata Populasi antar Kecamatan dalam Wilayah")
st.plotly_chart(fig6, use_container_width=True)

# Monthly Visualizations
st.subheader(f"📅 Visualisasi Data untuk Bulan {month_choice}")
col3, col4 = st.columns(2)
with col3:
    fig9 = px.bar(filtered_df_month, x="Kecamatan", y="Populasi", title=f"Populasi di Bulan {month_choice}")
    st.plotly_chart(fig9, use_container_width=True)
with col4:
    fig10 = px.bar(filtered_df_month, x="Kecamatan", y=["Jumlah Kelahiran", "Jumlah Kematian"],
                   title=f"Jumlah Kelahiran dan Kematian di Bulan {month_choice}", barmode='group')
    st.plotly_chart(fig10, use_container_width=True)
