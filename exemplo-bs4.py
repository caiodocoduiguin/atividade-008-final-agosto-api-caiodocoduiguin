import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://brasilescola.uol.com.br/doencas/coronavirus-covid-19.htm")
soup = bs(page.content, 'html.parser')

texto_enviar_sms = {
}

titulos_possiveis: list = soup.find_all("h1", class_="titulo-definicao")
for titulo in titulos_possiveis[0:1]:
    texto_enviar_sms['titulo'] = titulo.text

paragrafos_com_textos: list = soup.find_all("p")
for paragrafo in paragrafos_com_textos[0:1]:
    texto_enviar_sms['conteudo'] = paragrafo.text.split('\n\r\n')[0]

print(texto_enviar_sms)