from django import forms
from .models import quadrilateral

class UserForm(forms.ModelForm):
    class Meta:
        model=quadrilateral
        fields =('Name','Figure','Sides','Angles','Diagonals')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'