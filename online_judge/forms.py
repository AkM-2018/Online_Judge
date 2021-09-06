from django.forms import ModelForm, FileInput
from .models import Solution


class SubmitSolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['submitted_code']
        widgets = {
            'submitted_code': FileInput(attrs={'accept': '.py,.cpp'}),
        }
