from django.urls import path
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView, ItemReportView, ContactStaffView

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
    path('post/', ItemCreateView.as_view(), name='post-item'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update-item'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete-item'),
    path('report/', ItemReportView.as_view(), name='report-item'),
     path('contact/', ContactStaffView.as_view(), name='contact-staff'),
]
