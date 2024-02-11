# Importa a biblioteca requests, que é usada para fazer requisições HTTP
import requests
# Importa a classe BeautifulSoup do módulo bs4, que é usada para fazer a análise de HTML
from bs4 import BeautifulSoup

# Função para pesquisar no Google
def pesquisar_google(query):
    # Define a URL da pesquisa do Google com base na consulta passada como argumento
    url = f"https://www.google.com/search?q={query}"
    # Define os cabeçalhos HTTP para simular um navegador
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    # Faz uma requisição GET para a URL usando os cabeçalhos definidos
    response = requests.get(url, headers=headers)
    # Cria um objeto BeautifulSoup para analisar o conteúdo HTML da resposta
    soup = BeautifulSoup(response.text, "html.parser")
    # Encontra todos os elementos HTML com a classe "BNeawe", que contêm os resultados da pesquisa
    search_results = soup.find_all("div", class_="BNeawe")

    # Verifica se foram encontrados resultados na pesquisa
    if search_results:
        # Retorna o texto do primeiro resultado encontrado
        return search_results[0].get_text()
    else:
        # Retorna uma mensagem de erro caso nenhum resultado seja encontrado
        return "Desculpe, não encontrei resultados para sua pergunta."

# Função principal do programa
def main():
    # Imprime uma mensagem de boas-vindas
    print("Olá! Eu sou sua assistente virtual. Como posso ajudar?")
    # Loop principal para interação com o usuário
    while True:
        # Solicita uma pergunta ao usuário
        pergunta = input("Você: ")
        # Verifica se o usuário deseja sair do programa
        if pergunta.lower() in ["sair", "parar", "adeus"]:
            # Imprime uma mensagem de despedida e encerra o programa
            print("Até logo!")
            break
        # Chama a função pesquisar_google para obter uma resposta à pergunta do usuário
        resposta = pesquisar_google(pergunta)
        # Imprime a resposta da assistente virtual
        print("Assistente:", resposta)

# Verifica se o script está sendo executado como programa principal
if __name__ == "__main__":
    # Chama a função principal para iniciar a execução do programa
    main()
