import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '3xk*)i0x#k$btl=(6q)te!19=mp6d)lm1+zl#ts4ewxi3-!vm_'

DEBUG = True

ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'basket',
    'account',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Basket session ID
BASKET_SESSION_ID = 'basket'

# Stripe Payment
PUBLISHABLE_KEY = 'pk_test_51M7cRnBIBlYWlII2eg1XAVXfi6cNlEmtAO4hGIAk2Ydk45LBpbvpACa4WhwaTZTyX8Qnd247aRtUoP7VORQ3d3yM00jpoXElYv'
SECRET_KEY = 'sk_test_51M7cRnBIBlYWlII24t3jIL3kxnUfx1v4gX8tHAFZs1MH0Sz97mls2Ou45nQ29qBoRS16FtsUVOXsFyqU3VDdKFzY00GY530Lw2'
# STRIPE_ENDPOINT_SECRET = ''
# stripe listen --forward-to localhost:8000/payment/webhook/
STRIPE_PUBLIC_KEY = 'pk_test_51M7cRnBIBlYWlII2eg1XAVXfi6cNlEmtAO4hGIAk2Ydk45LBpbvpACa4WhwaTZTyX8Qnd247aRtUoP7VORQ3d3yM00jpoXElYv'
STRIPE_SECRET_KEY = 'sk_test_51M7cRnBIBlYWlII24t3jIL3kxnUfx1v4gX8tHAFZs1MH0Sz97mls2Ou45nQ29qBoRS16FtsUVOXsFyqU3VDdKFzY00GY530Lw2'


# USE - custom user model. Instead of default.
AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

# Email setting
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# settings for email sending form:
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'stibo84@mail.ru'
EMAIL_HOST_PASSWORD = '00KrtGcLNpmfM0wqTmxr'

sender_mail = 'stibo84@mail.ru'
receiver_mail = 'id764g@gmail.com'

