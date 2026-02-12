# ❄️ Predictive Industrial Cooling System

A smart thermal management platform designed for industrial motors and server racks, utilizing predictive analytics to prevent overheating through adaptive cooling.

## 🚀 Features
- **Early Warning System:** Predicts temperature spikes based on $dT/dt$ (Rate of change).
- **PWM Adaptive Fan Control:** Adjusts fan speed dynamically to save energy and reduce noise.
- **Health Diagnostics:** Tracks cooling efficiency over time to detect dusty filters or failing fans.
- **Cloud Interface:** Remote monitoring and threshold adjustment via Streamlit.

## ⚙️ Engineering Logic
- **Hardware:** ESP32 reads high-precision temperature data from a DS18B20 sensor.
- **Software:** The Python engine calculates the "Thermal Velocity" to trigger alerts before the critical threshold is reached.
