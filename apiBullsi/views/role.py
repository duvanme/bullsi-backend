from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apiBullsi.models import Role
from apiBullsi.serializers import RoleSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]