from setuptools import setup, find_packages


setup(
    name="supervisor-sysinfo",
    version=__import__("supervisor_sysinfo").__version__,
    description="a supervisor rpc extension for obtaining the hosts system and process information",
    author="thanos vassilakis",
    author_email="thanosv@gmail.com",
    url="https://github.com/thanos/supervisor-sysinfo",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Topic :: System :: Boot',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
    ],
    include_package_data=True,
    install_requires = ['setuptools','psutil','supervisor'],
    zip_safe=False,
)   