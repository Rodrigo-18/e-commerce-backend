from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .models import Product
from rest_framework import filters, generics

class ProductAPIView(generics.ListAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def product(request, format=None):
    if request.user.is_superuser and request.user.is_staff:
        produto = request.data
        produto['owner'] = request.user.owner
        serializer = ProductSerializer(data=produto)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


