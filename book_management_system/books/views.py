from django.shortcuts import render,redirect
from .models import Books
from .forms import BookForms

# Create your views here.
def homepage(request):
    books = Books.objects.all()
    print(books)

    return render(request,'book_list.html',{'books' :books})


def add_book(request):
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForms()
        return render(request,'add_book.html',{'form':form})
    

def delete_book(request,book_id):
    book = Books.objects.get(id=book_id)
    if book:
        book.delete()

    return redirect('homepage')

def update_book(request,book_id):
    specific_book = Books.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForms(request.POST, instance=specific_book)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForms(instance=specific_book)
        return render(request,'add_book.html',{'form':form})