from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ContactForm(forms.Form, ):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))



# form for user profile

class ProfileForm(forms.ModelForm):
    # create countires list for country field
    countries = Profile.objects.values_list('country', 'country').distinct()
    country = forms.ChoiceField(choices=countries, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['image', 'country', 'address', 'phone', 'linkedin_url', 'bio', 'Dream_Job', 'date_of_birth', 'destination']
        labels = {'image': 'Profile Picture', 'country': 'Country', 'address': 'Address', 'phone': 'Phone', 'linkedin_url': 'LinkedIn URL', 'bio': 'Bio', 'Dream_Job': 'Dream Job', 'date_of_birth': 'Date of Birth', 'destination': 'Destination'}
        widgets = {'image': forms.FileInput(attrs={'class': 'form-control-file'}), 'country': forms.Select(attrs={'class': 'form-control'}), 'address': forms.TextInput(attrs={'class': 'form-control'}), 'phone': forms.TextInput(attrs={'class': 'form-control'}), 'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}), 'bio': forms.Textarea(attrs={'class': 'form-control'}), 'Dream_Job': forms.TextInput(attrs={'class': 'form-control'}), 'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}), 'destination': forms.TextInput(attrs={'class': 'form-control'})}
  
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'username': 'Username', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'})}


