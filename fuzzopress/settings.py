# -*- coding: utf-8 -*-
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Javi Manzano', 'javi.manzano.oller@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    # 'postgres': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'fuzzopress',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Madrid'
USE_TZ = True
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = '/home/ubuntu/media/'
MEDIA_URL = '/static/media/'
STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})

SECRET_KEY = '%3maeu=guk3p#67j-2--drhy$*^vx+=l9r9bltk-n-^cw4#nic'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'fuzzopress.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/ubuntu/django_apps/fuzzopress/fuzzopress/blog/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'fuzzopress.blog',
    'django.contrib.markup',
    'markitup',
    'gunicorn',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MARKITUP_SET = 'markitup/sets/markdown'

# Settings for main blog app
FUZZOPRESS_SETTINGS = {
    'contact': [
        {
            'name': 'github',
            'icon': 'icon-github-alt',
            'url': 'https://github.com/jgasteiz',
            'show': True,
        },
        {
            'name': 'twitter',
            'icon': 'icon-twitter',
            'url': 'https://twitter.com/jgasteiz',
            'show': True,
        },
        {
            'name': 'googleplus',
            'icon': 'icon-google-plus-sign',
            'url': 'https://plus.google.com/u/0/104971241169939266087/posts',
            'show': True,
        },
        {
            'name': 'email',
            'icon': 'icon-envelope-alt',
            'url': 'mailto:javi.manzano.oller@gmail.com',
            'show': True,
        }
    ],
    'analytics': {
        'show': True,
        'code': 'UA-23612418-1'
    },
    'tags': {
        'show': True
    },
    'archive': {
        'show': True
    },
    'finder': {
        'show': True
    },
    'colors': ['#D65C3C', '#FFC000', '#40C080', '#2E6EB0', '#770999', '#E6006C', '#04B1D8'],
    'entries_per_page': 5
}
