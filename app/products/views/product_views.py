from common.provider import CleanCodeResponseObject
from drf_yasg.utils import swagger_auto_schema
from products.messages import ProductsMessages
from products.models import Product
from products.serializers.product_serializers import ProductSerializer
from rest_framework.views import APIView


class ProductList(APIView):
    """
    List all products, or create a new product.
    """

    @swagger_auto_schema(
        responses={200: ProductSerializer(many=True)},
    )
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return CleanCodeResponseObject(serializer.data)

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={200: ProductSerializer(many=False)},
    )
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CleanCodeResponseObject(serializer.data)
        return CleanCodeResponseObject(message=ProductsMessages.PRODUCT_CREATE_FAILED)


class ProductRetrieve(APIView):
    """
    Retrieve, update or delete a Product.
    """

    def get_product(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return CleanCodeResponseObject(message=ProductsMessages.PRODUCT_NOT_FOUND)

    @swagger_auto_schema(
        responses={
            200: ProductSerializer(many=False),
        },
    )
    def get(self, request, pk, format=None):
        product = self.get_product(pk)
        serializer = ProductSerializer(product)
        return CleanCodeResponseObject(serializer.data)

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={
            200: ProductSerializer(many=False),
        },
    )
    def put(self, request, pk, format=None):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CleanCodeResponseObject(serializer.data)
        return CleanCodeResponseObject(message=ProductsMessages.PRODUCT_UPDATE_FAILED)

    @swagger_auto_schema(
        responses={
            200: "Delete product successfully",
        },
    )
    def delete(self, request, pk, format=None):
        Product = self.get_product(pk)
        Product.delete()
        return CleanCodeResponseObject()
