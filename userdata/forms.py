from django import forms
from .models import UserDataDetail,MultipleImg



class PostFormDetail(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Folder Title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter somthing here'}))
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = UserDataDetail
        fields = ('title','description','image',)
