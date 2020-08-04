from setuptools import setup, find_packages


requirements = [
    "selenium==3.141.0",
]

test_requirements = [
    "black==19.10b0",
]

build_requirements = [
    "setuptools-scm==3.3.3",
    "wheel",
]

setup(
    name="type-faster-than-chan",
    description="a script to type defeat my coworker in a typing test",
    author="Michael Tanner",
    author_email="tanner.mbt@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    setup_requires=test_requirements + build_requirements,
    tests_require=test_requirements + build_requirements,
    extras_require={
        "test": test_requirements + build_requirements,
        "build": build_requirements,
    },
    python_requires=">=3.7",
    use_scm_version=True,
)
