from setuptools import setup

setup(name='lasotuvi_django',
      version='0.1.3',
      description='Chuong trinh an sao tu vi ma nguon mo su dung django',
      long_description="Chuong trinh an sao tu vi ma nguon mo su dung django",
      long_description_content_type="text/markdown",
      url='https://github.com/doanguyen/lasotuvi-django',
      author='doanguyen',
      author_email='dungnv2410@gmail.com',
      license='MIT',
      packages=['lasotuvi_django'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      include_package_data=True,
      install_requires=[
          "Django >= 2.1.2",
          "lasotuvi@git+https://github.com/nambhd/lasotuvi#egg=lasotuvi",
          "pytz==2018.5",
          "six==1.11.0",
          "typed-ast==1.5.5",
      ],
      zip_safe=False)
