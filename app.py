import streamlit as st
from utils.log_parser import load_logs, get_summary
from models.anomaly_detection import detect_anomalies

# Streamlit başlığı
st.title("🔍 Siber Güvenlik Log Analiz Dashboard")

# Log dosyasını oku
df = load_logs("data/security_logs.csv")

# Genel bilgiler
summary = get_summary(df)
st.write("**Genel Log İstatistikleri:**")
st.json(summary)

# Şüpheli girişler
anomalies = detect_anomalies(df)
st.write("**Şüpheli Hareketler:**")
st.dataframe(anomalies)
