#!C:\Users\komro\PycharmProjects\course-api-testing\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytest==6.1.1','console_scripts','py.test'
__requires__ = 'pytest==6.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pytest==6.1.1', 'console_scripts', 'py.test')()
    )
