
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Book
from .forms import BookForm
from .forms import BookNameForm


def book_detail(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'book_store/book_detail.html', {'book': book})

def book_list(request):
	books = Book.objects.all()
	return render(request, 'book_store/book_list.html', {'books' : books})

def add_new_book(request):
	if(request.method == "POST"):
		form = BookForm(request.POST)
		if(form.is_valid()):
			book = form.save(commit=False)
			book.add_book(request.POST.get("name"))
			return redirect('book_detail', pk=book.pk)
	else:
		form = BookForm() 
	return render(request, 'book_store/book_edit.html', {'form': form})

def add_new_name(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		b_name = Book.objects.all()[0]
		form = BookNameForm(request.POST, instance=b_name)
		if form.is_valid():
			b_name = form.save(commit=False)
			book.add_name(b_name.name)
			book.save()
			return redirect('book_detail', pk=book.pk)
	else:
	    form = BookNameForm(instance=book)
	return render(request, 'book_store/book_name_edit.html', {'form': form})
