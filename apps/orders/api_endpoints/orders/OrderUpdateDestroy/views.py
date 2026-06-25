from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orders.api_endpoints.orders.OrderUpdateDestroy.serializers import OrderUpdateDestroySerializer
from apps.orders.models import Order

@api_view(['PATCH', 'DELETE'])
def order_update_destroy_view(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status = 404)
    
    if request.method == 'PATCH':
        serializer = OrderUpdateDestroySerializer(order, data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderUpdateDestroySerializer(order).data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=204)