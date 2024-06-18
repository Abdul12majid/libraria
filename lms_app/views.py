from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Cart
# Create your views here.


def index(request):
	return render(request, 'index_3.html')

@login_required(login_url='login-user')
def inventory(request):
	user = request.user
	books_taken = user.profile.books_taken.all().order_by('-id')
	total = user.profile.books_price + 5
	book_count = user.profile.books_taken.count()
	price = user.profile.books_price
	latest = Book.objects.order_by('-id').first()
	books = Book.objects.all().order_by('-id')
	total_count = Book.objects.count()
	context = {
		'books_taken':books_taken,
		"latest":latest,
		'total_count':total_count,
		"book_count":book_count,
		'user':user,
		'books':books,
		'total':total,
		'price':price,
	}
	return render(request, 'inventory.html', context)

def cart(request):
	user = request.user
	books = user.profile.books_taken.all().order_by('-id')
	count = books.count()
	context = {
		'user':user,
		'books':books,
		'count':count,
	}
	return render(request, 'cart.html', context)


def collect_book(request, pk):
	user = request.user
	book_id = Book.objects.get(name=pk)
	if book_id.book_count >= 1:
		if user.profile.books_taken.filter(name=book_id).exists():
			pass
		else:
			user.profile.books_taken.add(book_id)
			user.profile.save()
			price = book_id.book_price
			total_price = user.profile.books_price + price
			user.profile.books_price = total_price
			user.profile.save()
			x = book_id.book_count - 1
			book_id.book_count = x
			book_id.save()
	else:
		print('Not enough book')
	
	context = {

	}
	return redirect('inventory')


def return_book(request, pk):
	user = request.user
	book_id = Book.objects.get(name=pk)
	
	user.profile.books_taken.remove(book_id)
	user.profile.save()
	price = book_id.book_price
	new_price = user.profile.books_price - price
	user.profile.books_price = new_price
	user.profile.save()
	x = book_id.book_count + 1
	book_id.book_count = x
	book_id.save()
	
	return redirect('cart')

def check_out(request):
	user = request.user
	books = user.profile.books_taken.all().order_by('-id')
	total = user.profile.books_price + 5
	price = user.profile.books_price
	context = {
		'user':user,
		'books':books,
		'total':total,
		'price':price,

	}
	return render(request, 'checkout.html', context)

def search(request):
	if request.method == "POST":
		name = request.POST['keywords']
		books = Book.objects.filter(name__contains=name)

		context = {
			"name":name,
			"books":books,

		}
		return render(request, 'search.html', context)
	return render(request, 'search.html')