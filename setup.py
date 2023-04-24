from  setuptools import find_packages , setup
from typing import List
# So this will automatically find out all the packages that are available in the Entire Machine Learning Application
# In the Directory that we have actually created




# This file_path is str and this will basically return a list ->List
# & in order to return a list we can basically write it in a function which will be in a form of str ->List[str]
# Basically we are saying our function will return a list -- bcoz this requirements.txt will basically have a list of Libraries
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requriements
    """
    requriements = []
    # Either you can specify the file name like requriements.txt or either i can specify directly file_path over here
    with open(file_path) as file_obj: # Lets create this as a temprorary file object
        # There is a slight problem whenver we use readlines and read line by line  a '/n' object or string is also added.
        # So once we get the requriement we will try to replace the '/n' with blank
        requirements = file_obj.readlines()
        # For that we are going to use List Comprehension where we use a function replace to replace the string with any '\n' as blank space
        requirements = [req.replace("\n","") for req in requirements]

        # If 'e- .' is found when we are reading requriements.txt file and we want to remove it from our list of requriements
        # This function is used for it  -- bcoz '-e .' triggers your setup.py file while installing all the requried libraries or building packages
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)



# All the Parameters that are required
# Whenever we are creating the Package what name is the Project of , What application is The Project of
setup(
name = 'mlproject',
# You can basically consider all of this as a MetaData Of the Entire Project
version='0.0.1',
# So whenver my new version will come i'll keep on updating it and Automatically  that entire Package will be build & go into the pypi where you can use it
author = "Kshtu",
author_email = 'kshetijpuri1994@gmail.com',
packages = find_packages(),
# Here you can mention what all requirements you want like Pandas , Numpy etc .. SO whatever libraries i want i can write it over here
install_requires = get_requirements('requirements.txt') # And automactically it will do the installation of all the libraries

)
