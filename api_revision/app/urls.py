from django.urls import path
from . import views


urlpatterns = [
    path('product/',views.ProductGetCreate.as_view(),name='product'),
    path('product/<int:pk>/',views.ProductRetrieveUpdateDelete.as_view(),name='productRUD')
]
