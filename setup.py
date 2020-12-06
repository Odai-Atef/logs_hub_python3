from distutils.core import setup
setup(
  name = 'LogsHub',         # How you named your package folder (MyLib)
  packages = ['LogsHub'],   # Chose the same as "name"
  version = '1.1.5',      # Start with a small number and increase it with every change you make
  license='OpenSource',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Writing specific logs',   # Give a short description about your library
  author = 'Odai',                   # Type in your name
  author_email = 'o.3odai@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Odai-Atef/logs_hub_python3',   # Provide either the link to your github or to your website
  install_requires=[            # I get to this in a second
          'python-decouple',
          'requests'
      ],
  entry_points={
    'console_scripts': ['LogsHub=LogsHub.logs_hub:main']
  },
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    # 'License ::  OpenSource',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
