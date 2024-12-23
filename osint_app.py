import requests
import googlesearch
import socket
import whois
import time
from bs4 import BeautifulSoup
import re
import dns.resolver
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import stem
from stem import Signal
from stem.control import Controller
import random
import time
from googlesearch import search
import os

# Fonction pour initialiser Tor via Selenium (pour dark web)
def init_tor():
    print("[Tor] Initialisation de Tor...")
    
    
    # Démarrer le navigateur avec Selenium et Tor
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Fonction pour envoyer un signal à Tor pour renouveler l'IP
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_tor_password')  # Assurez-vous de configurer un mot de passe Tor
        controller.signal(Signal.NEWNYM)

# Fonction de recherche Google
def google_search(query):
    print("[Google Search] Résultats :")
    try:
        search_results = googlesearch.search(query, num_results=5)
        for url in search_results:
            print(url)
    except Exception as e:
        print(f"Erreur lors de la recherche Google : {e}")

# Fonction de recherche d'articles de presse via Google News
def news_search(query):
    print("[Google News] Recherche d'articles :")
    try:
        # Recherche d'articles sur Google News
        search_results = googlesearch.search(f"site:news.google.com {query}", num_results=5)
        for url in search_results:
            if "news.google.com" in url:
                print(f"Article trouvé : {url}")
    except Exception as e:
        print(f"Erreur lors de la recherche d'articles de presse : {e}")

# Fonction de recherche d'articles sur Le Monde
def le_monde_search(query):
    print("[Le Monde] Recherche d'articles :")
    try:
        # Recherche d'articles sur Le Monde
        search_results = googlesearch.search(f"site:lemonde.fr {query}", num_results=5)
        for url in search_results:
            if "lemonde.fr" in url:
                print(f"Article trouvé sur Le Monde : {url}")
    except Exception as e:
        print(f"Erreur lors de la recherche d'articles sur Le Monde : {e}")

# Fonction de recherche d'articles sur Le Canard Enchaîné
def le_canard_enchaine_search(query):
    print("[Le Canard Enchaîné] Recherche d'articles :")
    try:
        # Recherche d'articles sur Le Canard Enchaîné
        search_results = googlesearch.search(f"site:lecanardenchaine.fr {query}", num_results=5)
        for url in search_results:
            if "lecanardenchaine.fr" in url:
                print(f"Article trouvé sur Le Canard Enchaîné : {url}")
    except Exception as e:
        print(f"Erreur lors de la recherche d'articles sur Le Canard Enchaîné : {e}")

# Fonction de recherche d'articles sur Le Point
def le_point_search(query):
    print("[Le Point] Recherche d'articles :")
    try:
        # Recherche d'articles sur Le Point
        search_results = googlesearch.search(f"site:lepoint.fr {query}", num_results=5)
        for url in search_results:
            if "lepoint.fr" in url:
                print(f"Article trouvé sur Le Point : {url}")
    except Exception as e:
        print(f"Erreur lors de la recherche d'articles sur Le Point : {e}")

# Fonction de recherche d'articles sur Frontières Media
def frontieres_media_search(query):
    print("[Frontières Media] Recherche d'articles :")
    try:
        # Recherche d'articles sur Frontières Media
        search_results = googlesearch.search(f"site:frontieresmedia.fr {query}", num_results=5)
        for url in search_results:
            if "frontieresmedia.fr" in url:
                print(f"Article trouvé sur Frontières Media : {url}")
    except Exception as e:
        print(f"Erreur lors de la recherche d'articles sur Frontières Media : {e}")

# Fonction de recherche d'articles sur WikiLeaks
def wikileaks_search(query):
    print("[WikiLeaks] Recherche d'articles :")
    try:
        # Recherche d'articles sur WikiLeaks
        search_results = googlesearch.search(f"site:wikileaks.org {query}", num_results=5)
        for url in search_results:
            if "wikileaks.org" in url:
                print(f"Article trouvé sur WikiLeaks : {url}")
    except Exception as e:
        print(f"Erreur lors de la recherche d'articles sur WikiLeaks : {e}")

