import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("SMTP_USER")
DESTINATARIO = "kevinpedrosodev@gmail.com"

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SERVER = "smtp.mailersend.net"
SMTP_PORT = 587

def capturar_noticias_infomoney():
    url = "https://www.infomoney.com.br/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar o InfoMoney")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    noticias = soup.find_all("a", class_="hover:underline", limit=5)

    resultado = []
    for noticia in noticias:
        titulo = noticia.get_text(strip=True)
        link = noticia.get("href")
        if not link.startswith("https://"):
            link = "https://www.infomoney.com.br" + link  
        resultado.append(f"<b>{titulo}</b><br><a href='{link}'>{link}</a><br><br>")

    return "".join(resultado)

def enviar_email(mensagem):
    if not SMTP_USER or not SMTP_PASSWORD:
        print("Erro: Credenciais SMTP não configuradas.")
        return

    msg = MIMEMultipart()
    msg["Subject"] = "Últimas Notícias do InfoMoney"
    msg["From"] = EMAIL
    msg["To"] = DESTINATARIO

    html_content = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                }}
                h2 {{
                    color: #333;
                    font-size: 24px;
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .noticias {{
                    margin-bottom: 20px;
                }}
                .noticia {{
                    background-color: #f9f9f9;
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 5px;
                    border-left: 4px solid #4CAF50;
                }}
                .noticia a {{
                    color: #1a73e8;
                    text-decoration: none;
                    font-size: 16px;
                }}
                .noticia a:hover {{
                    text-decoration: underline;
                }}
                footer {{
                    text-align: center;
                    margin-top: 20px;
                    font-size: 14px;
                    color: #888;
                }}
                footer img {{
                    width: 150px;
                    margin-top: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Últimas Notícias</h2>
                <div class="noticias">
                    {mensagem}
                </div>
                <footer>
                    <p>Obrigado por acompanhar o InfoMoney!</p>
                </footer>
            </div>
        </body>
    </html>
    """

    msg.attach(MIMEText(html_content, "html", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL, DESTINATARIO, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

noticias = capturar_noticias_infomoney()
if noticias:
    enviar_email(noticias)
