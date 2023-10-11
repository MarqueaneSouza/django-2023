from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 737734204},
    # se eu controlo os títulos e os ids respectivos, eu pdoerei usar o template para qualquer vídeo.
    {'slug': 'instalacao-windows', 'titulo': 'Instalação Windows', 'vimeo_id': 251497668},
]

videos_dct = {dct['slug']: dct for dct in videos}

def indice(request):
    return render(request, 'app_aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'app_aperitivos/video.html', context={'video': video})
