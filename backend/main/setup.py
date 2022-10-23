from setuptools import find_packages, setup


setup(
    name='main',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'python-dotenv',
        'dependency_injector',
        'text_ocr'
    ]
)