# Fonction de recherche d'articles sur Pappers.fr
def pappers_search(query):
    print("[Pappers.fr] Recherche d'articles :")
    try:
        # Recherche d'articles sur Pappers.fr
        search_results = googlesearch.search(f"site:pappers.fr {query}", num_results=5)
        for url in search_results:
            if "pappers.fr" in url:
                print(f"Article trouvé sur Pappers.fr : {url}")
    except Exception as e:
        print(f"Erreur lors de la recherche d'articles sur Pappers.fr : {e}")


# Fonction de recherche sur Facebook via Google
def facebook_search(query):
    print("[Facebook] Profils trouvés :")
    try:
        search_results = googlesearch.search(f"site:facebook.com {query}", num_results=3)
        for url in search_results:
            if "facebook.com" in url:
                print(url)
    except Exception as e:
        print(f"Erreur lors de la recherche Facebook : {e}")

# Fonction de recherche sur Twitter via Google
def twitter_search(query):
    print("[Twitter] Profils trouvés :")
    try:
        search_results = googlesearch.search(f"site:x.com {query}", num_results=3)
        for url in search_results:
            if "x.com" in url:
                print(url)
    except Exception as e:
        print(f"Erreur lors de la recherche Twitter : {e}")

# Fonction de recherche sur LinkedIn via Google
def linkedin_search(query):
    print("[LinkedIn] Profils trouvés :")
    try:
        search_results = googlesearch.search(f"site:linkedin.com {query}", num_results=3)
        for url in search_results:
            if "linkedin.com" in url:
                print(url)
    except Exception as e:
        print(f"Erreur lors de la recherche LinkedIn : {e}")

# Fonction de recherche sur Instagram via Google
def instagram_search(query):
    print("[Instagram] Profils trouvés :")
    try:
        search_results = googlesearch.search(f"site:instagram.com {query}", num_results=3)
        for url in search_results:
            if "instagram.com" in url:
                print(url)
    except Exception as e:
        print(f"Erreur lors de la recherche Instagram : {e}")

# Fonction de recherche sur GitHub via Google
def github_search(query):
    print("[GitHub] Profils trouvés :")
    try:
        search_results = googlesearch.search(f"site:github.com {query}", num_results=3)
        for url in search_results:
            if "github.com" in url:
                print(url)
    except Exception as e:
        print(f"Erreur lors de la recherche GitHub : {e}")

# Fonction WHOIS pour récupérer les informations de domaine
def whois_lookup(domain):
    print("[WHOIS] Informations :")
    try:
        domain_info = whois.whois(domain)
        print(domain_info)
    except Exception as e:
        print(f"Erreur lors de la recherche WHOIS : {e}")

# Fonction de recherche sur Reddit via Google
def reddit_search(query):
    print("[Reddit] Discussions trouvées :")
    try:
        search_results = googlesearch.search(f"site:reddit.com {query}", num_results=3)
        for url in search_results:
            if "reddit.com" in url:
                print(url)
    except Exception as e:
        print(f"Erreur lors de la recherche Reddit : {e}")


# Recherche Wayback Machine
def wayback_search(query):
    print("[Wayback Machine] Recherche d'archives pour :", query)
    wayback_url = f"http://web.archive.org/cdx/search/cdx?url={query}&output=json&filter=statuscode:200"
    try:
        response = requests.get(wayback_url, timeout=30)
        if response.status_code == 200:
            archives = response.json()[1:]  # Exclure l'en-tête
            print(f"{len(archives)} archives trouvées.")
            for archive in archives[:5]:  # Limiter les résultats affichés
                timestamp, original_url = archive[1], archive[2]
                archive_link = f"http://web.archive.org/web/{timestamp}/{original_url}"
                print(f"Archive trouvée : {archive_link}")
        else:
            print("[Wayback Machine] Aucun résultat trouvé.")
    except Exception as e:
        print(f"Erreur lors de la recherche dans Wayback Machine : {e}")

