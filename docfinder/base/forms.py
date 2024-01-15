from django.forms import ModelForm
from .models import Physician


class PhysicianForm(ModelForm):
    class Meta:
        model = Physician
        fields = "__all__"