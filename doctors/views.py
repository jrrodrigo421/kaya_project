from django.shortcuts import render, get_object_or_404

# Exemplo de dados fictícios:
DOCTORS = [
    {
        'id': 1,
        'name': 'Dr. João Silva',
        'specialty': 'Cardiologia',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Luisa_de_Freitas_Ramos.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=tEE1iyojY34tOfrnfIPQ%2F20250319%2Fbrazil%2Fs3%2Faws4_request&X-Amz-Date=20250319T152608Z&X-Amz-Expires=588000&X-Amz-SignedHeaders=host&X-Amz-Signature=5f99eb8a36861bec59d1fc552742e9fb4110f7fe0a1012c8f14553cb2383465e',
        'description': 'Cardiologista com 10 anos de experiência em hospitais públicos.'
    },
    {
        'id': 2,
        'name': 'Dra. Maria Oliveira',
        'specialty': 'Pediatria',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Luisa_de_Freitas_Ramos.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=tEE1iyojY34tOfrnfIPQ%2F20250319%2Fbrazil%2Fs3%2Faws4_request&X-Amz-Date=20250319T152608Z&X-Amz-Expires=588000&X-Amz-SignedHeaders=host&X-Amz-Signature=5f99eb8a36861bec59d1fc552742e9fb4110f7fe0a1012c8f14553cb2383465e',
        'description': 'Pediatra renomada, especializada em neonatologia.'
    },
    {
        'id': 3,
        'name': 'Dr. Carlos Souza',
        'specialty': 'Dermatologia',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Luisa_de_Freitas_Ramos.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=tEE1iyojY34tOfrnfIPQ%2F20250319%2Fbrazil%2Fs3%2Faws4_request&X-Amz-Date=20250319T152608Z&X-Amz-Expires=588000&X-Amz-SignedHeaders=host&X-Amz-Signature=5f99eb8a36861bec59d1fc552742e9fb4110f7fe0a1012c8f14553cb2383465e',
        'description': 'Dermatologista com foco em procedimentos estéticos e clínicos.'
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
