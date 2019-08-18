from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleCreationForm, ArticleEditForm


def articleListView(request):
    articles = Article.objects.all().order_by('created')
    context = {'articles': articles}
    return render(
        request,
        template_name='articles/article_list.html',
        context=context
    )

def articleDetailView(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(
        request,
        template_name='articles/article_detail.html',
        context=context
    )

@login_required(login_url="/accounts/login")
def articleCreateView(request):
    if request.method == 'POST':
        form = ArticleCreationForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:article_list')

    else:
        form = ArticleCreationForm()

    context = {'form': form}
    return render(
        request,
        template_name='articles/article_create.html',
        context=context
    )

@login_required(login_url="/accounts/login")
def articleEditView(request, slug):
    if request.method == 'POST':
        form = ArticleEditForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('articles:articles_list')
        else:
            article = Article.objects.get(slug=slug)
            form = ArticleEditForm(instance=article)

    context = {'form': form, 'article': article}
    return render(
        request,
        template_name='articles/article_edit.html',
        context=context
    )