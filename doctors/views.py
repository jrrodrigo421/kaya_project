from django.shortcuts import render
from decimal import Decimal

DOCTORS = [
    {
        'id': 23,
        'name': 'Maria Adriana Cruz',
        'specialty': 'Medicina Integrativa',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Adriana.jpg?...',
        'description': 'Médica com 10 anos de experiência em hospitais públicos.',
        'value': '420,00',
        'consultation_duration': '50 min',
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
        'id': 4,
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
        'id': 6,
        'name': 'Luisa Freitas Ramos',
        'specialty': 'Medicina de Família e Comunidade',
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
    {
        'id': 10,
        'name': 'Ricardo Freire Gurgel',
        'specialty': 'Clínico Geral',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Ricardo_Gurgel.jpeg?...',
        'description': 'Clínico Geral com experiência diversificada em atendimento.',
        'value': '500,00',
        'consultation_duration': '30 min',
        'crm': 'CRM 987654',
        'city': 'Curitiba',
        'uf': 'PR',
        'reviews_count': 15,
        'views': 200,
        'patologias': 'Hipertensão, Diabetes...',
        'atendimento': 'Adultos',
        'convenio': 'Sim',
        'retorno_info': '1 mês',
        'experiencia': 'Atua com abordagem humanizada...',
        'formacao': [
            {'instituicao': 'UFPR', 'descricao': 'Graduação em Medicina'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 25,
        'name': 'Alexandre Sponchiado',
        'specialty': 'Clínico Geral',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/FOTO.jpg?...',
        'description': 'Clínico Geral com abordagem humanizada.',
        'value': '350,00',
        'consultation_duration': '60 min',
        'crm': 'CRM 112233',
        'city': 'Fortaleza',
        'uf': 'CE',
        'reviews_count': 8,
        'views': 180,
        'patologias': 'Problemas circulatórios...',
        'atendimento': 'Adultos e Idosos',
        'convenio': 'Não',
        'retorno_info': '2 meses',
        'experiencia': 'Possui larga experiência em medicina preventiva...',
        'formacao': [
            {'instituicao': 'UFC', 'descricao': 'Graduação em Medicina'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 8,
        'name': 'Bruna Sanches',
        'specialty': 'Medicina de Família e Comunidade',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Bruna_Sanches.jpg?...',
        'description': 'Médica com abordagem centrada na família.',
        'value': '320,00',
        'consultation_duration': '30 min',
        'crm': 'CRM 445566',
        'city': 'Recife',
        'uf': 'PE',
        'reviews_count': 9,
        'views': 140,
        'patologias': 'Infecções, Alergias...',
        'atendimento': 'Infantis e Adultos',
        'convenio': 'Sim',
        'retorno_info': '1 mês',
        'experiencia': 'Experiência em atendimento domiciliar...',
        'formacao': [
            {'instituicao': 'UFPE', 'descricao': 'Graduação em Medicina'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 16,
        'name': 'Guilherme Pagliari',
        'specialty': 'Clínico Geral',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Foto_de_Perfil_-_Guilherme_Z5myU8M.jpeg?...',
        'description': 'Clínico Geral com vasta experiência.',
        'value': '300,00',
        'consultation_duration': '90 min',
        'crm': 'CRM 778899',
        'city': 'Porto Alegre',
        'uf': 'RS',
        'reviews_count': 12,
        'views': 250,
        'patologias': 'Problemas cardíacos, Hipertensão...',
        'atendimento': 'Adultos e Idosos',
        'convenio': 'Não',
        'retorno_info': '2 meses',
        'experiencia': 'Atendimento humanizado com foco em prevenção...',
        'formacao': [
            {'instituicao': 'PUC-RS', 'descricao': 'Graduação em Medicina'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 11,
        'name': 'Arailton Neto',
        'specialty': 'Clínico Geral',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dr._Arailton_Neto.png?...',
        'description': 'Clínico Geral com abordagem prática e humanizada.',
        'value': '300,00',
        'consultation_duration': '60 min',
        'crm': 'CRM 334455',
        'city': 'Florianópolis',
        'uf': 'SC',
        'reviews_count': 7,
        'views': 130,
        'patologias': 'Problemas respiratórios...',
        'atendimento': 'Adultos',
        'convenio': 'Não',
        'retorno_info': '1 mês',
        'experiencia': 'Focado em tratamentos personalizados...',
        'formacao': [
            {'instituicao': 'UFSC', 'descricao': 'Graduação em Medicina'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 5,
        'name': 'Amanda Medeiros',
        'specialty': 'Clínico Geral',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/amanda.jpg?...',
        'description': 'Clínico Geral com foco em atendimento humanizado.',
        'value': '420,00',
        'consultation_duration': '30 min',
        'crm': 'CRM 998877',
        'city': 'Salvador',
        'uf': 'BA',
        'reviews_count': 11,
        'views': 170,
        'patologias': 'Problemas hormonais...',
        'atendimento': 'Adultos e Idosos',
        'convenio': 'Sim',
        'retorno_info': '1 mês',
        'experiencia': 'Atendimento com foco em qualidade de vida...',
        'formacao': [
            {'instituicao': 'UFBA', 'descricao': 'Graduação em Medicina'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 3,
        'name': 'Vitor Datolli',
        'specialty': 'Medicina de Família e Comunidade',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/vitor.jpg?...',
        'description': 'Médico com abordagem humanizada.',
        'value': '200,00',
        'consultation_duration': '30 min',
        'crm': 'CRM 555555',
        'city': 'Cidade Exemplo',
        'uf': 'EX',
        'reviews_count': 5,
        'views': 100,
        'patologias': 'Exemplo de patologias',
        'atendimento': 'Adultos',
        'convenio': 'Não',
        'retorno_info': '1 mês',
        'experiencia': 'Atende com foco em prevenção.',
        'formacao': [
            {'instituicao': 'Instituto Exemplo', 'descricao': 'Graduação em Medicina'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 70,
        'name': 'Vania Rosa Roman',
        'specialty': 'Medicina Preventiva e Social',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/PERFIL_DRA._VANIA.jpg?...',
        'description': 'Médica com foco em medicina preventiva e social.',
        'value': '400,00',
        'consultation_duration': 'None min',
        'crm': 'CRM 888888',
        'city': 'São Paulo',
        'uf': 'SP',
        'reviews_count': 0,
        'views': 0,
        'patologias': 'Não especificado',
        'atendimento': 'Não especificado',
        'convenio': 'Não',
        'retorno_info': 'Não especificado',
        'experiencia': 'Não especificado',
        'formacao': [],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 69,
        'name': 'DR CARLOS ALBERTO SCARPELLI',
        'specialty': 'MEDICINA DO TRABALHO',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/WhatsApp_Image_2025-02-13_at_18.33.20.jpeg?...',
        'description': 'Clínico Geral com abordagem prática e humanizada.',
        'value': '300,00',
        'consultation_duration': '30 min',
        'crm': 'CRM 999999',
        'city': 'Florianópolis',
        'uf': 'SC',
        'reviews_count': 7,
        'views': 0,
        'patologias': 'Problemas respiratórios...',
        'atendimento': 'Adultos',
        'convenio': 'Não',
        'retorno_info': '1 mês',
        'experiencia': 'Focado em tratamentos personalizados...',
        'formacao': [
            {'instituicao': 'UFSC', 'descricao': 'Graduação em Medicina'},
        ],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 1,
        'name': 'Isabela Junqueira',
        'specialty': 'Medicina de Família e Comunidade',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/Dra._Isabela_Junqueira.jpeg?...',
        'description': 'Médica com vasta experiência em atendimento humanizado.',
        'value': '539,00',
        'consultation_duration': '60 min',
        'crm': 'CRM 101010',
        'city': 'Cidade Y',
        'uf': 'YY',
        'reviews_count': 0,
        'views': 0,
        'patologias': 'Não especificado',
        'atendimento': 'Não especificado',
        'convenio': 'Não',
        'retorno_info': 'Não especificado',
        'experiencia': 'Não especificado',
        'formacao': [],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 65,
        'name': 'Rafael Garcia Eymael',
        'specialty': 'Clínico Geral',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/result_img_2024_09_10_08_27_17.jpg?...',
        'description': 'Clínico Geral com abordagem humanizada.',
        'value': '350,00',
        'consultation_duration': '30 min',
        'crm': 'CRM 121212',
        'city': 'Cidade Z',
        'uf': 'ZZ',
        'reviews_count': 0,
        'views': 0,
        'patologias': 'Não especificado',
        'atendimento': 'Não especificado',
        'convenio': 'Não',
        'retorno_info': 'Não especificado',
        'experiencia': 'Não especificado',
        'formacao': [],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 68,
        'name': 'Jean Pedro Maldaner Jacoby',
        'specialty': 'Medicina Funcional Integrativa',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/JEAN-98.jpeg?...',
        'description': 'Médico com ampla experiência em medicina funcional.',
        'value': '299,00',
        'consultation_duration': '45 min',
        'crm': 'CRM 131313',
        'city': 'Cidade W',
        'uf': 'WW',
        'reviews_count': 0,
        'views': 0,
        'patologias': 'Não especificado',
        'atendimento': 'Não especificado',
        'convenio': 'Não',
        'retorno_info': 'Não especificado',
        'experiencia': 'Não especificado',
        'formacao': [],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
    {
        'id': 77,
        'name': 'Haslling Gomes Rocha',
        'specialty': 'Clínico Geral',
        'photo': 'https://saude-kayamind-minio.aqrour.easypanel.host/kayadoc/media/medic_photos/result_img_2024_09_10_08_27_17.jpg?...',
        'description': 'Clínico Geral com vasta experiência.',
        'value': '350,00',
        'consultation_duration': '30 min',
        'crm': 'CRM 151515',
        'city': 'Cidade U',
        'uf': 'UU',
        'reviews_count': 0,
        'views': 0,
        'patologias': 'Não especificado',
        'atendimento': 'Não especificado',
        'convenio': 'Não',
        'retorno_info': 'Não especificado',
        'experiencia': 'Não especificado',
        'formacao': [],
        'video_url': '',
        'instagram': '',
        'facebook': '',
    },
]

# def lista_medicos(request):
#     context = {
#         'doctors': DOCTORS,
#         'resolution': '1920x1080',
#     }
#     return render(request, 'doctors/lista_medicos.html', context)

# def lista_medicos(request):
#     specialty_filter = request.GET.get('specialty')
#     sort_filter = request.GET.get('filter')
#     search_query = request.GET.get('q', '').strip().lower()

#     doctors_filtered = DOCTORS.copy()

#     # --- FILTRAR POR ESPECIALIDADE ---
#     if specialty_filter and specialty_filter.lower() != 'all':
#         doctors_filtered = [
#             d for d in doctors_filtered
#             if d['specialty'].strip().lower() == specialty_filter.strip().lower()
#         ]

#     # --- FILTRAR POR BUSCA DE TEXTO ---
#     if search_query:
#         doctors_filtered = [
#             d for d in doctors_filtered
#             if search_query in d['name'].lower()
#         ]

#     # --- TRANSFORMA VALOR PARA DECIMAL ---
#     for doctor in doctors_filtered:
#         try:
#             doctor['valor_num'] = Decimal(doctor['value'].replace('.', '').replace(',', '.'))
#         except:
#             doctor['valor_num'] = Decimal('0')

#     # --- ORDENAR ---
#     if sort_filter == 'lowest-price':
#         doctors_filtered.sort(key=lambda d: d['valor_num'])
#     elif sort_filter == 'highest-price':
#         doctors_filtered.sort(key=lambda d: d['valor_num'], reverse=True)
#     elif sort_filter == 'most-viewed':
#         doctors_filtered.sort(key=lambda d: d['views'], reverse=True)

#     context = {
#         'doctors': doctors_filtered,
#         'total_prescritores': len(doctors_filtered),
#         'resolution': '1920x1080',
#     }
#     return render(request, 'doctors/lista_medicos.html', context)


from django.shortcuts import render
from decimal import Decimal

def lista_medicos(request):
    specialty_filter = request.GET.get('specialty')
    sort_filter = request.GET.get('filter')
    search_query = request.GET.get('q', '').strip().lower()

    doctors_filtered = DOCTORS.copy()

    # --- FILTRAR POR ESPECIALIDADE ---
    if specialty_filter and specialty_filter.lower() != 'all':
        doctors_filtered = [
            d for d in doctors_filtered
            if d['specialty'].strip().lower() == specialty_filter.strip().lower()
        ]

    # --- FILTRAR POR BUSCA (nome do médico) ---
    if search_query:
        doctors_filtered = [
            d for d in doctors_filtered
            if search_query in d['name'].lower()
        ]

    # --- CONVERTER VALORES PARA DECIMAL (para ordenar corretamente) ---
    for doctor in doctors_filtered:
        try:
            doctor['valor_num'] = Decimal(doctor['value'].replace('.', '').replace(',', '.'))
        except:
            doctor['valor_num'] = Decimal('0')

    # --- ORDENAR ---
    if sort_filter == 'lowest-price':
        doctors_filtered.sort(key=lambda d: d['valor_num'])
    elif sort_filter == 'highest-price':
        doctors_filtered.sort(key=lambda d: d['valor_num'], reverse=True)
    elif sort_filter == 'most-viewed':
        doctors_filtered.sort(key=lambda d: d['views'], reverse=True)

    context = {
        'doctors': doctors_filtered,
        'total_prescritores': len(doctors_filtered),
        'resolution': '1920x1080',
    }
    return render(request, 'doctors/lista_medicos.html', context)





def perfil_medico(request, medico_id):
    doctor = next((d for d in DOCTORS if d['id'] == medico_id), None)
    if not doctor:
        return render(request, '404.html', status=404)

    context = {
        'doctor': doctor,
        'resolution': '1920x1080',
    }
    return render(request, 'doctors/perfil_medico.html', context)
