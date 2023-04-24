from django.urls import path
from products.views.product_views import ProductList, ProductRetrieve

urlpatterns = [
    path("/product", ProductList.as_view(), name="all_product"),
    path("/product/<int:pk>", ProductRetrieve.as_view(), name="retrieve-product"),
]
