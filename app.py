import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="Industrial Cooling Monitor", page_icon="❄️", layout="wide")

st.markdown("""
    <style>
    .stMetric { background: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid #00f2fe; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("❄️ Predictive Thermal Management System")

if 'temp_history' not in st.session_state:
    st.session_state.temp_history = pd.DataFrame(columns=['Time', 'Temp', 'Trend'])

placeholder = st.empty()

for _ in range(100):
    current_temp = round(np.random.uniform(35.0, 50.0), 2)
    last_temp = st.session_state.temp_history['Temp'].iloc[-1] if not st.session_state.temp_history.empty else current_temp
    trend = current_temp - last_temp
    
    new_data = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), current_temp, trend]], 
                            columns=st.session_state.temp_history.columns)
    st.session_state.temp_history = pd.concat([st.session_state.temp_history, new_data]).tail(20)

    with placeholder.container():
        m1, m2, m3 = st.columns(3)
        m1.metric("Current Temperature", f"{current_temp} °C", delta=f"{round(trend, 2)} °C/s")
        m2.metric("Fan Speed", "85%" if trend > 0.5 else "30%", delta="Adaptive")
        m3.metric("System Health", "OPTIMAL" if trend < 1.0 else "WARNING")

        if trend > 0.8:
            st.error("⚠️ PREDICTIVE ALERT: Rapid Temperature Spike Detected!")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=st.session_state.temp_history['Time'], y=st.session_state.temp_history['Temp'], mode='lines+markers', name="Temp"))
        fig.update_layout(title="Thermal Gradient Analysis", template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    time.sleep(2)
