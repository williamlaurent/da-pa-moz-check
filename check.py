# DA PA Checker
# Silahkan recoded tetapi berikan sumber dari github ini
# github.com/williamlaurent

import requests

def get_da_pa(domain):
    url = f"https://api.moz.com/stats/url-metrics/{domain}?Cols=103079217524"

    # Masukkan AccessID & SecretKey - Beli sendiri membershipnya moz.com Ya
    payload = {
        "AccessID": "YOUR_ACCESS_ID",
        "SecretKey": "YOUR_SECRET_KEY"
    }

    response = requests.get(url, params=payload)
    data = response.json()

    if 'pda' in data:
        pa = data['upa']
        da = data['pda']
        print(f"Domain Authority (DA) of {domain}: {da}")
        print(f"Page Authority (PA) of {domain}: {pa}")
    else:
        print(f"Failed to retrieve DA and PA data for {domain}")

# Mendapatkan daftar domain dari file txt
with open("domains.txt", "r") as file:
    domains = file.read().splitlines()

# Pengecekan DA dan PA untuk setiap domain
for domain in domains:
    get_da_pa(domain)
