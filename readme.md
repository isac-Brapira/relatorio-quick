# Quick Gestão

Este projeto é uma ferramenta para baixar relatórios de chamados de diferentes categorias (TI, Serviços Gerais, Compras) a partir de uma API e salvar os dados em um arquivo JSON. As datas nos dados são formatadas para o padrão brasileiro (dd/mm/aaaa).

## Funcionalidades

- Baixa relatórios de diferentes categorias de chamados.
- Formata as datas para o padrão brasileiro (dd/mm/aaaa).
- Salva todos os dados em um único arquivo JSON.

## Pré-requisitos

- Python 3.x
- Bibliotecas: `requests`, `json`, `os`, `datetime`

## Instalação

1. Clone o repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd <NOME_DO_DIRETORIO>
    ```
3. Instale as dependências:
    ```sh
    pip install requests
    ```

## Como usar

1. Configure o token de autenticação e o resaleId no código.
2. Defina as datas de início e fim (`startDate` e `endDate`).
3. Execute o script para baixar os relatórios e salvar os dados em um arquivo JSON.

## Exemplo de uso

```python
token = 'seu_token_aqui'
resaleId = 1
startDate = '2025-01-01'
endDate = date.today()

baixar_relatorios(token, startDate, endDate, resaleId)
