from setuptools import setup, find_packages


def get_requirements(file_path:str) -> list[str]:
    '''
    This function will return list of requirements
    '''
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name='studentPerformanceIndicator',
    version='1.0.0',
    author='AmrAhmed',
    author_email='amr.ahmedm95@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements('requirements.txt')
)

