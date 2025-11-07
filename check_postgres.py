import os
import django
from dotenv import load_dotenv

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_portfolio_site.settings')
django.setup()

from projects.models import Project, Profile, IntroVideo

print("=== PostgreSQL Data Check ===")
print(f"Projects: {Project.objects.count()}")
print(f"Profiles: {Profile.objects.count()}")
print(f"Intro Videos: {IntroVideo.objects.count()}")
print("")

print("Sample Projects:")
for p in Project.objects.all()[:5]:
    print(f"- {p.title} (ID: {p.id})")
    print(f"  Image: {bool(p.image)} ({p.image})")
    print(f"  Video: {bool(p.video)} ({p.video})")
    print("")

print("Sample Profiles:")
for prof in Profile.objects.all()[:2]:
    print(f"- {prof.name} (ID: {prof.id})")
    print(f"  Profile Image: {bool(prof.profile_image)} ({prof.profile_image})")
    print("")

print("Sample Intro Videos:")
for iv in IntroVideo.objects.all()[:2]:
    print(f"- {iv.title} (ID: {iv.id})")
    print(f"  Video File: {bool(iv.video_file)} ({iv.video_file})")
    print("")
