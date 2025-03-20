from django.shortcuts import render, get_object_or_404

# Exemplo de dados fictícios:
DOCTORS = [
    {
        'id': 1,
        'name': 'Maria Adriana Cruz',
        'specialty': 'Medicina Integrativa',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Adriana.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=tEE1iyojY34tOfrnfIPQ%2F20250319%2Fbrazil%2Fs3%2Faws4_request&X-Amz-Date=20250319T235917Z&X-Amz-Expires=588000&X-Amz-SignedHeaders=host&X-Amz-Signature=efa7dca7b16efd5a872b7967b65194360eb13aade864f136bf9e54c8674c21be',
        'description': 'Cardiologista com 10 anos de experiência em hospitais públicos.',
        'value': '420,00',
        'consultation_duration': '50 min'
    },
    {
        'id': 2,
        'name': 'Bruno Paladini',
        'specialty': 'Medicina de Familia e Comunidade',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/bruno.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=tEE1iyojY34tOfrnfIPQ%2F20250319%2Fbrazil%2Fs3%2Faws4_request&X-Amz-Date=20250319T235917Z&X-Amz-Expires=588000&X-Amz-SignedHeaders=host&X-Amz-Signature=35f5fc7c3ea487036302eb9ee0d7f826dc9773a1046382d3195a6c2ee9191532',
        'description': 'Pediatra renomada, especializada em neonatologia.',
        'value': '800,00',
        'consultation_duration': '90 min'
    },
    {
        'id': 3,
        'name': 'Luisa Freitas Ramos',
        'specialty': 'Dermatologia',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Luisa_de_Freitas_Ramos.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=tEE1iyojY34tOfrnfIPQ%2F20250319%2Fbrazil%2Fs3%2Faws4_request&X-Amz-Date=20250319T152608Z&X-Amz-Expires=588000&X-Amz-SignedHeaders=host&X-Amz-Signature=5f99eb8a36861bec59d1fc552742e9fb4110f7fe0a1012c8f14553cb2383465e',
        'description': 'Dermatologista com foco em procedimentos estéticos e clínicos.',
        'value': '420,00',
        'consultation_duration': '60 min'
    },
]

def lista_medicos(request):
    context = {
        'doctors': DOCTORS,
        'resolution': '1920x1080',  # Exemplo de resolução principal
    }
    return render(request, 'doctors/lista_medicos.html', context)

def perfil_medico(request, doctor_id):
    # Localiza o médico pelo ID na lista fictícia
    doctor = next((d for d in DOCTORS if d['id'] == doctor_id), None)
    if not doctor:
        # Exemplo simples de 404
        # ou use: doctor = get_object_or_404(Model, pk=doctor_id) se usar banco
        return render(request, '404.html', status=404)

    context = {
        'doctor': doctor,
        'resolution': '1920x1080',
    }
    return render(request, 'doctors/perfil_medico.html', context)
