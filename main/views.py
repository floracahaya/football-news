from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406350955',
        'name': 'Flora Cahaya Putri',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)