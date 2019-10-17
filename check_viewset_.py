#<--------------------------------------------- .Serializer----------------------------------------------------->

class EmpoyeeSerializer(serializer.HyperlinkModelSerializer):
  class Meta:
    fields=(
      'first_name',
      'last_name',
      'email',
      'url')
    
# class EmpoyeeSerializer(serializer.ModelSerializer):
#   class Meta:
#     #fields='__all__'
#     fields=(
#       'first_name',
#       'last_name',
#       'email',
#       'url')

# class EmpoyeeSerializer(serializer.Serializer):
Need to be edited
#   class Meta:
#     #fields='__all__'
#     fields=(
#       'first_name',
#       'last_name',
#       'email',
#       'url')

#<----------------------------------------------   .views -------------------------------------------------------->
from rest_framework import viewsets
from .serializers import EmpoyeeSerializer

class EmployeeViewset(viewsets.ModelViewset):
  queryset = User.objects.all()
  serializer_class = EmployeeSerializer
  

#<----------------------------------------------   Project urls -------------------------------------------------------->
urlpatterns = [
  path('api/v1/',include('employee.api_urls'))
]
#<----------------------------------------------   .api_urls ----------------------------------------------------------->
from rest_framework import routers

routes=routers.DefaultRouter()
router.register('',EmployeeViewset)

urlpatterns = [
  path('employee',include('router.urls'))
]
