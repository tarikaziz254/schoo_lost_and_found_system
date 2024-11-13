from django.urls import path
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
    path('post/', ItemCreateView.as_view(), name='post-item'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update-item'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete-item'),
]
