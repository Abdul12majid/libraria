from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Cart, Message, Inventory, Blog, Catalogue
from django.contrib.auth.models import User
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

@login_required(login_url='login-user')
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
			store = Inventory.objects.get(id=1)
			total_price = user.profile.books_price + price
			user.profile.books_price = total_price
			user.profile.save()
			x = book_id.book_count - 1
			book_id.book_count = x
			book_id.save()
			new_amount = store.book_count - 1
			store.book_count = new_amount
			store.save()
	else:
		print('Not enough book')
	
	context = {

	}
	return redirect('inventory')


def return_book(request, pk):
	user = request.user
	book_id = Book.objects.get(name=pk)
	store = Inventory.objects.get(id=1)
	user.profile.books_taken.remove(book_id)
	user.profile.save()
	price = book_id.book_price
	new_price = user.profile.books_price - price
	user.profile.books_price = new_price
	user.profile.save()
	x = book_id.book_count + 1
	book_id.book_count = x
	book_id.save()
	new_amount = store.book_count + 1
	store.book_count = new_amount
	store.save()
	
	return redirect('cart')

@login_required(login_url='login-user')
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


@login_required(login_url='login-user')
def contact(request):
	user = request.user
	messages = user.profile.message
	print(messages)
	if request.method == "POST":
		body = request.POST['message']
		message = Message.objects.create(sender=user, body=body)
		#message.save()
	context = {
		
			'user':user,
			'messages':messages,
		}
	return render(request, 'contact.html', context)


@login_required(login_url='login-user')
def dashboard(request):
	user = request.user
	if request.user.is_superuser:
		inventory = Inventory.objects.all()
		users = User.objects.count()
		users_in = User.objects.all()
		books = Book.objects.all().order_by('-id')[:10]
		blogs = Blog.objects.all().order_by('-id')[:5]
		catalogue = Catalogue.objects.all()
		books_taken = user.profile.books_taken.all()
		
		context = {
			"inventory":inventory,
			"users":users,
			"users_in":users_in,
			"books":books,
			"blogs":blogs,
			"catalogue":catalogue,
			"books_taken":books_taken,

		}
		return render(request, 'dashboard.html', context)
	else:
		return redirect('inventory')