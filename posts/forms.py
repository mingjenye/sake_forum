from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'sake_name', 'content', 'image', 'rating', 'purchase_location', 'drinking_occasion']
        labels = {
            'name': 'Nickname',
            'sake_name': '日本酒名',
            'content': '感想',
            'purchase_location': '購入場所',
            'drinking_occasion': '飲んだシーン',
            'rating': '評価',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'sake_name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'purchase_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '例：〇〇酒店、〇〇スーパー'}),
            'drinking_occasion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': '例：友人との食事会、家飲み'}),
        }
