from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from apiBullsi.models import Store
from apiBullsi.serializers import StoreSerializer

class StoreViewSet(viewsets.ModelViewSet):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Check if user has one store before creating a new one."""
        # request.user is the User object. We need its ID to check against user_id integer field.
        if Store.objects.filter(user_id=request.user.id).exists():
            return Response(
                {"detail": "User can only have one store."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user's ID to the store
        serializer.save(user_id=self.request.user.id)
    

    



