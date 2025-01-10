import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image

def validate_apk(file):
    file_name, file_extension = os.path.splitext(file.name)
    if file_extension.lower() != '.apk':
        raise ValidationError(_('File must be an APK (.apk) file.'))
    if file.size > 150 * 1024 * 1024:  # 150 MB
        raise ValidationError(_('File size must be less than 150 MB.'))

def validate_icon(file):
    file_name, file_extension = os.path.splitext(file.name)
    if file_extension.lower() != '.png':
        raise ValidationError(_('File must be a PNG (.png) file.'))
    
    image = Image.open(file)
    if image.width != 512 or image.height != 512:
        raise ValidationError(_('Icon dimensions must be 512x512 pixels.'))
    
    if file.size > 1 * 1024 * 1024:  # 1 MB
        raise ValidationError(_('File size must be less than 1 MB.'))
    
    if image.mode != 'RGBA' and image.mode != 'RGB':
        raise ValidationError(_('Icon must have a transparent background (use RGBA or RGB).'))
    
    if image.width != image.height:
        raise ValidationError(_('Icon must be a square image.'))

def validate_cover_graphics(file):
    file_name, file_extension = os.path.splitext(file.name)
    if file_extension.lower() not in ['.png', '.jpg']:
        raise ValidationError(_('File must be a PNG or JPG file.'))
    
    image = Image.open(file)
    if image.width != 1024 or image.height != 500:
        raise ValidationError(_('Cover graphics must be 1024x500 pixels.'))
    
    if file.size > 1.5 * 1024 * 1024:  # 1.5 MB
        raise ValidationError(_('File size must be less than 1.5 MB.'))
    

def validate_screenshot(file):
    file_name, file_extension = os.path.splitext(file.name)
    if file_extension.lower() not in ['.png', '.jpg']:
        raise ValidationError(_('Screenshot must be a PNG or JPG file.'))

    image = Image.open(file)
    if not (image.width == 1080 and image.height == 1920) and not (image.width == 1920 and image.height == 1080):
        raise ValidationError(_('Screenshot must be 1080x1920 or 1920x1080 pixels.'))

    if file.size > 2 * 1024 * 1024:
        raise ValidationError(_('File size must be less than 2 MB.'))

