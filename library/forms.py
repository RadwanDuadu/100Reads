from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'rating']  # Include rating here
        widgets = {
            'rating': forms.Select(
                choices=[
                    (i, f'{i} Star{"s" if i > 1 else ""}')
                    for i in range(1, 6)
                ]
            )
        }
