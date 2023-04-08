from django import forms
from webone.models import Personal_Details
from webone.models import Prant_Details
from webone.models import PUPIL_Details
class Personal_DetailsForm(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = "__all__"

class Prant_DetailsForm(forms.ModelForm):
    class Meta:
        model = Prant_Details
        fields = "__all__"

class PUPIL_DetailsForm(forms.ModelForm):
    class Meta:
        model = PUPIL_Details
        fields = "__all__"