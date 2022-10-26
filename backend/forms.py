from django.forms import ModelForm
from .models import User
from .models import Bee

class UserForm(ModelForm):
    class Meta:
        model = User        #tells django that this form uses the User model
        fields = '__all__'  #tells django to include all fields in the model. refer to https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/ 


class Bee(ModelForm):
    class Meta:
        model = Bee        #tells django that this form uses the User model
        fields = '__all__'  