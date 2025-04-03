import pandas as pd
import random
from datetime import datetime, timedelta

# Rastgele IP adresleri ve kullanıcılar
ip_addresses = ["192.168.1.10", "192.168.1.15", "192.168.1.20", "192.168.1.5", "192.168.1.8"]
usernames = ["admin", "user1", "user2", "root", "user3", "guest"]
actions = ["login_success", "login_failed"]

# Rastgele log verisi oluştur
log_data = []
start_time = datetime(2024, 4, 2, 8, 0, 0)

for _ in range(100):  # 100 satır log üret
    timestamp = start_time + timedelta(minutes=random.randint(1, 30))
    ip = random.choice(ip_addresses)
    user = random.choice(usernames)
    action = random.choice(actions)
    log_data.append([timestamp, ip, user, action])

# Veriyi DataFrame'e çevir
df = pd.DataFrame(log_data, columns=["timestamp", "ip_address", "username", "action"])

# CSV dosyası olarak kaydet
df.to_csv("data/security_logs.csv", index=False)

print("Log dosyası başarıyla oluşturuldu: data/security_logs.csv")
