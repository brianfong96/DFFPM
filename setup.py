from distutils.core import setup
setup(
  name = 'DFFPM',
  packages = ['DFFPM'],
  version = '0.1',
  license='MIT',
  description = 'Directory Folder File Path Manager',
  author = 'brianfong96',
  author_email = 'brianwkfong@gmail.com',
  url = 'https://github.com/brianfong96/DFFPM',
  download_url = 'https://github.com/brianfong96/DFFPM/archive/v_01.tar.gz',
  keywords = ['Path', 'Directory', 'Folder', 'File'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',      #Specify which python versions that you want to support    
  ],
)