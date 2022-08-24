import os
import re
import clipboard as clip
import git as Git
import subprocess as sbp

import utils

URL_REPO = 'https://github.com/parasxos/quasar'

LOCAL_REPO = '/Users/jolyne/Desktop/Code/CERN/tmp'
SRC_REPO = '/Users/jolyne/Desktop/Code/CERN/quasar'

TARGET_VERSIONS_DIR = '/Users/jolyne/Desktop/Code/CERN/versions'

VERSION_REGEX = r'^v\d+\.\d+\.\d+$'

if os.path.exists(LOCAL_REPO):
  repo = Git.Repo(LOCAL_REPO)
else:
  repo = Git.Repo.clone_from(URL_REPO, LOCAL_REPO, branch='master')

for tag in repo.tags:
  if re.match(VERSION_REGEX, tag.name):
    print('Found tag: ' + tag.name)
    repo.git.checkout('tags/' + tag.name)

    os.system(f'cp -r {SRC_REPO}/Documentation {LOCAL_REPO}')
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

    os.system(f'mkdir -p {LOCAL_REPO}/Documentation/source/converted')
    repo.git.restore('.')
    print(f'Tag {tag.name} processed')


