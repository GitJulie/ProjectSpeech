#!"C:\Users\julie\Documents\ESME\4ème_année\Projet 5 - Text 2 Speech\TTS\ProjectSpeech\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'activation==0.1.0','console_scripts','activation'
__requires__ = 'activation==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('activation==0.1.0', 'console_scripts', 'activation')()
    )
