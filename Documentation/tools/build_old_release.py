import re
import os
import shutil
import git as Git
import subprocess as sbp

URL_REPO = 'https://github.com/parasxos/quasar'

TEMP_FOLDER = '/tmp/sandbox'
LOCAL_REPO = f'{TEMP_FOLDER}/tmp_repo'
SRC_REPO = f'{TEMP_FOLDER}/src_repo'
TARGET_VERSIONS_DIR = f'{TEMP_FOLDER}/versions'

VERSION_REGEX = r'^v\d+\.\d+\.\d+$'

#os.makedirs(TEMP_FOLDER, exist_ok=True)
print(LOCAL_REPO, SRC_REPO)
if os.path.exists(LOCAL_REPO):
  print('Deleting previous local repo')
  shutil.rmtree(LOCAL_REPO)
if os.path.exists(SRC_REPO):
  print('Deleting previous src repo')
  shutil.rmtree(SRC_REPO)

os.makedirs(TEMP_FOLDER, exist_ok=True)
os.makedirs(TARGET_VERSIONS_DIR, exist_ok=True)

_ = Git.Repo.clone_from(URL_REPO, SRC_REPO, branch='master')
repo = Git.Repo.clone_from(URL_REPO, LOCAL_REPO, branch='master')

def copy_sphinx_files():
  os.system(f'cp -r {SRC_REPO}/Documentation/source {LOCAL_REPO}/Documentation')

  files = ['make.bat', 'Makefile', 'utils.py', 'html2rst.py', 'update_versions.py']
  for file in files:
    os.system(f'cp {SRC_REPO}/Documentation/{file} {LOCAL_REPO}/Documentation/{file}')

  os.system(f'cp {SRC_REPO}/Documentation/source/converted/quasar_OPC_UA_servers.rst {LOCAL_REPO}/Documentation/source/converted/quasar_OPC_UA_servers.rst')

for tag in repo.tags:
  if re.match(VERSION_REGEX, tag.name):
    print('Processing tag: ' + tag.name)
    repo.git.checkout('tags/' + tag.name)

    copy_sphinx_files()
    os.system(f'cp -r {LOCAL_REPO}/CalculatedVariables/doc/. {LOCAL_REPO}/Documentation')

    os.system(f'rm -rf {LOCAL_REPO}/Documentation/source/converted')
    os.system(f'mkdir -p {LOCAL_REPO}/Documentation/source/converted')

    os.system(f'cd {LOCAL_REPO} && python3 ./Documentation/html2rst.py && ls -l Documentation/source/converted')

    os.system(f'cd {LOCAL_REPO} && sphinx-build -b html ./Documentation/source ./Documentation/_build/{tag.name}')

    #make epub file
    os.system(f'cd {LOCAL_REPO}/Documentation && make epub && cp ./build/epub/Quasar.epub ./_build/{tag.name}/Quasar.epub')
    os.system(f'cd {LOCAL_REPO}/Documentation && mv ./_build/{tag.name}/Quasar.epub ./_build/{tag.name}/Quasar\ {tag.name}.epub')

    #make pdf file
    os.system(f'cd {LOCAL_REPO}/Documentation && make latexpdf && cp ./build/latex/quasar.pdf ./_build/{tag.name}/quasar.pdf')
    os.system(f'cd {LOCAL_REPO}/Documentation && mv ./_build/{tag.name}/quasar.pdf ./_build/{tag.name}/Quasar\ {tag.name}.pdf')

    os.system(f'cd {LOCAL_REPO} && cp -r ./Documentation/_build/{tag.name} {TARGET_VERSIONS_DIR}')

    os.system(f'rm -rf {LOCAL_REPO}/Documentation/source/converted')
    os.system(f'mkdir -p {LOCAL_REPO}/Documentation/source/converted')
    
    repo.git.clean('-f', '-q', './') 
    repo.git.restore('.')

    print(f'Tag {tag.name} processed')

print()
print(
  '=' * 120 + '\n' +
  'The old release was compiled successfully. In order to update it on the VM you must send all these release folder to the VM via scp.\n' +
  'Here you have a example of the commands to do that:\n' +
  f'scp -r {TARGET_VERSIONS_DIR} <your_username>@<hostname>:/tmp\n' + 
  'cp -r /tmp/versions/. /usr/share/nginx/version\n' +
  'cp -r /tmp/versions/. /eos/project-q/quasar/www/version' 
)
