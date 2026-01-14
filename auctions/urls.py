from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:nome_id>/", views.listining, name="listning"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("categories/", views.categories, name="categories"),
    path("categories/<int:nome_id>/", views.categories_list, name="categories_list"),
    path("create_Listing/", views.create_Listing, name="create_Listing"),
]
