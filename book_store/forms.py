
from django import forms
from .models import BookName
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'author', 'price', 'created_date', 'category',)
        widgets = {
            'price': forms.TextInput(attrs={'class': 'book_price'}),
        }

class BookNameForm(forms.ModelForm):

    class Meta:
        model = BookName
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
        fields = ('name',)