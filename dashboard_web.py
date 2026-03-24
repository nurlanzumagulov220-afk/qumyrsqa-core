import streamlit as st
import pandas as pd
import pydeck as pdk

# Настройка стиля страницы
st.set_page_config(page_title="Mining 4.0: GuardAI & ISU Swarm", layout="wide")

st.title("🐝 Интеллектуальный центр управления роем «Майнинг 4.0»")
st.markdown("---")

# --- УРОВЕНЬ 2: ИНТЕЛЛЕКТУАЛЬНЫЙ СИНТЕЗ (Cognition Layer) ---
with st.sidebar:
    st.header("🧠 Cognition Layer")
    st.subheader("Narrative AI")
    st.info("Назначена машина №101: ближайшая к зоне риска (5 км), 100% совместимость, SpO2 водителя 98%.")
    
    st.subheader("Консенсус-барометр")
    st.progress(92, text="Уверенность роя: 92%")
    
    st.subheader("KPI Эффективности")
    st.metric("Снижение пробега", "-40%", "Оптимально")
    st.metric("Простои", "-52%", delta_color="inverse")
    st.metric("Объяснимость ИИ", "100%")

# --- УРОВЕНЬ 1: 3D ЦИФРОВОЙ ДВОЙНИК (Адаптивное восприятие) ---
st.subheader("🌐 Уровень 1: 3D Цифровой двойник (Поле феромонов)")

# Данные феромонов (Стигмергия)
map_data = pd.DataFrame({
    'lat': [47.1, 47.12, 47.11, 47.105],
    'lon': [51.9, 51.92, 51.91, 51.915],
    'type': ['Маршрут (Синий)', 'РИСК (Красный)', 'Техника', 'Цель'],
    'radius': [100, 400, 200, 300],
    'color': [[0, 100, 255, 100], [255, 0, 0, 200], [255, 255, 0, 150], [0, 255, 0, 150]]
})

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(latitude=47.11, longitude=51.91, zoom=12, pitch=45),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=map_data,
            get_position='[lon, lat]',
            get_color='color',
            get_radius='radius',
            pickable=True
        ),
    ],
    tooltip={"text": "Объект: {type}"}
))

# --- УРОВЕНЬ 3: АКТИВНОЕ УПРАВЛЕНИЕ (Action Layer) ---
st.markdown("---")
st.subheader("⚡ Уровень 3: Активное управление и Handoff")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("**Automatic Handoff**")
    st.button("🔴 ПЕРЕДАТЬ ЗАЯВКУ (Приоритет 55%)", use_container_width=True)

with col2:
    st.write("**Оптимизация Multi-stop**")
    st.code("База -> Склад -> Сектор Б-12 (Риск) -> Скважина 5", language="markdown")

with col3:
    st.write("**The Bid (Тендер)**")
    st.bar_chart({"Машина 101": 0.95, "Машина 105": 0.65, "Машина 202": 0.40})

st.success("🤖 Рой работает автономно. Консенсус достигнут.")