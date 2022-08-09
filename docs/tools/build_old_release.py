import os
import re
import clipboard as clip
import git as Git
import subprocess as sbp

import utils

URL_REPO = 'https://github.com/parasxos/quasar'

LOCAL_REPO = '/Users/jolyne/Desktop/Code/CERN/tmp'
SRC_REPO = '/Users/jolyne/Desktop/Code/CERN/quasar'

TARGET_VERSIONS_DIR = '/Users/jolyne/Desktop/Code/CERN/tmp/versions'

VERSION_REGEX = r'^v\d+\.\d+\.\d+$'

if os.path.exists(LOCAL_REPO):
  repo = Git.Repo(LOCAL_REPO)
else:
  repo = Git.Repo.clone_from(URL_REPO, LOCAL_REPO, branch='master')

for tag in repo.tags:
  if re.match(VERSION_REGEX, tag.name):
    print('Found tag: ' + tag.name)
    repo.git.checkout('tags/' + tag.name)

    os.system(f'cp -r {SRC_REPO}/docs {LOCAL_REPO}')

    os.system(f'rm -rf {LOCAL_REPO}/docs/source/converted')
    os.system(f'mkdir -p {LOCAL_REPO}/docs/source/converted')

    os.system(f'cd {LOCAL_REPO} && python3 ./docs/html2rst.py && ls -l docs/source/converted')

    cmd = f'cd {LOCAL_REPO} && sphinx-build -b html ./docs/source ./docs/_build/{tag.name}'
    #clip.copy(cmd)
    print('The following command was copied to the clipboard, please execute it:', cmd)

    os.system(f'cd {LOCAL_REPO} && sphinx-build -b html ./docs/source ./docs/_build/{tag.name}')
    #response = input('Press enter to continue any key to continue, "x" to exit: ')
    #if response.lower() == 'x':
    #  break

    os.system(f'cd {LOCAL_REPO} && cp -r ./docs/_build/{tag.name} {TARGET_VERSIONS_DIR}')

    repo.git.restore('.')
    print(f'Tag {tag.name} processed')
    break
