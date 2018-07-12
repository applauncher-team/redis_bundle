from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='redis_bundle',
    packages=['redis_bundle'],
    version='0.2',
    description='Redis support for applauncher',
    author='Alvaro Garcia Gomez',
    author_email='maxpowel@gmail.com',
    url='https://github.com/applauncher-team/redis_bundle',
    download_url='https://github.com/applauncher-team/redis_bundle/archive/master.zip',
    keywords=['applauncher', 'bundle', 'redis'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System',
                 'Topic :: Utilities'],
    install_requires=install_requires
)
