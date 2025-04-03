import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Log dosyasını yükle
log_file = "data/security_logs.csv"

@st.cache_data  # 🔥 Performans için cache mekanizması ekledik
def load_data():
    df = pd.read_csv(log_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Zamanı datetime objesine çevir
    return df

df = load_data()

# 📌 Genel İstatistikler
total_logins = len(df)
unique_ips = df["ip_address"].nunique()
failed_logins = df[df["action"] == "login_failed"].shape[0]

# 📊 **Streamlit Arayüzü**
st.title("🔍 Siber Güvenlik Log Analizi")

st.sidebar.header("📊 İstatistikler")
st.sidebar.write(f"**Toplam Giriş:** {total_logins}")
st.sidebar.write(f"**Benzersiz IP Sayısı:** {unique_ips}")
st.sidebar.write(f"**Hatalı Girişler:** {failed_logins}")

# 📊 **1️⃣ Başarılı & Başarısız Girişler (Pie Chart)**
st.subheader("🛡️ Başarılı & Başarısız Girişler")
fig, ax = plt.subplots()
df["action"].value_counts().plot.pie(autopct="%1.1f%%", labels=["Başarılı", "Başarısız"], colors=["green", "red"], ax=ax)
st.pyplot(fig)

# 📊 **2️⃣ En Çok Giriş Yapan IP'ler (Bar Chart)**
st.subheader("🌍 En Çok Giriş Yapan IP'ler")
fig, ax = plt.subplots()
top_ips = df["ip_address"].value_counts().head(5)  # İlk 5 IP
sns.barplot(x=top_ips.index, y=top_ips.values, palette="Blues_r", ax=ax)
ax.set_xlabel("IP Adresi")
ax.set_ylabel("Giriş Sayısı")
st.pyplot(fig)

# 📊 **3️⃣ Zaman Bazlı Giriş Analizi (Line Chart)**
st.subheader("📅 Zaman Bazlı Giriş Analizi")
df["hour"] = df["timestamp"].dt.hour  # Saat bilgisini çıkart
hourly_counts = df["hour"].value_counts().sort_index()
fig, ax = plt.subplots()
sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker="o", ax=ax)
ax.set_xlabel("Saat")
ax.set_ylabel("Giriş Sayısı")
st.pyplot(fig)

# 🕵️ **4️⃣ Şüpheli IP'leri Listele**
st.subheader("🚨 Şüpheli IP Adresleri")
threshold = 5  # 5'ten fazla başarısız giriş yapanları şüpheli say
suspicious_ips = df[df["action"] == "login_failed"]["ip_address"].value_counts()
suspicious_ips = suspicious_ips[suspicious_ips > threshold]

if not suspicious_ips.empty:
    st.write(suspicious_ips)
else:
    st.write("✅ Şüpheli IP bulunamadı.")

