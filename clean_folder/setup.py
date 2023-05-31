from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='sort files in specified directory',
    url='https://github.com/AntonHran/python_core_ht_7.git',
    author='AntonHran',
    author_email='t.granowsky@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['cln = clean_folder.clean:main']}
)
