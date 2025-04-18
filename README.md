# 📊 Análise de Consumo Residencial de Energia Elétrica por Estado

Este projeto realiza uma análise estatística simples do **consumo mensal de energia elétrica residencial no Brasil**, utilizando dados públicos fornecidos pela **Empresa de Pesquisa Energética (EPE)**. Os dados analisados cobrem os anos de 2004 a 2025* e estão organizados por estado e mês.

## 🧠 Sobre o projeto

A aplicação lê uma planilha em formato CSV com os dados históricos de consumo residencial por UF, realiza o pré-processamento necessário e gera um relatório contendo:
- Média de consumo por estado
- Soma total de consumo por estado
- Desvio padrão do consumo por estado

Os resultados são exportados em formato **JSON**, podendo ser facilmente utilizados em uma aplicação front-end para visualização interativa.

## 🗂 Fonte dos dados

Os dados utilizados neste projeto foram extraídos da publicação oficial disponível no portal de dados abertos da EPE:

🔗 [Consumo de Energia Elétrica - EPE.gov.br](https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/consumo-de-energia-eletrica)

## 🏢 O que é a EPE?

A **Empresa de Pesquisa Energética (EPE)** é uma empresa pública vinculada ao Ministério de Minas e Energia. Ela é responsável por desenvolver estudos e fornecer informações técnicas que subsidiam o planejamento energético do Brasil nas áreas de:
- Energia elétrica
- Petróleo e gás natural
- Fontes renováveis

A EPE atua de forma estratégica na formulação de políticas energéticas sustentáveis e na promoção do uso racional e eficiente da energia.

## ⚙️ Tecnologias utilizadas

- Python 3
- Pandas
- JSON

## 📂 Estrutura do projeto

```
📁 dados
    └── CONSUMO MENSAL DE ENERGIA ELÉTRICA POR CLASSE.xlsx - CONSUMO RESIDENCIAL POR UF.csv
📄 analise_energia.py
📄 estatisticas_consumo.json
📄 README.md
```

## ▶️ Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repo.git
   ```

2. Instale as dependências:
   ```bash
   pip install pandas
   ```

3. Execute o script:
   ```bash
   python analise_energia.py
   ```

4. O arquivo `estatisticas_consumo.json` será gerado com as estatísticas por estado.

