import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import time

st.set_page_config(page_title="VRP Solver Local", layout="wide")
st.title("🚛 VRP Solver: Optimización de Rutas")

# Función para convertir dirección a coordenadas (Lat/Lon)
def geocodificar(direccion):
    geolocator = Nominatim(user_agent="mi_vrp_solver_local")
    try:
        location = geolocator.geocode(direccion, timeout=10)
        return (location.latitude, location.longitude) if location else (None, None)
    except:
        return (None, None)

# Carga de archivos
st.sidebar.header("Carga de Datos")
file1 = st.sidebar.file_uploader("Subir Hoja 1", type=["xlsx", "xls"])
file2 = st.sidebar.file_uploader("Subir Hoja 2", type=["xlsx", "xls"])

if file1 and file2:
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    df = pd.concat([df1, df2])
    
    st.subheader("Vista previa de Sucursales")
    st.dataframe(df.head())
    
    if st.button("Procesar Ubicaciones (Geocodificar)"):
        with st.spinner("Buscando coordenadas en el mapa..."):
            coords = [geocodificar(dir) for dir in df['Direccion']]
            df['Latitud'], df['Longitud'] = zip(*coords)
            st.success("Coordenadas obtenidas")
            st.dataframe(df)
            
            # Aquí conectaríamos el motor OR-Tools en el futuro
            st.info("Ahora el sistema está listo para calcular la ruta óptima.")
