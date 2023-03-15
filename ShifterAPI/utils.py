import os

def setConfig():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShifterAPI.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')
