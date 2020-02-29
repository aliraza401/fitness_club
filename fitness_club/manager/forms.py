from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from manager.models import Fee , Admin , Member , Trainer

class AdminCreateForm(UserCreationForm):

    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'



class TrainerForm(forms.ModelForm):
    
    class Meta():
        model =  Trainer
        fields = ( 'name','username','email','password' )

        weights = {
            'name' : forms.TextInput(attrs={'class':''}),
            'username' : forms.Textarea(attrs={'class':''}),
            'email' : forms.TextInput(attrs={'class':''}),
            'password' : forms.Textarea(attrs={'class':''})
        }

class MemberForm(forms.ModelForm):
    
    class Meta():
        model =  Member
        fields = ( 'name','username','email','password','age','height','weight' )

        weights = {
            'name' : forms.TextInput(attrs={'class':''}),
            'username' : forms.Textarea(attrs={'class':''}),
            'email' : forms.TextInput(attrs={'class':''}),
            'password' : forms.Textarea(attrs={'class':''}),
            'age' : forms.Textarea(attrs={'class':''}),
            'height' : forms.TextInput(attrs={'class':''}),
            'weight' : forms.Textarea(attrs={'class':''})
        }


class  FeeForm(forms.ModelForm):
    class Meta():
        model =  Fee
        fields = ( 'member','amount','month')

        weights = {
            'member' : forms.TextInput(attrs={'class':''}),
            'amount' : forms.Textarea(attrs={'class':''}),
            'month' : forms.TextInput(attrs={'class':''}),
        }


class SearchForm(forms.Form):
  data = forms.CharField()

  def process(self):
    return self.cleaned_data 
