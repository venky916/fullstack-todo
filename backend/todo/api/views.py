from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializers
    # authentication_classes= [JWTAuthentication]
    # permission_classes=[IsAuthenticated,]
    
