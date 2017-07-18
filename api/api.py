from rest_framework import routers, serializers, viewsets, filters
from .models import Code

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'description')
    ordering_fields = ('name',)
    ordering = ('name',)

router = routers.DefaultRouter()
router.register(r'codes', CodeViewSet)

