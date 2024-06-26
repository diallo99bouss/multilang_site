from django.shortcuts import render
from django.utils.translation import gettext as _

def article_list(request):
    context = {
        'articles': [
            {'title': _('Article 1'), 'content': _('Content of article 1')},
            {'title': _('Article 2'), 'content': _('Content of article 2')},
        ]
    }
    return render(request, 'main/article_list.html', context)
