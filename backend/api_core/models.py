from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    DOCTOR = 'doctor'
    PATIENT = 'patient'

    USER_TYPE_CHOICES = (
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    )
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES, default=PATIENT)


class PatientProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='patient_profile')

    def __str__(self):
        return f'{self.user.username} '


class DoctorProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='doctor_profile')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} (Verified: {self.verified}) '


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == User.DOCTOR:
            DoctorProfile.objects.create(user=instance)
        elif instance.user_type == User.PATIENT:
            PatientProfile.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == User.DOCTOR:
        if hasattr(instance, 'patient_profile'):
            instance.patient_profile.delete()
        if hasattr(instance, 'doctor_profile'):
            instance.doctor_profile.save()
        else:
            DoctorProfile.objects.create(user=instance)
    elif instance.user_type == User.PATIENT:
        if hasattr(instance, 'doctor_profile'):
            instance.doctor_profile.delete()
        if hasattr(instance, 'patient_profile'):
            instance.patient_profile.save()
        else:
            PatientProfile.objects.create(user=instance)
