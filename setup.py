from setuptools import setup

setup(
    name='fisher-catcher',
    version='0.0.1',
    author='Evgeny Prokopets',
    author_email='prokopetz.e@gmail.com',
    description='Fisher Catcher API APP',
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'request==2.26.0'
    ],
    scripts=[]
)
