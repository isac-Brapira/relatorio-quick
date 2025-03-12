import requests
import json
import os
from datetime import date, datetime

# Formatando a data para o padrão brasileiro ex: 01/01/2021
def formatar_data(data_iso):
    data = datetime.fromisoformat(data_iso.rstrip("Z"))
    return data.strftime("%d/%m/%Y")

# Função para baixar os relatórios
def baixar_relatorios(token, start_date, end_date):
    url = "https://api-quick.quickaplica.com.br/api/v1/purchases/solicitations/export-purchases"
    headers = {"Authorization": f"Bearer {token}"}
    
    todos_os_dados = {
        "solicitacoes": [],
        "itens": []
    }
    
    params = {
        "startDate": start_date,
        "endDate": end_date
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Lança exceção para status de erro (4xx, 5xx)

        dados = response.json()["data"]

        for solicitacao in dados["solicitacoes"]:
            for chave, valor in solicitacao.items():
                if isinstance(valor, str) and (chave.startswith('dt_') or chave == 'data'):
                    try:
                        solicitacao[chave] = formatar_data(valor)
                    except ValueError:
                        pass # Ignora formatação se não for uma data válida
            todos_os_dados["solicitacoes"].append(solicitacao)

        for item in dados["itens"]:
            for chave, valor in item.items():
                if isinstance(valor, str) and (chave.startswith('dt_') or chave == 'data'):
                    try:
                        item[chave] = formatar_data(valor)
                    except ValueError:
                        pass # Ignora formatação se não for uma data válida
            todos_os_dados["itens"].append(item)

    # Trata exceções
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar relatório: {e}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar resposta JSON: {e}, resposta: {response.text}")

    caminho_pasta = r"I:\Administrativo\TecInfo\DATABASE\QuickGestao\Relatórios Quick - Compras"
    # Salva todos os dados em um único arquivo JSON
    nome_arquivo = f"Relatório Completo - {datetime.now().strftime('%Y')}.json"
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo) 
    
    with open(caminho_completo, "w", encoding="utf-8") as arquivo_json:
        json.dump(todos_os_dados, arquivo_json, ensure_ascii=False, indent=4)
    print(f"Relatório completo salvo em {caminho_completo}!")
            
# Configurações

# Lendo token do arquivo
with open(r"I:\Administrativo\TecInfo\DESENVOLVIMENTOS\QUICK GESTÃO\token.txt", "r") as arquivo_token:
    token = arquivo_token.read().strip() # Remove espaços em branco e quebras de linha
    

# Pega a data atual e formata para o primeiro dia do mês
x = datetime.now()
monthNow = x.month

# Adiciona um zero à esquerda se o mês tiver apenas um dígito
if len(str(monthNow)) == 1:
    monthNow = f'0{x.month}'

# startDate = str(f'{x.year}-{monthNow}-01')

startDate = f'{x.year}-01-01'
endDate = date.today()

# Chama a função para baixar os relatórios
baixar_relatorios(str(token), startDate, endDate)


