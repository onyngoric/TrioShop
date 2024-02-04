from django.shortcuts import render

# Create your views here.
def post(request):
    return render(request, 'admin_post.html')