from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def scrape(request):
    page = requests.get('https://www.google.com')
    soup = BeautifulSoup(page.text, 'html.parser')

    link_adress = []

    for link in soup.find_all('a'):
        link_adress.append(link.get('href'))

    return render(request, 'myapp/result.html', {'link_address': link_adress})