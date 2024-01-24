from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' #-e . automatically triggers setup.py
def get_requirements(file_path:str)->List[str]:
    '''
    this will return list of requirments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]#reading each line and replacing \n with blank
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)#-e . will also be read that must be removed
        
    return requirements

#pip install -r requirements.txt

setup(
    name='mlproject',
    version='0.0.1',
    author='Anushreel',
    author_email='anushreelgowda12@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)