# Recherche sur le Deep Web
def deep_web_search(query):
    print("[Deep Web] Recherche dans des bases de données spécialisées...")
    deep_web_sources = [
        {"name": "Pipl", "url": f"https://pipl.com/search/?q={query}"},
        {"name": "WebMii", "url": f"https://webmii.com/people?n={query.replace(' ', '+')}"},
        {"name": "Spokeo", "url": f"https://www.spokeo.com/search?q={query}"},
        {"name": "PeekYou", "url": f"https://www.peekyou.com/{query.replace(' ', '_')}"},
    ]
    for source in deep_web_sources:
        print(f"Recherche sur {source['name']} : {source['url']}")


# Fonction pour extraire les emails d'une page et vérifier leur validité
def find_emails(soup):
    emails = []
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    text_content = soup.get_text()
    emails = re.findall(email_pattern, text_content)
    
    valid_emails = []
    for email in emails:
        domain = email.split('@')[1]
        try:
            # Vérification si le domaine du mail existe
            dns.resolver.resolve(domain, 'MX')  # MX signifie Mail Exchanger
            valid_emails.append(email)
        except dns.resolver.NoAnswer:
            continue  # Si le domaine n'existe pas, on passe à l'email suivant

    return list(set(valid_emails))  # Supprimer les doublons

# Fonction pour extraire des numéros de téléphone d'une page
def find_phone_numbers(soup):
    phone_numbers = []
    phone_pattern = r"\+?[0-9]{1,4}?[-.\s]?[0-9]{1,3}[-.\s]?[0-9]{3,4}[-.\s]?[0-9]{3,4}"
    text_content = soup.get_text()
    phone_numbers = re.findall(phone_pattern, text_content)
    return list(set(phone_numbers))  # Supprimer les doublons

# Fonction de scraping des résultats
def scrape_results(url):
    print(f"[Scraping] Scraping de l'URL : {url}")
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Exemple pour récupérer les images
        images = soup.find_all('img')
        for img in images:
            print(f"Image trouvée : {img.get('src')}")
        
        # Exemple pour récupérer les articles
        articles = soup.find_all('a', href=True)
        for article in articles:
            print(f"Article trouvé : {article['href']}")
        
        # Recherche des e-mails dans le contenu de la page
        emails = find_emails(soup)
        for email in emails:
            print(f"Adresse email trouvée : {email}")
        
        # Recherche des numéros de téléphone
        phone_numbers = find_phone_numbers(soup)
        for phone in phone_numbers:
            print(f"Numéro de téléphone trouvé : {phone}")
        
    except Exception as e:
        print(f"Erreur lors du scraping de {url} : {e}")

# Fonction de recherche sur le dark web (via Tor)
def dark_web_search(query, driver):
    print("[Dark Web] Recherche dans le dark web...")
    query = f"site:*.onion {query}"
    try:
        driver.get(f"https://duckduckgo.com/?q={query}")  # Recherche via DuckDuckGo sur le dark web
        time.sleep(5)  # Attendre que la page se charge
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        
        links = soup.find_all('a', href=True)
        for link in links:
            # Filtrer uniquement les liens .onion
            if '.onion' in link['href']:
                print(f"Lien trouvé sur le dark web : {link['href']}")
    
    except Exception as e:
        print(f"Erreur lors de la recherche sur le dark web : {e}")

def find_documents(first_name, last_name, nickname=None):
    # Crée la requête de recherche de base avec le prénom et le nom
    query = f"{first_name} {last_name}"
    
    # Ajoute le pseudo à la recherche si fourni
    if nickname:
        query += f" {nickname}"
    
    print(f"[Document Search] Recherche de documents pour : {query}")
    
    # Recherche Google pour des documents en PDF
    google_query = f"{query} filetype:pdf"
    google_search(google_query)  # Cette fonction doit effectuer une recherche Google pour des fichiers PDF
    
    # Recherche de fichiers DOCX (documents Word)
    docx_query = f"{query} filetype:docx"
    google_search(docx_query)
    
    # Recherche de fichiers PPTX (présentations PowerPoint)
    pptx_query = f"{query} filetype:pptx"
    google_search(pptx_query)

    # Recherche sur Google Drive (via des requêtes publiques)
    drive_query = f"{query} site:drive.google.com"
    google_search(drive_query)

    # Recherche sur Dropbox
    dropbox_query = f"{query} site:dropbox.com"
    google_search(dropbox_query)

    # Recherche sur Scribd (partage de documents)
    scribd_query = f"{query} site:scribd.com"
    google_search(scribd_query)

    # Recherche sur ResearchGate (publications académiques)
    researchgate_query = f"{query} site:researchgate.net"
    google_search(researchgate_query)
    
    # Recherche dans les résultats de Wayback Machine pour des documents archivés
    wayback_search(query)
    
    # Scraping des pages de résultats pour rechercher des PDF et autres documents
    url = input("Entrez une URL pour le scraping des documents (ou appuyez sur Entrée pour ignorer) : ")
    if url:
        scrape_documents(url)

