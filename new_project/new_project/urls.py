"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.index),
    path('products/', views.product_list_view),
    path('products/<int:id>', views.product_detail_view),
    path('directors/', views.director_films),
    path('directors/<int:id>', views.director_film),
    path('movie/', views.movies_film),
    path('movie/<int:id>', views.movies_films),
    path('review/', views.review),
    path('review/<int:id>', views.review_list),
    path('category/<int:category_id>/products/', views.category_product_filter_view),
    path('add_product/', views.add_product_view),
    path('add_movie/', views.add_movie_view),
    path('add_director/', views.add_director_view),
    path('register/', views.register_view),
    path('login/', views.login_view),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
