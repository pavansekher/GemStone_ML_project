from setuptools import find_packages,setup
from typing import List


HYPEN_R_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_R_DOT in requirements:
            requirements.remove(HYPEN_R_DOT)
    
    return requirements
    

setup(
    name="Regressor Project",
    version='1.0',
    author_email="k.pavansai900#gmail.com",
    author="pavan",
    install_requires=['numpy','pandas','seaborn'],
    packages=find_packages(),
    


)