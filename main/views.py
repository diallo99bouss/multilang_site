# views.py
from django.shortcuts import render
from datetime import datetime  # Importez si vous utilisez la date de publication simulée

# Exemple de données simulées pour les articles
simulated_articles = [
    {'title': 'Premier article', 'content': 'Contenu du premier article', 'pub_date': datetime.now()},
    {'title': 'Deuxième article', 'content': 'Contenu du deuxième article', 'pub_date': datetime.now()},
    {'title': 'Troisième article', 'content': 'Contenu du troisième article', 'pub_date': datetime.now()},
]

def article_list(request):
    articles = simulated_articles  # Utilisez la liste simulée d'articles
    return render(request, 'main/article_list.html', {'articles': articles})
