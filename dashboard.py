%%writefile dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Bike Sharing Dataset (day).csv')

df["dteday"] = pd.to_datetime(df["dteday"])

average_rentals_by_season = df.groupby('season')['cnt'].mean().reset_index()

min_date = df["dteday"].min()
max_date = df["dteday"].max()

with st.sidebar:
    st.image("https://img.okezone.com/content/2015/11/09/15/1246377/yamaha-motors-segera-rilis-dua-sepeda-santai-xeiJ3zqFvd.jpg")

    start_date, end_date = st.date_input(
    label='Rentang Waktu',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
    )

# Main content
st.title("Bike Sharing Daily")

st.write("Rata-Rata Jumlah Peminjaman Sepeda Berdasarkan Musim")
st.bar_chart(average_rentals_by_season.set_index('season'))

st.write("Korelasi antara Variabel Cuaca dan Jumlah Peminjaman Sepeda")
correlation_matrix = df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
st.pyplot(heatmap.get_figure())
