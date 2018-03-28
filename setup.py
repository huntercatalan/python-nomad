from distutils.core import setup

try:
    requirements = [ x.strip() for x
        in open('requirements.txt').readlines() if not x.startswith('#')]
except:
    requirements = []

setup(
    name='pynomad',
    version='0.7.0',
    install_requires=requirements,
    packages=['nomad', 'nomad.api'],
    url='http://github.com/jrxfive/python-nomad',
    license='MIT',
    author='jrxfive',
    author_email='jrxfive@gmail.com',
    description='Client library for Hashicorp Nomad',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='nomad hashicorp client',
)
