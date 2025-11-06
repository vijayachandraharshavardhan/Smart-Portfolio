# TODO: Fix Cloudinary Media Expiration Issue

## Approved Plan Steps
- [x] Update smart_portfolio_site/settings.py to set cloudinary.uploader.default_upload_options = {'type': 'upload'} after the config, ensuring all uploads use permanent public URLs.

## Followup Steps
- [ ] Test uploading new media in admin and verify the URL does not contain '/authenticated/' and persists beyond 1 hour.
- [ ] If existing media still expires, re-upload them to generate new permanent URLs.
