import pandas as pd
import numpy as np

github_url = "https://github.com/GiinaLee/Supply-Chain-Operations-Dashboard/raw/refs/heads/main/Retail-Supply-Chain-Sales-Dataset.xlsx"
df = pd.read_excel(github_url, engine = "openpyxl", sheet_name= "Retails Order Full Dataset")

#calculate and catogorize LT
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Lead_Time_Days"] = (df['Ship Date'] - df['Order Date']).dt.days

def catogorize_LT(date):
    if date <= 3:
        return "short"
    elif date <= 7:
        return "middle"
    else:
        return "long"

df["LT_evaluate"] = df["Lead_Time_Days"].apply(catogorize_LT)

#calculate return rate 
df["Returned_check"] = df["Returned"].apply(lambda x:1 if str(x).lower().strip()== "yes" else 0)

#calculate profit rate
df["Profit_Rate"] = np.where(df["Profit"] > 0, df["Profit"]/df["Sales"], 0)
print(df)

#cleaning data to csv
new_file = "Processing_Retails_Dataset.csv"
df.to_csv(new_file, index=False, encoding= "utf-8-sig")

