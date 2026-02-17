from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_phone_number(value):
    """
    Validate phone number format.
    Supports international formats.
    """
    # Remove all non-digit characters
    phone_digits = re.sub(r'[^\d+]', '', value)
    
    # Check if it starts with + (international) or has valid length
    if not (phone_digits.startswith('+') or len(phone_digits) >= 10):
        raise ValidationError(
            _('Enter a valid phone number. Include country code if international.')
        )
    
    # Check minimum length (excluding +)
    if len(phone_digits.replace('+', '')) < 10:
        raise ValidationError(
            _('Phone number must be at least 10 digits long.')
        )


def validate_url_scheme(value):
    """
    Validate URL has proper scheme (http/https).
    """
    if not value.startswith(('http://', 'https://')):
        raise ValidationError(
            _('URL must start with http:// or https://')
        )


def validate_json_structure(value):
    """
    Validate JSON structure for specific content types.
    """
    if not isinstance(value, dict):
        raise ValidationError(_('Value must be a JSON object.'))
    
    # Add specific validation based on expected structure
    # This can be extended based on requirements


def validate_alt_text_completeness(model_instance):
    """
    Validate that alt text is provided in all languages for images.
    """
    if hasattr(model_instance, 'alt_text_ne') and hasattr(model_instance, 'alt_text_en') and hasattr(model_instance, 'alt_text_de'):
        if not (model_instance.alt_text_ne and model_instance.alt_text_en and model_instance.alt_text_de):
            raise ValidationError(
                _('Alt text must be provided in all languages (Nepali, English, German).')
            )


def validate_language_completeness(model_instance):
    """
    Validate that all required fields are filled for the current language.
    """
    required_fields = getattr(model_instance, 'REQUIRED_FIELDS', [])
    missing_fields = []
    
    for field_name in required_fields:
        field_value = getattr(model_instance, field_name, None)
        if not field_value or (isinstance(field_value, str) and not field_value.strip()):
            missing_fields.append(field_name)
    
    if missing_fields:
        field_names = ', '.join(missing_fields)
        raise ValidationError(
            _('The following required fields are missing or empty: %(fields)s') % 
            {'fields': field_names}
        )


def validate_publishable_content(model_instance):
    """
    Validate that content can be published (all required fields filled).
    """
    if model_instance.status == 'published':
        # Check language completeness
        validate_language_completeness(model_instance)
        
        # Check if all required translations exist
        if hasattr(model_instance, 'get_translations'):
            translations = model_instance.get_translations()
            required_languages = ['NE', 'EN', 'DE']
            
            for lang in required_languages:
                if lang not in translations:
                    raise ValidationError(
                        _('Cannot publish: %(language)s translation is missing.') % 
                        {'language': dict(model_instance.LANGUAGE_CHOICES).get(lang, lang)}
                    )


def validate_file_size(value):
    """
    Validate file size doesn't exceed maximum allowed.
    """
    max_size = 5 * 1024 * 1024  # 5MB
    
    if value.size > max_size:
        raise ValidationError(
            _('File size cannot exceed 5MB. Current size: %(size)s MB.') % 
            {'size': round(value.size / (1024 * 1024), 2)}
        )


def validate_image_dimensions(value):
    """
    Validate image dimensions are within acceptable limits.
    """
    from PIL import Image
    import io
    
    try:
        # Reset file pointer
        value.seek(0)
        
        # Open image to check dimensions
        image = Image.open(io.BytesIO(value.read()))
        width, height = image.size
        
        max_width = 4000
        max_height = 4000
        
        if width > max_width or height > max_height:
            raise ValidationError(
                _('Image dimensions cannot exceed %(max_width)x%(max_height) pixels. '
                  'Current size: %(width)x%(height)s.') % 
                {
                    'max_width': max_width,
                    'max_height': max_height,
                    'width': width,
                    'height': height
                }
            )
        
        # Reset file pointer for Django to process
        value.seek(0)
        
    except Exception as e:
        if isinstance(e, ValidationError):
            raise
        # If we can't process the image, let Django handle it
        pass


def validate_video_format(value):
    """
    Validate video file format.
    """
    allowed_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm']
    file_extension = value.name.lower().split('.')[-1]
    
    if f'.{file_extension}' not in allowed_extensions:
        raise ValidationError(
            _('Video format not supported. Allowed formats: %(formats)s') % 
            {'formats': ', '.join(allowed_extensions)}
        )


def validate_slug_uniqueness(model_instance, slug_field='slug'):
    """
    Validate that slug is unique within its language.
    """
    slug = getattr(model_instance, slug_field)
    language = getattr(model_instance, 'language', 'NE')
    
    # Check for existing slug with same language
    queryset = model_instance.__class__.objects.filter(
        **{slug_field: slug, 'language': language}
    )
    
    # Exclude current instance if it's an update
    if model_instance.pk:
        queryset = queryset.exclude(pk=model_instance.pk)
    
    if queryset.exists():
        raise ValidationError(
            _('Slug "%(slug)s" already exists for %(language)s language.') % 
            {'slug': slug, 'language': dict(model_instance.LANGUAGE_CHOICES).get(language, language)}
        )
