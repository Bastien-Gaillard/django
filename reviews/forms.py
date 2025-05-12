from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, show_content=True, show_rating=True, **kwargs):
        super().__init__(*args, **kwargs)
        if not show_content:
            self.fields.pop('content')
        if not show_rating:
            self.fields.pop('user_rating')

    class Meta:
        model = Review
        fields = ['content', 'user_rating']
        widgets = {
            'user_rating': forms.Select(choices=[(i, i) for i in range(1, 6)])
        }
