from reservetion_project.settings.base import * 

DEBUG = False

ALLOWED_HOSTS = ['reservetionproject.herokuapp.com']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')