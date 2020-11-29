from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .models import PhotoImage
from .forms import PhotoImageForm, ReviewForm

# Create your views here.
def index(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  # return HttpResponse(f'hello world')
  return render(request, 'main/index.html', {'posts': posts})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'main/post_detail.html', {'post': post})

def image_list(request):
  images = PhotoImage.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'main/image_list.html', {'images': images})

def image_detail(request, pk):
  image = get_object_or_404(PhotoImage, pk=pk)
  return render(request, 'main/image_detail.html', {'image': image})

def image_new(request):
  if request.method == "POST":
    form = PhotoImageForm(request.POST)
    if form.is_valid():
      image = PhotoImage()
      print(request)
      image.title = request.POST['title']
      image.link = request.POST['link']
      image.image = request.FILES['image']
      image.author = request.user
      image.published_date = timezone.now()
      image.save()
      return redirect('image_detail', pk=image.pk)
  else:
    form = PhotoImageForm()
  return render(request, 'main/image_new.html', {'form': form})

def add_review_to_image(request, pk):
  image = get_object_or_404(PhotoImage, pk=pk)
  if request.method == "POST":
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.save(commit=False)
      review.image = image
      review.save()
      return redirect('image_detail', pk=image.pk)
  else:
    form = ReviewForm()
  return render(request, 'main/add_review_to_image.html', {'form': form})