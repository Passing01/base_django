article = Article(titre="Mon premier article", contenu="Le contenu de mon article", date_publication=timezon.now())
article.save()


# Pour afficher tout le contenue en ciblant le modele Article
article = Article.objects.all()

# Pour filtrer l'affichage des articles
article = Article.objects.filter(date_publication_year=2024)