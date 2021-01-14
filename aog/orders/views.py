from django.shortcuts import render
from .models import Order
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	context={
		'orders': Order.objects.all()
	}
	return render(request, 'orders/home.html',context)

class OrderListView(ListView):
	model=Order
	template_name='orders/home.html'
	context_object_name='orders'
	ordering=['-date_posted']

class OrderDetailView(DetailView):
	model=Order

class OrderCreateView(LoginRequiredMixin,CreateView):
	model=Order
	fields=['title','description','category','image']

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class OrderUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model=Order
	fields=['title','description','category','image']

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

class OrderDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Order
	success_url='/'
	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'orders/about.html',{'title': 'About'})
