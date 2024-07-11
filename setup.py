from setuptools import find_packages,setup
from typing import List
HYPHEN="-e ."
def get_requirements(file_path:str)-> List[str]:
    '''return the list of requirements'''
    req=[]
    with open(file_path) as fileobj:
        req=fileobj.readlines()
        req=[r.replace("\n","") for r in req]
    if HYPHEN in req:
        req.remove(HYPHEN)
    return req 
    
setup(
    name="mlproject",
    version='0.0.1',
    author='Ishika',
    author_email="ishika.datascientist@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)