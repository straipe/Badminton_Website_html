from django import forms
from .models import Match, Review

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['manager','title','photo','address',
                  'match_day','match_time','match_rank','cost']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['message','satisfaction']
        widgets = {
            "message":forms.Textarea(attrs={"rows": 2}),
        }