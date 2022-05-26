from setuptools import setup, find_packages

setup(name="backend",
      version="1.0",
      author="Kirill Raikov",
      author_email="kraykov45@gmail.com",
      description="This is a simple api for book ordering with sqlalchemy db",
      python_requires='>=3.6',
      packages=find_packages())