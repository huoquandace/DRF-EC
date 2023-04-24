from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import UserData
from users.serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer


class UserList(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer


class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=CreateUserSerializer, responses={201: UserSerializer(many=False)}
    )
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")
        user = UserData.objects.create_user(name=name, email=email, password=password)
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "User created successfully",
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    serializer_class = LoginUserSerializer

    @swagger_auto_schema(
        request_body=LoginUserSerializer, responses={200: UserSerializer(many=False)}
    )
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")

            user = authenticate(request, email=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "message": "Login successful",
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Invalid username or password"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
