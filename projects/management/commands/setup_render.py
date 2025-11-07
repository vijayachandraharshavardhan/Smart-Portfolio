from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command
from projects.models import Project, Profile, IntroVideo

class Command(BaseCommand):
    help = 'Setup database for Render deployment'

    def handle(self, *args, **options):
        self.stdout.write('Setting up database for Render...')

        # Run migrations
        call_command('migrate', verbosity=1)

        # Collect static files
        self.stdout.write('Collecting static files...')
        call_command('collectstatic', '--noinput', verbosity=0)

        # Create superuser (always recreate to ensure clean state)
        self.stdout.write('Creating superuser...')
        User.objects.filter(username='admin').delete()  # Remove any existing
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin123'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Project.objects.all().delete()
        Profile.objects.all().delete()
        IntroVideo.objects.all().delete()

        self.stdout.write('Data cleared. Ready for fresh content via admin panel.')

        self.stdout.write(self.style.SUCCESS('Setup complete!'))
