from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = 'api'
urlpatterns = [
    path('', ArticleListView.as_view(), name="list-view"),
    path('<int:pk>', ArticleDetailView.as_view(), name="detail-view"),
]
