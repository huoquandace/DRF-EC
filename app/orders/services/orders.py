from common.provider import CleanCodeResponseObject
from orders.messages import OrdersMessages
from orders.models import Order, OrderItem
from orders.serializers import OrderDetailSerializer


class OrderServices:
    """
    Các hàm xử lý cho order
    """

    model = Order
    sub_model = OrderItem

    @classmethod
    def list(cls, user):
        order = OrderServices.model.objects.filter(user=user)
        order_data = OrderDetailSerializer(order, many=True).data
        return CleanCodeResponseObject(data=order_data)

    @classmethod
    def get(cls, user, id):
        try:
            order = OrderServices.model.objects.get(id=id, user_id=user)
        except Order.DoesNotExist:
            return CleanCodeResponseObject(message=OrdersMessages.ORDER_NOT_FOUND)

        order_data = OrderDetailSerializer(order).data
        return CleanCodeResponseObject(data=order_data)

    @classmethod
    def update(cls, user, id, payload):
        try:
            order = OrderServices.model.objects.get(id=id, user_id=user)
        except Order.DoesNotExist:
            return CleanCodeResponseObject(message=OrdersMessages.ORDER_NOT_FOUND)
        order.status = payload.get("status")
        order.save()
        return CleanCodeResponseObject(data={"order_id": order.id})

    @classmethod
    def create(cls, user, payload):
        order = cls.model.objects.create(
            user_id=user, total_price=payload.get("total_price")
        )
        for it in payload.get("items"):
            cls.sub_model.objects.create(
                order=order,
                product_id=it.get("product_id"),
                quantity=it.get("quantity"),
            )
        return CleanCodeResponseObject(data={"order_id": order.id})
