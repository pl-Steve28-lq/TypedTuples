import setuptools, json

with open('README.md', 'r', encoding='utf-8') as fh:
  long_description = fh.read()

with open('project.json', 'r', encoding='utf-8') as f:
  info = json.loads(f.readline())
  ver = info['version']
  desc = info['desc']

with open('project.json', 'w', encoding='utf-8') as f:
  newver = ver.split('.')
  last = newver[2]
  newver[2] = str(int(last)+1)
  info['version'] = '.'.join(newver)
  f.write(json.dumps(info))
  ver = info['version']

setuptools.setup(
  name='Typedtuples',
  version=ver,
  author='Steve28',
  author_email='holiday28784@gmail.com',
  description=desc,
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/pl-Steve28-lq/TypedTuples',
  packages=setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
)
