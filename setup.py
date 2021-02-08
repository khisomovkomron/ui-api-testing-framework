from setuptools import setup, find_packages


setup(name='ui_api_testing_framework',
      version='1.0',
      description="Practice API testing",
      author="Komron Khisomov",
      author_email='komronkhisomov@gmail.com',
      url='http://threek-store.ru',
      packages=find_packages(), install_requires=[
                                                  'requests==2.24.0',
                                                  'pytest==6.1.1',
                                                  'woocommerce',
                                                  'pymysql',
                                                  'requests-oauthlib',
                                                  'pytest-html',
                                                  'html-testRunner==1.2.1',
                                                  ]
      )