def google_search(query):
    # Effectue une recherche Google avec l'opérateur de type de fichier
    print(f"Recherche Google pour : {query}")
    # Simuler une recherche Google (cela pourrait être automatisé avec un outil comme Selenium ou Scrapy)
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.text, "html.parser")
    
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if "pdf" in href or "docx" in href or "pptx" in href:
            print(f"Document trouvé : {href}")
    
    # Retourner la liste des liens
    return links

def scrape_documents(url):
    # Scrape une page URL pour trouver des documents PDF, DOCX, PPTX
    print(f"Scraping de l'URL pour des documents : {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Cherche tous les liens vers des documents
    links = soup.find_all("a", href=True)
    for link in links:
        file_url = link["href"]
        if file_url.endswith(".pdf") or file_url.endswith(".docx") or file_url.endswith(".pptx"):
            print(f"Document trouvé : {file_url}")

# Fonction principale pour rechercher les informations OSINT
def osint_search(first_name, last_name, nickname=None):
    query = f"{first_name} {last_name} {nickname}"

    # Si un pseudo est fourni, l'ajouter à la requête
    if nickname:
        query += f" {nickname}"
    
    # Recherche Google
    google_search(query)

    # Recherche d'articles de presse
    news_search(query)

    # Recherche sur Le Monde
    le_monde_search(query)

    # Recherche sur Le Canard Enchaîné
    le_canard_enchaine_search(query)

    # Recherche sur Le Point
    le_point_search(query)

    # Recherche sur Frontières Media
    frontieres_media_search(query)

    # Recherche sur WikiLeaks
    wikileaks_search(query)

    # Recherche sur Pappers.fr
    pappers_search(query)
    
    # Recherche sur Facebook
    facebook_search(query)
    
    # Recherche sur x
    twitter_search(query)
    
    # Recherche sur LinkedIn
    linkedin_search(query)
    
    # Recherche sur Instagram
    instagram_search(query)
    
    # Recherche sur GitHub
    github_search(query)
    
    # Recherche WHOIS si l'utilisateur entre un domaine
    domain = input("Entrez un domaine pour effectuer une recherche WHOIS (ou appuyez sur Entrée pour ignorer) : ")
    if domain:
        whois_lookup(domain)
    
    # Scraping des pages de résultats (articles, images)
    url = input("Entrez une URL pour le scraping (ou appuyez sur Entrée pour ignorer) : ")
    if url:
        scrape_results(url)
    
    # Recherche sur Reddit
    reddit_search(query)

    # Recherche Wayback Machine
    wayback_search(query)

    # Recherche sur le Deep Web
    deep_web_search(query)

    # Recherche sur le dark web
    use_tor = input("Souhaitez-vous effectuer une recherche sur le dark web via Tor (oui/non) ? : ").lower()
    if use_tor == 'oui':
        driver = init_tor()
        dark_web_search(query, driver)
        driver.quit()
    
    # Recherche de documents (pdf, docx etc...
    find_documents(first_name, last_name, nickname)


if __name__ == "__main__":
    first_name = input("Entrez le prénom : ")
    last_name = input("Entrez le nom : ")
    nickname = input("Entrer le pseudo : ")

    
    osint_search(first_name, last_name)

    
