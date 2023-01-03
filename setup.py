from setuptools import find_packages,setup

requirement_file_name="requirements.txt"
hyphen_e_dot ="-e ."
def get_requirements():
    with open(requirement_file_name) as requirement_file :
        requirement_list=requirement_file.readlines()
    requirement_list=[requirement_name.replace("/n","") for requirement_name in requirement_list ]
    if hyphen_e_dot in requirement_list:
        requirement_list.remove(hyphen_e_dot)
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="vijay",
    author_email="vijaymshine09@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)