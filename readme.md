# Web Scraping InfoMoney

Este é um projeto simples de **Web Scraping** que captura as últimas notícias do portal InfoMoney e as envia por e-mail para o destinatário configurado. O projeto utiliza **Python** com as bibliotecas `requests`, `BeautifulSoup`, `smtplib`, entre outras.

## Funcionalidades

- Captura as últimas notícias do portal InfoMoney.
- Envia um e-mail com as notícias formatadas em HTML.
- Usa o serviço de SMTP para o envio de e-mails (configurado com Mailersend).
- O envio de e-mails é feito de maneira assíncrona, utilizando a autenticação segura.

## Pré-requisitos

Antes de rodar o projeto, você precisa configurar as variáveis de ambiente para garantir que tudo funcione corretamente.

### Instalação das dependências

1. Clone o repositório:
   ```bash
   git clone https://github.com/alveskevinn/scraping-info-money.git
   cd scraping-info-money
2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use venv\Scripts\activate
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
4. Crie um arquivo .env na raiz do projeto e configure suas variáveis de ambiente:
    ```bash
    SMTP_USER=seu_email@dominio.com
    SMTP_PASSWORD=sua_senha

### Estrutura do Projeto
    scraping-info-money/
    │
    ├── main.py            # Código principal do scraping e envio de e-mail
    ├── requirements.txt   # Dependências do projeto
    ├── .env               # Variáveis de ambiente (não commitadas)
    ├── .gitignore         # Ignora arquivos desnecessários para o Git
    └── README.md 

### Como usar

- Certifique-se de ter configurado corretamente as variáveis de ambiente com seu e-mail SMTP.
- Execute o script Python:
    ```bash
    python main.py

O script irá:

Acessar o portal InfoMoney.
Capturar as últimas notícias.
Enviar as notícias por e-mail no formato HTML.

### Contribuições
Sinta-se à vontade para contribuir com melhorias ou correções para o projeto. Se você encontrar algum bug ou tiver sugestões, crie uma issue ou envie um pull request.
