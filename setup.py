from setuptools import setup, find_packages

requirements_list=[]
def requirements()->list:
    with open('requirements.txt') as f:
        for line in f:
            if line.strip()!="-e .":
                requirements_list.append(line.strip())

    return requirements_list

setup(
    name='MLops Cityscape',
    version='0.1.0',
    author='Saumya Vaidya',
    author_email="prince.saumya05@gmail.com",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=requirements(),
    python_requires='>=3.8'
)   