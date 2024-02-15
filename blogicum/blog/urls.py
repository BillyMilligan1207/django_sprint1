from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts')
]
#здесь не совсем понял объяснения ошибки и как ее исправить, можете пожалуйста объяснить по-другому или в целом как это сделать и для чего)
# потому что еще в первом ревью не понял, если честно) вроде исправил, но не уверен просто