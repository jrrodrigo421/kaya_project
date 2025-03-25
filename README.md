# Projeto Kaya Doc

## 📋 Descrição do Projeto
Projeto de replicação das páginas de médicos do Kaya Doc utilizando Django e Tailwind CSS.

## 🚀 Funcionalidades
- Listagem de médicos em página desktop
- Página de perfil público de médicos
- Design próximo ao layout original do Kaya Doc

## 📦 Tecnologias Utilizadas
- Django 5.0.1
- Tailwind CSS
- Python
- HTML
- JavaScript

## 🔧 Requisitos
- Python 3.8+
- pip
- virtualenv (opcional, mas recomendado)

## 🛠️ Instalação Passo a Passo

### 1. Clonar o Repositório
```bash
git clone https://github.com/jrrodrigo421/kaya-doc-teste.git
cd kaya-doc-teste
```

### 2. Criar Ambiente Virtual (Opcional mas Recomendado)
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar Migrações
```bash
python manage.py migrate
```

### 5. Iniciar Servidor Local
```bash
python manage.py runserver
```

## 🌐 Acesso
Abra seu navegador e acesse:
- Listagem de Médicos: `http://localhost:8000/medicos/`
- Perfil de Médico: `http://localhost:8000/medicos/10/perfil/`

## 📱 Resolução
Projeto desenvolvido para resolução desktop & Mobile

## 📧 Contato
```bash
Rodrigo Lopes - rodrigoplopesjr@gmail.com
```