import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos (el usuario debe subir archivo enriquecido con Cluster y Score)
st.set_page_config(layout="wide")
st.title("Análisis de Clientes - Segmentación y ROI")

uploaded_file = st.sidebar.file_uploader("Sube el archivo CSV con columnas: Cluster, Score, Fecha, Response...", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['Dt_Customer'])

    # Filtros generales
    st.sidebar.subheader("Filtros")
    fecha_min = df['Dt_Customer'].min()
    fecha_max = df['Dt_Customer'].max()
    fecha_range = st.sidebar.date_input("Rango de fecha de cliente", [fecha_min, fecha_max])

    selected_clusters = st.sidebar.multiselect("Selecciona Clusters", sorted(df['Cluster'].unique()), default=df['Cluster'].unique())
    score_min, score_max = float(df['Score'].min()), float(df['Score'].max())
    score_slider = st.sidebar.slider("Rango de Score", min_value=score_min, max_value=score_max, value=(score_min, score_max))

    # Aplicar filtros
    df_filt = df[(df['Dt_Customer'] >= pd.to_datetime(fecha_range[0])) &
                 (df['Dt_Customer'] <= pd.to_datetime(fecha_range[1])) &
                 (df['Cluster'].isin(selected_clusters)) &
                 (df['Score'] >= score_slider[0]) &
                 (df['Score'] <= score_slider[1])]

    tab1, tab2, tab3 = st.tabs(["Descriptivo", "Clustering", "Score y ROI"])

    with tab1:
        st.subheader("Análisis Descriptivo")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Clientes", len(df_filt))
            st.metric("Tasa de Compra", f"{df_filt['Response'].mean()*100:.2f}%")
        with col2:
            st.bar_chart(df_filt['Response'].value_counts(normalize=True))

        st.write("Distribución por Edad")
        fig, ax = plt.subplots()
        sns.histplot(df_filt['Age'], bins=20, kde=True, ax=ax)
        st.pyplot(fig)

    with tab2:
        st.subheader("Perfil de Clusters")
        cluster_avg = df_filt.groupby("Cluster")[['Age', 'Income', 'Score']].mean()
        st.dataframe(cluster_avg)

        fig2, ax2 = plt.subplots()
        sns.boxplot(data=df_filt, x='Cluster', y='Income', ax=ax2)
        ax2.set_title("Distribución de Ingresos por Cluster")
        st.pyplot(fig2)

    with tab3:
        st.subheader("Score y Simulación de ROI")

        threshold = st.slider("Selecciona umbral de score", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        contactados = df_filt[df_filt['Score'] >= threshold]
        TP = ((contactados['Response'] == 1)).sum()
        FP = ((contactados['Response'] == 0)).sum()

        ingreso = TP * 48.98
        costo = (TP + FP) * 3
        roi = ingreso - costo

        st.metric("Clientes contactados", len(contactados))
        st.metric("Ingresos estimados", f"{ingreso:.2f} MU")
        st.metric("Costo estimado", f"{costo:.2f} MU")
        st.metric("ROI estimado", f"{roi:.2f} MU")

        fig3, ax3 = plt.subplots()
        sns.histplot(contactados['Score'], bins=20, ax=ax3)
        ax3.set_title("Distribución de Scores en Clientes Contactados")
        st.pyplot(fig3)

else:
    st.info("Por favor sube un archivo CSV para comenzar.")
