from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    path("<slug:slug>/", views.DetailView.as_view(), name="detail"),#如果用pk的话那么限制就太大了，根据后面这个原则所以改成slug，get_object() looks for a pk_url_kwarg argument in the arguments to the view; if this argument is found, this method performs a primary-key based lookup using that value. If this argument is not found, it looks for a slug_url_kwarg argument, and performs a slug lookup using the slug_field.
    path('category/<category>/', views.CategoryView.as_view(), name='category')
]
