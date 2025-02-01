from django import forms 
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model =Article
        fields = ['titre', 'contenue', 'date_publication', 'image']

    def clear_titre(self):
        titre = self.cleaned_data.get('titre')
        if "interdit" in titre:
            raise forms.ValidationError("Ce titre contient un mot interdit")