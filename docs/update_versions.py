import os
import sys
import json

PASS_USER = os.environ.get('PASS_USER')

JSON_FILE = './docs/source/_static/versions.json'
JSON_FILE_LOCAL = '/home/fmagalla/quasar/versions.json'

VERSIONS_FOLDER = '/usr/share/nginx/quasar/version'
EOS_VERSIONS_FOLDER = '/eos/project-q/quasar/www/version'

cp_local_command = f'cp {JSON_FILE} {JSON_FILE_LOCAL}'
print(cp_local_command)
os.system(cp_local_command)

if __name__ == '__main__':
  for folder_version in os.listdir(VERSIONS_FOLDER):
    print('Processing version: ', folder_version)

    cp_nginx_command = f'echo {PASS_USER} | sudo -S cp {JSON_FILE_LOCAL} {VERSIONS_FOLDER}/{folder_version}/_static/versions.json'
    os.system(cp_nginx_command)
    
    cp_eos_command = f'cp {JSON_FILE_LOCAL} {EOS_VERSIONS_FOLDER}/{folder_version}/_static/versions.json'
    os.system(cp_eos_command)

  exit(0)
