from setuptools import find_packages, setup

package_data = {"": ["README.md"]}

setup(
    name="Flask API Rest Olivanders",
    version="0.1",
    author="z0s3r77",
    author_email="ipopdue24@gmail.com",
    url="https://github.com/z0s3r77/PROYECTO-FLASK",
    description="Little Rest API that is used to update domain from a Cloud MongoDB ",
    packages=find_packages(),
    install_requires=[
        "auto_mix_prep==0.2.0",
        "Flask==2.2.3",
        "Flask_Cors==3.0.10",
        "Flask_RESTful==0.3.9",
        "pymongo==4.3.3",
        "pytest==7.2.1",
        "requests==2.28.2",
        "setuptools==59.6.0",
    ],
    entry_points={"console_scripts": ["my-App = controller.main:run"]},
    package_data=package_data,
)
