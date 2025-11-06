from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Profile
import cloudinary

def landing(request):
    profile = Profile.objects.order_by('-updated_at').first()
    if not profile:
        profile = Profile.objects.create()
    return render(request, 'projects/landing.html', {'profile': profile})

def project_list(request):
    profile = Profile.objects.order_by('-updated_at').first()
    if not profile:
        profile = Profile.objects.create()
    projects = Project.objects.all().order_by('position', '-created_at')
    # Get unique tech stacks for filtering
    tech_stacks = set()
    for project in projects:
        if project.tech_stack:
            stacks = [stack.strip() for stack in project.tech_stack.split(',')]
            tech_stacks.update(stacks)
            # Add tech_stack_list to each project for template use
            project.tech_stack_list = stacks
        else:
            project.tech_stack_list = []
    tech_stacks = sorted(list(tech_stacks))

    context = {
        'profile': profile,
        'projects': projects,
        'tech_stacks': tech_stacks,
        'total_projects': projects.count(),
    }
    return render(request, 'projects/projects.html', context)

def about(request):
    profile = Profile.objects.order_by('-updated_at').first()
    if not profile:
        profile = Profile.objects.create()
    return render(request, 'projects/about.html', {'profile': profile})

def check_cloudinary(request):
    try:
        # Get your Cloudinary config
        config = cloudinary.config()
        return JsonResponse({
            "cloud_name": config.cloud_name,
            "api_key": config.api_key[:4] + "*****",  # partially hidden
            "secure": config.secure,
            "status": "✅ Connected successfully to Cloudinary"
        })
    except Exception as e:
        return JsonResponse({
            "status": "❌ Connection failed",
            "error": str(e)
        })
