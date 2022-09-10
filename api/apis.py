from rest_framework.generics import ListAPIView
from .serializers import BureauSerializer
from blog.models import Bureau

# Create your views here.
class BureauList(ListAPIView):
    serializer_class = BureauSerializer
    queryset = Bureau.objects.all()
