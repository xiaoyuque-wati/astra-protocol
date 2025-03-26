from setuptools import setup, find_packages
from datetime import datetime

def version():
    return datetime.now().strftime('%Y.%m.dev%H%m')


setup(
    name='python_ai_platform_api',
    version=version(),
    packages=['python_ai_platform_api'],
    package_dir={'python_ai_platform_api': 'all-languages-api/python'},
    install_requires=[
        'protobuf',
    ],
    package_data={
        'python_ai_platform_api': ['*.py', '*.pyi'],
    },
    include_package_data=True,
    description='Python protocol for AI Platform API',
)