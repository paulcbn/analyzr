from knox.views import LoginView as KnoxLoginView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from api_core.models import User
from .serializers import GetDoctorSerializer, GetPatientSerializer, LoginUserSerializer


class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        request.user = user
        return super(LoginAPI, self).post(request, format=None)


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.user.user_type == User.DOCTOR:
            return GetDoctorSerializer
        return GetPatientSerializer

    def get_object(self):
        return self.request.user
