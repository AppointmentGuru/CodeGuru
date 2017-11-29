from rest_framework import routers, serializers, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Code, ProcessCode

class ProcessCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessCode
        fields = '__all__'

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'description')
    filter_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name',)


class ProcessCodeViewSet(viewsets.ModelViewSet):
    queryset = ProcessCode.objects.all()
    serializer_class = ProcessCodeSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    search_fields = ('name', 'description')
    filter_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name',)

router = routers.DefaultRouter()
router.register(r'codes', CodeViewSet)
router.register(r'processcodes', ProcessCodeViewSet)

