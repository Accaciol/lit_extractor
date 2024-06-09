import re
import csv

def extrair_informacoes(txt_path, csv_path):
    with open(txt_path, 'r', encoding='latin-1') as file:
        conteudo = file.read()

    # Padrão para encontrar a seção de litologia
    padrao_secao = re.compile(
        r'LITOLOGIA -\s*'
        r'TOPO\s+BASE\s+ROCHA\s+COR\s+TONALIDADE\s+GRANULOMETRIA\s+ARREDONDAMENTO\s*'
        r'((?:\s{2,}.*\n?)+)', 
        re.IGNORECASE
    )

    # Encontra a seção de litologia no conteúdo
    secao_litologia = padrao_secao.search(conteudo)

    if not secao_litologia:
        print("Nenhuma informação encontrada.")
        return

    # Extrai a tabela de litologia
    tabela_litologia = secao_litologia.group(1).strip()

    # Processar as linhas da tabela de litologia
    linhas = tabela_litologia.split('\n')
    dados = []

    # Processar as linhas da tabela de litologia
    for linha in linhas:
        # Remove espaços em branco no início e no fim da linha
        linha = linha.strip()
        if not linha:
            continue
        
        # Divide a linha em partes, considerando múltiplos espaços como separadores
        partes = re.split(r'\s{2,}', linha)
        
        # Preenche os valores faltantes com vazio ("")
        while len(partes) < 7:
            partes.append("")

        # Substitui explicitamente valores ausentes por strings vazias
        partes = ["" if parte.strip() == "-" else parte for parte in partes]

        topo, base, rocha, cor, tonalidade, granulometria, arredondamento = partes[:7]
        dados.append([topo, base, rocha, cor, tonalidade, granulometria, arredondamento])


    # Salvar os dados em um arquivo CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        # Escreve o cabeçalho do CSV
        escritor.writerow(['TOPO', 'BASE', 'ROCHA', 'COR', 'TONALIDADE', 'GRANULOMETRIA', 'ARREDONDAMENTO'])
        # Escreve os dados
        escritor.writerows(dados)

# Caminho para o arquivo TXT e CSV
txt_path = 'C:/Users/lucas/Documents/litologia_Extractor/1RJS0106RJ_agp.txt'
csv_path = 'C:/Users/lucas/Documents/litologia_Extractor/litologia.csv'

# Chamar a função para extrair as informações e salvar no CSV
extrair_informacoes(txt_path, csv_path)
