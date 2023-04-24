from common.decorators import parse_request
from django.utils.decorators import method_decorator
from orders.serializers import CreateOrderSerializer, UpdateOrderSerializer
from orders.services import OrderServices
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class OrderIdAPI(APIView):
    """
    1. API lấy chi tiết 1 đơn hàng của user
    2. API cập nhật thông tin đơn hàng user

    Args:
        pk: id của order
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """API lấy chi tiết 1 đơn hàng của user

        Args:
            request (_type_): _description_
            pk (_type_): _description_

        Returns:
            _type_: _description_
        """
        order = OrderServices.get(request.user, pk)
        return order

    @method_decorator(parse_request(UpdateOrderSerializer))
    def put(self, request, pk):
        """API cập nhật thông tin đơn hàng user

        Args:
            request (_type_): _description_
            pk (_type_): _description_

        Returns:
            _type_: _description_
        """
        order = OrderServices.update(request.user, pk, request.data)
        return order


class OrderAPI(APIView):
    """
    1. API lấy danh sách các đơn hàng của user
    2. API tạo đơn hàng của user
    Args:

    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """API lấy danh sách các đơn hàng của user

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        order = OrderServices.list(request.user)
        return order

    @method_decorator(parse_request(CreateOrderSerializer))
    def post(self, request):
        """API tạo đơn hàng của user

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        order = OrderServices.create(request.user, request.data)
        return order
