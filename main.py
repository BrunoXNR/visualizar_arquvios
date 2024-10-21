import os
import time

def abrir_arquivos_pdf(pasta):
    # Verifica se a pasta existe
    if not os.path.exists(pasta):
        print(f"A pasta {pasta} não foi encontrada.")
        return

    # Percorre todos os arquivos da pasta
    for arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, arquivo)
        
        # Verifica se é um arquivo PDF
        if os.path.isfile(caminho_completo) and arquivo.lower().endswith('.pdf'):
            print(f"Abrindo o arquivo PDF: {arquivo}")
            
            # Abre o arquivo PDF com o programa padrão do sistema
            os.startfile(caminho_completo)  

            # Espera por 5 segundos antes de fechar ou passar ao próximo arquivo
            time.sleep(5)
            print(f"Arquivo {arquivo} foi aberto por 5 segundos.\n")

# Exemplo de uso
caminho_da_pasta = "Insira o caminho da pasta" 
abrir_arquivos_pdf(caminho_da_pasta)
