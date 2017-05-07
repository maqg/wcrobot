#!/usr/bin/python

import sys

import os.path as op

RAM_HOME = "/oct/"
PRODUCT_HOME = "/OCT/"
PROJECT_HOME = "/OCT/OCTFrame/"
DB_PATH = PROJECT_HOME + "db/"

sys.path.append(PROJECT_HOME + "lib")

ADMINS = (
)


def _getAbsPath(relPath):
	selfDir = op.dirname(__file__)
	return selfDir + op.sep + op.normpath(relPath)


MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'octframe',
		'USER': 'root',
		'PASSWORD': '123456',
		'HOST': '',
		'PORT': '',
	},
}

TIME_ZONE = 'Asia/Shanghai'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_URL = 'media/'
STATIC_PATH = 'media'
PAGES_PATH = _getAbsPath("media/")
UI_PATH = _getAbsPath("media/ui")
TEMPLATES_PATH = _getAbsPath("templates/")
RESOURCES_PATH = _getAbsPath("media/Resources")
SECRET_KEY = 'tyd^!eo(tbfmzx#*@^&^a-jojqt+t*4apm%%d7*07-!cpg5^lr'

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	TEMPLATES_PATH,
)

FILE_UPLOAD_HANDLERS = (
	"django.core.files.uploadhandler.MemoryFileUploadHandler",
	"django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
)

LANGUAGE_COOKIE_NAME = 'django_language'
SESSION_COOKIE_NAME = 'sessionid'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = False
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_AGE = 60 * 10

FORCE_SCRIPT_NAME = ""
