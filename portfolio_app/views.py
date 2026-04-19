from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact, Project, Skill
from .forms import ContactForm


def home(request):
    projects = [
        {
            'title': 'Student Management System',
            'description': 'A full-stack web application to manage student records, attendance, and grades using Django backend with a responsive Bootstrap frontend.',
            'tech': 'Python, Django, Bootstrap, SQLite',
            'category': 'python',
            'github': 'https://github.com/nitikaswami',
            'image' : 'img/student.png'
        },
        {
            'title': 'E-Commerce Landing Page',
            'description': 'A fully responsive e-commerce product showcase with cart functionality, built with pure HTML, CSS, Bootstrap and JavaScript.',
            'tech': 'HTML, CSS, Bootstrap, JavaScript',
            'category': 'frontend',
            'github': 'https://github.com/nitikaswami',
            'image' : 'img/e-commerce.png'
        },
        {
            'title': 'Personal Blog Platform',
            'description': 'A dynamic blog platform with user authentication, CRUD operations for posts, comments system, and admin dashboard using Django.',
            'tech': 'Python, Django, HTML, CSS, JavaScript',
            'category': 'python',
            'github': 'https://github.com/nitikaswami',
            'icon': '✍️'
        },
        {
            'title': 'Weather Dashboard',
            'description': 'An interactive weather app fetching real-time data from OpenWeatherMap API, with animated weather icons and 5-day forecast.',
            'tech': 'JavaScript, HTML5, CSS3, REST API',
            'category': 'frontend',
            'github': 'https://github.com/nitikaswami',
            'image' : 'img/weather.png'
        },
        {
            'title': 'Task Manager App',
            'description': 'A productivity app with user login, task creation, priority levels, deadlines, and progress tracking built with Django REST + JS frontend.',
            'tech': 'Django, JavaScript, Bootstrap, SQLite',
            'category': 'python',
            'github': 'https://github.com/nitikaswami',
            'icon': '✅'
        },
        {
            'title': 'Portfolio Website',
            'description': 'This very portfolio — a full-stack Django-powered website with contact form backend, smooth animations, and fully responsive design.',
            'tech': 'Django, HTML, CSS, Bootstrap, JS',
            'category': 'web',
            'github': 'https://github.com/nitikaswami',
            'image' : 'img/portfolio.png'
        },
    ]

    skills = {
        'frontend': [
            {'name': 'HTML5', 'percent': 90, 'icon': 'html5'},
            {'name': 'CSS3', 'percent': 85, 'icon': 'css3'},
            {'name': 'Bootstrap', 'percent': 88, 'icon': 'bootstrap'},
            {'name': 'JavaScript', 'percent': 75, 'icon': 'javascript'},
        ],
        'backend': [
            {'name': 'Python', 'percent': 82, 'icon': 'python'},
            {'name': 'Django', 'percent': 78, 'icon': 'django'},
            {'name': 'SQL / SQLite', 'percent': 70, 'icon': 'database'},
        ],
        'tools': [
            {'name': 'VS Code', 'percent': 92, 'icon': 'vscode'},
            {'name': 'Git', 'percent': 80, 'icon': 'git'},
            {'name': 'GitHub', 'percent': 82, 'icon': 'github'},
        ]
    }

    form = ContactForm()
    context = {
        'projects': projects,
        'skills': skills,
        'form': form,
    }
    return render(request, 'index.html', context)


@require_POST
def contact_submit(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contact = form.save()
        return JsonResponse({
            'success': True,
            'message': 'Thank you! Your message has been received. I will get back to you soon.'
        })
    else:
        errors = {field: error[0] for field, error in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors}, status=400)


def about(request):
    return render(request, 'index.html')
