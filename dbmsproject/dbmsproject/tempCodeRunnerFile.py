STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static") # this is your static folder
]

STATIC_ROOT = os.path.join(BASE_DIR,'assets') #this is you assets folder.

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'