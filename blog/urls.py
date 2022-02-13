import django


from django.urls import path
from .views import index, show,create,edite,delete,articlesbycateg

urlpatterns = [
    path("", index, name = "list_articles"),
    path("create/", create, name = "create_article"),
    path("edite/<int:slug>/", edite, name = "edite_article"),
    path("delete/<int:slug>/", delete, name = "delete_article"),

    # Categories
    # path("<int:id>/", articlesbycateg, name = "articles_by_categ"),
    path("<slug:slug>/", show, name = "show_article"),






]