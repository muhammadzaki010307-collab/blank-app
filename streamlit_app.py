import streamlit as st

st.title("🎈 Jurnalika")
st.write(
    "Kami Bnagga Jadi PERS Kampus [jurnalika.com](https://www.jurnalikanews.com/)."
)
import pandas as pd
import streamlit as st
import numpy as np

# 1. Tentukan koordinat pusat Kota Bogor
BOGOR_LAT = -6.5944
BOGOR_LON = 106.7892

# 2. Buat data acak di sekitar Bogor
# Pembagi [150, 150] membuat sebaran titik tetap berada di dalam area kota
rng = np.random.default_rng(0)
data = rng.standard_normal((1000, 2)) / [150, 150] + [BOGOR_LAT, BOGOR_LON]

df = pd.DataFrame(data, columns=["lat", "lon"])

# 3. Tampilkan judul dan peta
st.title("Peta Sebaran Titik di Bogor")
st.map(df)
