from django.shortcuts import render

# Exemplo de dados fictícios, cada médico tem todos os campos necessários
DOCTORS = [
    {
        'id': 1,
        'name': 'Maria Adriana Cruz',
        'specialty': 'Medicina Integrativa',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Adriana.jpg?...',
        'description': 'Médica com 10 anos de experiência em hospitais públicos.',
        'value': '420,00',
        'consultation_duration': '50 min',

        # Campos adicionais para o perfil
        'crm': 'CRM 12345',
        'city': 'Rio de Janeiro',
        'uf': 'RJ',
        'reviews_count': 10,
        'views': 153,
        'patologias': 'Ansiedade, Depressão...',
        'atendimento': 'Adultos',
        'convenio': 'Sim',
        'retorno_info': '2 meses',
        'experiencia': 'Especialista em fitocanabinoides...',
        'formacao': [
            {'instituicao': 'UFRJ', 'descricao': 'Graduação em Medicina'},
            {'instituicao': 'WeCann Academy', 'descricao': 'Curso de Medicina Canabinóide'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 2,
        'name': 'Bruno Paladini',
        'specialty': 'Medicina de Família e Comunidade',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/bruno.jpg?...',
        'description': 'Médico de família, com conhecimento aprofundado no uso dos canabinoides.',
        'value': '800,00',
        'consultation_duration': '90 min',

        'crm': 'CRM 199359',
        'city': 'São Paulo',
        'uf': 'SP',
        'reviews_count': 20,
        'views': 369,
        'patologias': 'Ansiedade, Insônia, Depressão...',
        'atendimento': 'Adultos e Idosos',
        'convenio': 'Não',
        'retorno_info': '3 meses',
        'experiencia': 'Especializado em uso de fitocanabinoides...',
        'formacao': [
            {'instituicao': 'UNIARA', 'descricao': 'Graduação em Medicina'},
            {'instituicao': 'WeCann Academy', 'descricao': 'Curso de Medicina Canabinóide'},
        ],
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
        'instagram': 'https://instagram.com/drbruno',
        'facebook': 'https://facebook.com/drbruno',
    },
    {
        'id': 3,
        'name': 'Luisa Freitas Ramos',
        'specialty': 'Dermatologia',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Luisa_de_Freitas_Ramos.jpg?...',
        'description': 'Dermatologista com foco em procedimentos estéticos e clínicos.',
        'value': '420,00',
        'consultation_duration': '60 min',

        'crm': 'CRM 556677',
        'city': 'Belo Horizonte',
        'uf': 'MG',
        'reviews_count': 12,
        'views': 220,
        'patologias': 'Acne, Psoríase, Rosácea...',
        'atendimento': 'Adolescentes, Adultos',
        'convenio': 'Não',
        'retorno_info': '1 mês',
        'experiencia': 'Grande experiência em procedimentos estéticos e uso de canabinoides em dermatologia.',
        'formacao': [
            {'instituicao': 'UFMG', 'descricao': 'Graduação em Medicina'},
            {'instituicao': 'WeDerm Academy', 'descricao': 'Especialização em Dermatologia'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
]

def lista_medicos(request):
    context = {
        'doctors': DOCTORS,
        'resolution': '1920x1080',  # Exemplo de resolução principal
    }
    return render(request, 'doctors/lista_medicos.html', context)


def perfil_medico(request, medico_id):
    # Localiza o médico pelo ID
    doctor = next((d for d in DOCTORS if d['id'] == medico_id), None)
    if not doctor:
        # Se não encontrado, retorna 404 (ou use get_object_or_404 se tiver model real)
        return render(request, '404.html', status=404)

    context = {
        'doctor': doctor,
        'resolution': '1920x1080',
    }
    return render(request, 'doctors/perfil_medico.html', context)
