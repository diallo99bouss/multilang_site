import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

# Définir ROOT_URLCONF
ROOT_URLCONF = 'multilang_site.urls'

# Configuration des langues
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    # Ajoutez d'autres langues si nécessaire
]

# Chemin des fichiers de traduction
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Code de langue par défaut
LANGUAGE_CODE = 'en'

# Activer les fonctionnalités i18n et l10n
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Ajoutez ce middleware pour les langues
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Ajoutez d'autres applications ici si nécessaire
]

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # Ajoutez ce context processor pour i18n
            ],
        },
    },
]

# Configuration des fichiers statiques
STATIC_URL = '/static/'

# Répertoires des fichiers statiques
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Configuration de la base de données (à adapter selon vos besoins)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Autres configurations Django

# Définir DEBUG
DEBUG = False

# Définir ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']
