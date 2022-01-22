from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name="toci",
        version="0.0.3",
        author="Hakan Ozler",
        author_email="ozler.hakan@gmail.com",
        description="markdown tool to create table of content from jupyter notebooks",
        long_description=long_description,
        long_description_content_type="text/plain; charset=UTF-8",
        url="https://github.com/ozlerhakan/toci",
        project_urls={
            "Bug Tracker": "https://github.com/ozlerhakan/toci/issues",
        },
        license="MIT",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        python_requires=">=3.7",
        keywords=["python", 'jupyter', 'notebook', 'markdown', 'toc'],
        install_requires=[
            'nbconvert>= 6.2.0',
            'nbformat>=5.1.3',
            'mistune==0.8.4',
        ],
        platforms=["linux", "unix"],
        entry_points={
            "console_scripts": [
                "toci=toci.Toci:main"
            ],
        }
    )
