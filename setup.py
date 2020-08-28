from setuptools import setup

setup(
    name='GrindrWebAccess',
    version='0.0.1',
    description='A framework for using the github v4 api in python',
    url='git@github.com:slenderman00/Pip-Grindr-Web-Access.git',
    author='Joar Heimonen',
    author_email='joarheimonen@live.no',
    license='mit',
    packages=['GrindrWebAccess'],
    zip_safe=False
    install_requires=[
        'requests==2.23.0',
        'asyncio==3.4.3',
        'pyqrcode==1.2.1',
        'websocket_client==0.57.0',
        'xmltodict==0.12.0',
        'pygeohash==1.2.0'
    ]
)