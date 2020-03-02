from django.urls import include, path

urlpatterns = [
    path('auth/', include('api_auth.urls')),
    path('doctor/', include('api_doctor.urls')),
    path('patient/', include('api_patient.urls')),
]
