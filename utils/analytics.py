import pandas as pd
import time

log_file = "query_log.csv"

def log_query(query, response):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame([[ts, query, response]], columns=["timestamp", "query", "response"])
    df.to_csv(log_file, mode="a", header=False, index=False)

def load_logs():
    try:
        return pd.read_csv(log_file, names=["timestamp", "query", "response"])
    except:
        return pd.DataFrame(columns=["timestamp", "query", "response"]) 