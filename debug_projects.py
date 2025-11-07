import os
import django
from dotenv import load_dotenv

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_portfolio_site.settings')
django.setup()

from projects.models import Project

print("Debugging projects and media...")

projects = Project.objects.all()
print(f"Total projects: {projects.count()}")

for p in projects:
    print(f"\nProject: {p.title}")
    print(f"  Image field: {repr(p.image)}")
    print(f"  Image bool: {bool(p.image)}")
    print(f"  Image public_id: {getattr(p.image, 'public_id', 'N/A')}")
    print(f"  Image format: {getattr(p.image, 'format', 'N/A')}")
    print(f"  Image url: {getattr(p.image, 'url', 'N/A')}")
    print(f"  Video field: {repr(p.video)}")
    print(f"  Video bool: {bool(p.video)}")
    print(f"  Video public_id: {getattr(p.video, 'public_id', 'N/A')}")
    print(f"  Video format: {getattr(p.video, 'format', 'N/A')}")
    print(f"  Video url: {getattr(p.video, 'url', 'N/A')}")

# Check for 'school' project
school_project = Project.objects.filter(title__icontains='school').first()
if school_project:
    print(f"\nFound 'school' project: {school_project.title}")
else:
    print("\nNo 'school' project found.")
