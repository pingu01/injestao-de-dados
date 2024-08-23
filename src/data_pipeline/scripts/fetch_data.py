import requests
import random
import datetime

def fetch_and_send_data(api_url, headers, target_url):
    # Faz a requisição para a API original
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        distilleries = response.json()
        total_distilleries = len(distilleries)
        
        # Seleciona um número aleatório dentro do total de destilarias
        random_index = random.randint(0, total_distilleries - 1)

        data = {
            "date": int(datetime.datetime.now().timestamp()),  # Corrigido para chamar timestamp()
            "dados": distilleries[random_index]  # Envia o objeto JSON diretamente
        }
        print(data)
        
        # Envia os dados para a nova API na rota /data
        send_response = requests.post(target_url, json=data)
        
        if send_response.status_code == 200:
            print("Dados enviados com sucesso para a API /data")
        else:
            print(f"Erro ao enviar dados: {send_response.status_code} - {send_response.text}")
    else:
        print(f"Erro ao buscar dados: {response.status_code} - {response.text}")

# Configurações da API
api_url = 'https://whiskyhunter.net/api/distilleries_info/'
headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': 'eMayJjYzv8qvC9S7bNuWXIky7QsQsvuM4PQhxHO9PtdkERCK1SkIxbldfwICdpda'
}

# URL da API onde os dados serão enviados
target_url = 'http://localhost:5000/data'

# Chama a função
fetch_and_send_data(api_url, headers, target_url)
