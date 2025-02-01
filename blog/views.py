from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.views.generic import ListView

# Create your views here.
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # ajouter une notification
            messages.success(request, "votre article est bien enregistrer")
            return redirect('page_acceuil')
        else:
            messages.error(request, "Erreur lors de la création de l'article")
            form = ArticleForm()
            return render(request, 'blog/creer_article.html', {'form': form})
    else:
        # Si la méthode est GET, afficher un formulaire vide
        form = ArticleForm()
        return render(request, 'blog/creer_article.html', {'form': form})
    
def page_acceuil(request):
    articles = Article.objects.all()
    return render(request, 'blog/page_acceuil.html', {'articles': articles})

class ListeArticleView(ListView):
    model = Article
    template_name = 'bog/liste_article.html'
    context_object_name = 'article'

def afficher_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/afficher_article', {'article': article})