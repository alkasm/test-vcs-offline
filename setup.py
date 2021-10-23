from distutils.core import setup

setup(
    name="test-vcs-offline",
    install_requires=[
        "six==1.15.0",
        "theta-alkasm @ git+https://github.com/alkasm/theta.git",
    ],
)
