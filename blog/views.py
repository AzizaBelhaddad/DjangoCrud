from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from account.models import Profile
from .models import Article, Category
from .forms import ArticleForm

# Create your views here.

def index(request):
    # articles = Article.objects.filter(state=1, deleted=0)
    # categories = Category.objects.filter(state=1)
    # return render(request,'index.html', {
    #     "articles":articles,
    #     "categories": categories
    # })

    articles = Article.objects.filter(state=1)
    categories = Category.objects.filter(state=1)
    profiles = Profile.objects.filter(state=1)
    return render(
        request, "index.html", {"articles": articles, "categories": categories, "profiles": profiles}
    )


def show(request, slug):
    article = Article.objects.get(slug=slug)
    # my_article = None
    # for article in data:
    #     if article["id"] == id:
    #         my_article = id


    return render(request,'show.html', {'article': article})

def articlesbycateg(request, id):
    articlescateg = Article.objects.filter(category=id)

    return render(request,'articlesbycategory.html', {'articlescateg': articlescateg})


def create(request):

    form = ArticleForm
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("list_articles")
    return render(request, 'create.html', {
        "form": form
    })


def edite(request, slug):

    # article = get_object_or_404(Article, slug=slug)
    
    article = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)


    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid:
            form.save()
            return redirect("list_articles")
    
    return render(request, 'edite.html', {
        "form": form
    })



def delete(request, id):  
    article = Article.objects.filter(pk=id)
    if request.method == "POST":
        article.softdelete()
        
        
    return redirect("list_articles")
    return render(request, 'delete.html', {
           "article": article})
