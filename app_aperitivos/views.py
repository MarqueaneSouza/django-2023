from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('app_aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Vídeo Aperitivo: Motivação',  737734204),
    Video('instalacao-windows', 'Instalação Windows',  251497668),
]

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'app_aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'app_aperitivos/video.html', context={'video': video})
