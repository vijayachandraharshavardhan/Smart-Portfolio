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

print("Checking existing Cloudinary media URLs for expiration...")

# Check last project
project = Project.objects.last()
if project:
    if project.image:
        url = project.image.url
        print(f"Project image URL: {url}")
        if 'authenticated' in url:
            print("❌ ERROR: Project image URL is authenticated (expiring)")
        else:
            print("✅ OK: Project image URL is permanent")
    if project.video:
        url = project.video.url
        print(f"Project video URL: {url}")
        if 'authenticated' in url:
            print("❌ ERROR: Project video URL is authenticated (expiring)")
        else:
            print("✅ OK: Project video URL is permanent")
else:
    print("No projects found.")

# Check profile
profile = Profile.objects.last()
if profile and profile.profile_image:
    url = profile.profile_image.url
    print(f"Profile image URL: {url}")
    if 'authenticated' in url:
        print("❌ ERROR: Profile image URL is authenticated (expiring)")
    else:
        print("✅ OK: Profile image URL is permanent")
else:
    print("No profile image found.")

# Check intro video
intro = IntroVideo.objects.last()
if intro and intro.video_file:
    url = intro.video_file.url
    print(f"Intro video URL: {url}")
    if 'authenticated' in url:
        print("❌ ERROR: Intro video URL is authenticated (expiring)")
    else:
        print("✅ OK: Intro video URL is permanent")
else:
    print("No intro video found.")

print("\nNote: For new uploads after the settings change, URLs will be permanent.")
print("If any existing URLs are expiring, re-upload the media in admin to generate new permanent URLs.")
