from rest_framework import viewsets, status
from apiBullsi.models import User
from apiBullsi.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        Allow unauthenticated POST (create), login, and refresh_token requests.
        All other actions require authentication.
        """
        if self.action in ['create', 'login', 'refresh_token']:
            return [AllowAny()]
        return [IsAuthenticated()]

    
    def create(self, request, *args, **kwargs):
        """Override create to hash password before saving."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Hash the password before saving
        user = serializer.save(
            password = make_password(request.data['password']),
            role_id = 3  # Default role assignment (e.g., 'customer')
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request, *args, **kwargs):
        """Handle user login using JWT authentication."""
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user':{
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'role': user.role.name if user.role else None,
                }
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def refresh_token(self, request):
        """Refresh access token using refresh token"""
        refresh = request.data.get('refresh')
        try:
            refresh_token = RefreshToken(refresh)
            return Response({
                'access': str(refresh_token.access_token),
            }, status=status.HTTP_200_OK)
        except:
            return Response(
                {'error': 'Invalid refresh token'},
                status=status.HTTP_401_UNAUTHORIZED
            )