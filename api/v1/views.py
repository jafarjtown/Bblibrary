from app.models import Material, Course, PastQuestion
from rest_framework import viewsets
from rest_framework import permissions

from api.v1.serializers import MaterialSerializer, CourseSerializer, PastQSerializer


from rest_framework_word_filter import FullWordSearchFilter 
from url_filter.integrations.drf import DjangoFilterBackend




class MaterialViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows materials to be viewed or edited.
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_fields = ['course','title', "upload_on"]
    filter_backends = (FullWordSearchFilter,DjangoFilterBackend )
    word_fields = ('title','comment')
    
    
class CourseViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = (FullWordSearchFilter,DjangoFilterBackend )
    word_fields = ('title','info','code')
    filter_fields = ["department", "level"]
    
class PassQViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows pass questions to be viewed or edited.
    """
    queryset = PastQuestion.objects.all()
    serializer_class = PastQSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
