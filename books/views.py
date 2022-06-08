# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout

from django.contrib import messages

from .models import Book
from .forms import BookForm,CustomUserCreationForm
from django.contrib.auth.models import User
# Create your views here.



def loginUser(request):
    if request.user.is_authenticated:
        return redirect('books')
    
    if request.method == 'POST':
        user = None
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user:
                username = user.username
                user = authenticate(username=username,password=password)
        except:
            messages.info(request," email or Password is incorrect ")

        if user is not None:
            login(request,user)
            messages.info(request,"logged in succesfully")
            return redirect('books')


    return render(request,'books/login.html')



@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request,"User logged out successfully")
    return redirect('login')

    #return render(request,'books/login.html')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('login')
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request,"User account created successfully")
            return redirect('login')

    context = {'form':form}
    return render(request,'books/register.html',context)




def books(request):
    # if request.user.is_authenticated:
    #     #user       = request.user
    #     books = request.user.book_set.all()
    # else:
    #     books = Book.objects.all()

    books = Book.objects.all()
    context={'books':books}
    return render(request,'books/books.html',context)


@login_required(login_url='login')
def addBook(request):
    user = request.user
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            messages.success(request,"New Book added succesfully")
            return redirect('books') 

    context = {'form':form}
    return render(request,'books/book_form.html',context)
    

@login_required(login_url='login')
def updateBook(request,pk):
    candidate = Book.objects.get(id=pk)
    form = BookForm(instance=candidate)

    if request.method == 'POST':
        form = BookForm(request.POST,instance=candidate)
        if form.is_valid():
            form.save()
            messages.info(request,"Book information updated succesfully")
            return redirect('books')

    context = {'form':form}
    return render(request,'books/book_form.html',context)


@login_required(login_url='login')
def deleteBook(request,pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        messages.info(request,"Book deleted succesfully")
        return redirect('books')

    context = {'book':book}
    return render(request,'books/delete-book.html',context)