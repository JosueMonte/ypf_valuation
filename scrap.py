import requests

url = 'https://inversores.ypf.com/r/documents.html?p=Informacion-financiera/YPF%20-%202024%20-%20FY24%20%26%204Q%20-%20ESP.xlsx'
response = requests.get(url)

with open('Tablas_Financieras_2024_4T24.xlsx', 'wb') as f:
    f.write(response.content)
