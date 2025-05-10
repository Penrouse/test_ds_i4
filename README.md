# Prueba Data Science

🟦 Optimización de Campañas Directas con Analítica Predictiva y Segmentación

    🧩 Empresa con múltiples categorías de productos y canales de venta.

    📉 Campañas anteriores con baja rentabilidad (ROI negativo).

    🎯 Objetivo: Identificar clientes con alta probabilidad de compra para optimizar la próxima campaña de marketing directo.

    🛠️ Enfoque: análisis descriptivo, clustering y modelo predictivo con simulación de ROI.


🟨 Identificación de 4 Clusters Estratégicos

| Cluster | Descripción                     | Ingreso  | Tasa de Compra | Recomendación        |
| ------- | ------------------------------- | -------- | -------------- | -------------------- |
| 0       | Jóvenes con hijos, bajo ingreso | Bajo     | 11.6%          | Baja prioridad       |
| 1       | Digitales premium, sin hijos    | Alto     | **23.5%**      | ✅ Objetivo principal |
| 2       | Ultra exclusivos por catálogo   | Muy alto | 0%             | Excluir              |
| 3       | Adultos mayores multicanal      | Medio    | 10.3%          | Target secundario    |


🟩 Predicción de probabilidad de compra por cliente

    📊 Modelo: XGBoost entrenado con variables sociodemográficas y de comportamiento.

    🧠 Métricas: AUC > 0.85, F1 > 0.60 (alto desempeño).

    🏷️ Cada cliente recibe un score de propensión de compra entre 0 y 1.


🟧 Simulación de ROI en función del score

| Umbral | Contactados | Tasa éxito | ROI Estimado    |
| ------ | ----------- | ---------- | --------------- |
| 0.30   | 54          | 64.8%      | +1,552 MU       |
| 0.35   | 51          | **68.6%**  | **+1,561 MU** ✅ |
| 0.40   | 51          | 68.6%      | +1,561 MU       |
| 0.50   | 44          | 70.5%      | +1,386 MU       |


🟪 Streamlit App para gestión de campañas

    🔍 Visualización dinámica de segmentos y scores

    🧮 Simulación de ROI en tiempo real

    🎛️ Filtros por fecha, cluster, score

    ✅ Herramienta lista para toma de decisiones por marketing

![alt text](data/2025-05-10-08-19-18.gif)