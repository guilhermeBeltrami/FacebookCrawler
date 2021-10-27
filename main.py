import sys
import requests
import re

from bs4 import BeautifulSoup


def request(url):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    try:
        r = requests.get(url, headers=header)
        return r.text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass


def banner():
	print("Bem Vindo!")
	print("     ___      _  __  __ ")
	print("    |   \ ___| |_\ \/ / ")
	print("    | |) / _ \  _|>  < ")
	print("  __|___/\___/\__/_/\_\ ")
	print(" / __| ___ _ ___ _(_)__ ___ ___ ")
	print(" \__ \/ -_) '_\ V / / _/ -_|_-< ")
	print(" |___/\___|_|  \_/|_\__\___/__/ ")
	print("\n")


if __name__ == "__main__":
	banner()
	nome = str(input("Digite o nome: ")).replace(" ", "-")
	url = "https://pt-br.facebook.com/public/"
	url += nome
	html = request(url)
	soup = BeautifulSoup(html, "html.parser")
	soup.prettify()
	tags = soup.find_all("code")
	total = 0
	for tag in tags:
		urls = []
		text = str(tag)
		linhas = re.findall("href=[\"\'](.*?)[\"\']", text)
		for linha in linhas:
			if "https://pt-br.facebook.com/" in linha:
				if "/photos" not in linha:
					if linha not in urls:
						urls.append(linha)
	for url in urls:
		total += 1
	print("\nO total de usuarios encontrados foi: {}\n".format(total))
	print("Lista com os perfis dos usuarios encontrados: ")
	for url in urls:
		print(url)
