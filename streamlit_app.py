import streamlit as st

st.title("🎈 Jurnalika")
st.write(
    "Kami Bnagga Jadi PERS Kampus [jurnalika.com](https://www.jurnalikanews.com/)."
)
import pandas as pd
import pydeck as pdk
import streamlit as st
import numpy as np

# Menggunakan koordinat pusat Kota Bogor
BOGOR_LAT = -6.5944
BOGOR_LON = 106.7892

# Membuat data acak di sekitar Bogor
# Pembagi [100, 100] membuat sebaran titik lebih rapat/fokus di area kota
rng = np.random.default_rng(0)
data = rng.standard_normal((1000, 2)) / [100, 100] + [BOGOR_LAT, BOGOR_LON]
df = pd.DataFrame(data, columns=["lat", "lon"])

st.title("Visualisasi Data Kota Bogor")

st.pydeck_chart(
    pdk.Deck(
        map_style=None,  # Mengikuti tema Streamlit
        initial_view_state=pdk.ViewState(
            latitude=BOGOR_LAT,
            longitude=BOGOR_LON,
            zoom=12,
            pitch=45,
        ),
        layers=[
            # Layer Hexagon untuk melihat densitas secara 3D
            pdk.Layer(
                "HexagonLayer",
                data=df,
                get_position="[lon, lat]",
                radius=150,
                elevation_scale=50,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            # Layer Scatterplot untuk titik lokasi presisi
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[lon, lat]",
                get_color="[0, 128, 255, 160]", # Warna biru transparan
                get_radius=50,
            ),
        ],
        # Menambahkan tooltip agar interaktif saat kursor diarahkan ke balok
        tooltip={"text": "Jumlah titik di area ini: {elevationValue}"}
    )
)
