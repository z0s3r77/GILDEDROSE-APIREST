from setuptools import setup, find_packages

setup(
    name="Flask API Rest Olivanders",
    version="0.1",
    author="z0s3r77",
    author_email="ipopdue24@gmail.com",
    description="Little Rest API that is used to update items from a Cloud MongoDB ",
    packages=find_packages(),
    install_requires=["Flask==2.2.3", "pytest==7.2.1"],
    entry_points={"console_scripts": ["my-App = controller.main:run"]},
)
