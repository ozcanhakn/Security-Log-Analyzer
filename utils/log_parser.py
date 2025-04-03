import pandas as pd

def load_logs(file_path):
    """log dosyasını indirmek ve analiz etmek için"""

    df = pd.read_csv(file_path)

    # Zaman damgasını datetime'a çevir

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Boş değeri kontrol
    df.dropna(inplace=True)

    return df


def get_summary(df):

    """
    Log verisinin özet istatistiklerini döndür.
    """
    summary = {
        "Toplam Giriş": df.shape[0],
        "Benzersiz IP Sayısı": df['ip_address'].nunique(),
        "Hatalı Girişler": df[df['action'] == 'login_failed'].shape[0],
    }
    return summary