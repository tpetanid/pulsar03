from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Owner URLs
    path('owners/', views.OwnerListView.as_view(), name='owner_list'),
    path('owners/add/', views.OwnerCreateView.as_view(), name='owner_create'),
    path('owners/<int:pk>/', views.OwnerDetailView.as_view(), name='owner_detail'),
    path('owners/<int:pk>/edit/', views.OwnerUpdateView.as_view(), name='owner_update'),
    path('owners/<int:pk>/delete/', views.OwnerDeleteView.as_view(), name='owner_delete'),
] 