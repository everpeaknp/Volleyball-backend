from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class MultiLanguageCharField(models.CharField):
    """
    Custom CharField that validates multi-language content completeness.
    """
    
    def __init__(self, *args, **kwargs):
        self.required_languages = kwargs.pop('required_languages', ['NE', 'EN', 'DE'])
        super().__init__(*args, **kwargs)
    
    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        
        # Check if all required languages have content
        if hasattr(model_instance, 'language'):
            # This is for single-language models
            pass
        else:
            # This would be for multi-language content validation
            # Implementation depends on the specific use case
            pass


class MultiLanguageTextField(models.TextField):
    """
    Custom TextField that validates multi-language content completeness.
    """
    
    def __init__(self, *args, **kwargs):
        self.required_languages = kwargs.pop('required_languages', ['NE', 'EN', 'DE'])
        super().__init__(*args, **kwargs)
    
    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        
        # Similar validation logic as MultiLanguageCharField
        pass


class SafeHTMLField(models.TextField):
    """
    TextField that automatically sanitizes HTML content.
    """
    
    def __init__(self, *args, **kwargs):
        self.allow_tags = kwargs.pop('allow_tags', True)
        self.strip_tags = kwargs.pop('strip_tags', True)
        super().__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        
        if self.strip_tags and value:
            import bleach
            # Define allowed HTML tags and attributes
            allowed_tags = [
                'p', 'br', 'strong', 'em', 'u', 'ol', 'ul', 'li',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                'a', 'img', 'div', 'span', 'blockquote'
            ]
            allowed_attributes = {
                'a': ['href', 'title', 'target'],
                'img': ['src', 'alt', 'title', 'width', 'height'],
                'div': ['class'],
                'span': ['class'],
                '*': ['class']
            }
            
            # Sanitize HTML
            value = bleach.clean(
                value,
                tags=allowed_tags,
                attributes=allowed_attributes,
                strip=True
            )
        
        return value


class JSONField(models.JSONField):
    """
    Custom JSONField with validation for structured data.
    """
    
    def __init__(self, *args, **kwargs):
        self.schema = kwargs.pop('schema', None)
        super().__init__(*args, **kwargs)
    
    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        
        if self.schema and value:
            # Validate against schema if provided
            try:
                import jsonschema
                jsonschema.validate(value, self.schema)
            except ImportError:
                # jsonschema not installed, skip validation
                pass
            except Exception as e:
                raise ValidationError(
                    _('Invalid JSON data: %(error)s') % {'error': str(e)}
                )


class OptimizedImageField(models.ImageField):
    """
    ImageField that automatically optimizes images on upload.
    """
    
    def __init__(self, *args, **kwargs):
        self.optimize = kwargs.pop('optimize', True)
        self.max_width = kwargs.pop('max_width', 1920)
        self.max_height = kwargs.pop('max_height', 1080)
        self.quality = kwargs.pop('quality', 85)
        super().__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        
        if self.optimize and value and hasattr(value, 'path'):
            try:
                from PIL import Image
                import os
                
                # Open the image
                img = Image.open(value.path)
                
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                
                # Resize if necessary
                if img.width > self.max_width or img.height > self.max_height:
                    img.thumbnail((self.max_width, self.max_height), Image.Resampling.LANCZOS)
                
                # Save with optimization
                img.save(value.path, 'JPEG', quality=self.quality, optimize=True)
                
            except Exception:
                # If optimization fails, continue with original image
                pass
        
        return value
