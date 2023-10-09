from django.shortcuts import render

def video(request, slug):
    return render(request, 'app_aperitivos/video.html')
