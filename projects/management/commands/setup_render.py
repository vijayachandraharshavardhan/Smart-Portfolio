from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Setup database for Render deployment'

    def handle(self, *args, **options):
        self.stdout.write('Setting up database for Render...')

        # Run migrations
        call_command('migrate', verbosity=1)

        # Load data
        try:
            call_command('loaddata', 'render_data_clean.json', verbosity=1)
            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Could not load data: {e}'))

        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin123'))
        else:
            self.stdout.write('Superuser already exists')

        self.stdout.write(self.style.SUCCESS('Setup complete!'))
