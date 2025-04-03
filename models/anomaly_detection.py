import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """
    Anomali tespiti için Isolation Forest kullan.
    """
    df['hour'] = df['timestamp'].dt.hour
    df['failed_login'] = df['action'].apply(lambda x: 1 if x == 'login_failed' else 0)

    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df[['hour', 'failed_login']])

    anomalies = df[df['anomaly'] == -1]
    return anomalies
