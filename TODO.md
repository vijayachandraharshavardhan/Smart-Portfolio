# TODO: Fix Media Files Loading on Other Devices

## Approved Plan Steps
- [x] Update requirements.txt to include django-cloudinary-storage
- [x] Add Cloudinary integration to settings.py
- [x] Update Profile and Project models in models.py to use CloudinaryField for images/videos
- [x] Fix landing.html to use profile.profile_image instead of hero_media loop

## Followup Steps
- [x] Run pip install django-cloudinary-storage locally
- [x] Run migrations after model changes
- [x] Test media upload in admin and display on site
- [ ] Deploy to Render

## Important Notes
- Cloudinary credentials have been added to render.yaml
- For local development, add these to your .env file:
  CLOUDINARY_CLOUD_NAME=dnglmw8l0
  CLOUDINARY_API_KEY=986362225853921
  CLOUDINARY_API_SECRET=nZREC-59laRxF120SXrm91XIUmE
- Existing media files will need to be re-uploaded to Cloudinary
- Server is running at http://127.0.0.1:8000/ - you can test media upload in admin
