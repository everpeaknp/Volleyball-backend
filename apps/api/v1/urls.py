from django.urls import path, include

urlpatterns = [
    # Page Content (e.g., /api/v1/content/home/)
    path('content/', include('apps.pages.urls')),
    
    # Reusable Data/Resources (e.g., /api/v1/data/events/)
    # Using 'data' prefix to avoid collision with 'content' pages
    path('data/', include('apps.content.urls')),
    
    # Navigation (e.g., /api/v1/navigation/)
    path('navigation/', include('apps.navigation.urls')),
    
    # Media (e.g., /api/v1/media/)
    path('media/', include('apps.media.urls')),

    # Core/Global Styles (e.g., /api/v1/core/)
    path('core/', include('apps.core.urls')),
    
    # Membership Applications (e.g., /api/v1/membership/)
    path('membership/', include('apps.membership_options.urls')),
    
    # Contact Submissions (e.g., /api/v1/contact/)
    path('contact/', include('apps.contact_options.urls')),
]
