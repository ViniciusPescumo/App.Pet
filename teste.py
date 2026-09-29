import requests

base = "http://127.0.0.1:8000"

proxies = {"http": None, "https": None}

pet1 = {
    "nome_pet": "Marvel",
    "especie": "Felino",
    "raca": "Laranja",
    "bloco": "8",
    "apartamento": "2",
    "nome_tutor": "Isabela",
    "telefone_tutor": "11912345678"
}

pet2 = {
    "nome_pet": "Leslie",
    "especie": "Cachorro",
    "raca": "Pastor Alemão",
    "bloco": "8",
    "apartamento": "517",
    "nome_tutor": "Vinicius",
    "telefone_tutor": "15912345678"
}

r1 = requests.post(f"{base}/pets", json=pet1, proxies=proxies)
print("Status:", r1.status_code)
print("Resposta:", r1.text)

r2 = requests.post(f"{base}/pets", json=pet2, proxies=proxies)
print("Status:", r2.status_code)
print("Resposta:", r2.text)

r3 = requests.get(f"{base}/apartamento/517", proxies=proxies)
print("Status:", r2.status_code)
print("Resposta:", r2.text)