from django import forms
from Finance.models import Uploads

class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ('description', 'document', )