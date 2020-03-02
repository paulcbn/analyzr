from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from api_core.models import PatientProfile, DoctorProfile


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = tuple()


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ('verified',)


class GetPatientSerializer(serializers.ModelSerializer):
    patient_profile = PatientProfileSerializer()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'user_type', 'patient_profile')


class GetDoctorSerializer(serializers.ModelSerializer):
    doctor_profile = DoctorProfileSerializer()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'user_type', 'doctor_profile')


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        password = password.strip()
        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
