import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/<"309297996">/export?format=csv'
data = pd.read_csv(url)
print(data.head())

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe

# Setup akses
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Buka Google Sheet dan pilih sheet tertentu
sheet = client.open("total_anggaran").worksheet("total_anggaran")
data = get_as_dataframe(sheet)
print(data.head())