from django import forms
from .models import App,Screenshot,Review
from django.forms.models import inlineformset_factory

class AppSubmissionForm(forms.ModelForm):
    class Meta:
        model = App
        fields = [
            'app_name', 'app_version', 'category', 'supported_platforms', 'apk_file',
            'app_icon', 'cover_graphics', 'promotional_video',
            'description', 'tags', 'privacy_policy_url', 'release_notes','ios_url','web_portal'
        ]
        widgets = { 'supported_platforms': forms.CheckboxSelectMultiple, }
        
class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = ['screenshot']

ScreenshotFormSet = inlineformset_factory(App, Screenshot, form=ScreenshotForm, extra=1)



    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Write your review here...'})
        }