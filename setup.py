import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name='spotify',
  packages=setuptools.find_packages(),
  version='0.0.1',
  license='MIT',
  description='Personal spotify analytics',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author='Lauren McNamara',
  author_email='lauren.mcnamara@gmail.com',
)
