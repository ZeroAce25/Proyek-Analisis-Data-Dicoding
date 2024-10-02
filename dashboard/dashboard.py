import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat dataset
day_df = pd.read_csv('https://raw.githubusercontent.com/ZeroAce25/Proyek-Analisis-Data-Dicoding/refs/heads/main/data/day.csv?token=GHSAT0AAAAAACYLT5WDACIEQURW7XICDZTQZX5M5KA')  # Ganti dengan path yang sesuai
# Pastikan kolom 'dteday' bertipe datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Judul aplikasi
st.title('Bike Sharing Data Analysis')

# Widget kalender untuk menentukan rentang tanggal
start_date = st.date_input('Select Start Date', value=day_df['dteday'].min())
end_date = st.date_input('Select End Date', value=day_df['dteday'].max())

# Filter data berdasarkan rentang tanggal
filtered_data = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

# Visualisasi Pengaruh Cuaca terhadap Penyewaan
st.header('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda')

# Boxplot untuk casual dan registered
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
sns.boxplot(x='weathersit', y='casual', data=filtered_data, ax=ax[0])
ax[0].set_title('Casual Rentals by Weather Conditions')
ax[0].set_xlabel('Weather Conditions')
ax[0].set_ylabel('Casual Rentals')

sns.boxplot(x='weathersit', y='registered', data=filtered_data, ax=ax[1])
ax[1].set_title('Registered Rentals by Weather Conditions')
ax[1].set_xlabel('Weather Conditions')
ax[1].set_ylabel('Registered Rentals')

plt.tight_layout()
st.pyplot(fig)

# Visualisasi Tren Penyewaan Berdasarkan Musim
st.header('Tren Penyewaan Sepeda Berdasarkan Musim')

# Rata-rata penyewaan berdasarkan musim
season_avg = filtered_data.groupby('season')[['casual', 'registered', 'cnt']].mean().reset_index()

# Line plot untuk tren penyewaan
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=season_avg, x='season', y='casual', label='Casual Rentals', marker='o')
sns.lineplot(data=season_avg, x='season', y='registered', label='Registered Rentals', marker='o')

ax2.set_title('Average Rentals by Season')
ax2.set_xlabel('Season')
ax2.set_ylabel('Average Rentals')
ax2.set_xticks(range(4))
ax2.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
plt.legend()
st.pyplot(fig2)

# Menampilkan data yang difilter (opsional)
st.subheader('Data Bikeset')
st.write(day_df)
