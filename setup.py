from pathlib import Path
from setuptools import setup, find_packages

long_description = Path("README.md").read_text()
reqs = Path("requirements.txt").read_text().strip().splitlines()

def main() -> None:
    pkg = "plaintext_playlist_py"
    setup(
        name=pkg,
        version="0.1.0",
        url="https://github.com/seanbreckenridge/plaintext_playlist_py",
        author="Sean Breckenridge",
        author_email="seanbrecke@gmail.com",
        license="MIT",
        packages=find_packages(include=[pkg]),
        install_requires=reqs,
        package_data={pkg: ["py.typed"]},
        zip_safe=False,
        keywords="music",
        python_requires=">=3.10",
        entry_points={
            "console_scripts": [
                "plaintext_playlist_py = plaintext_playlist_py.__main__:main"
            ]
        },
        scripts=[str(p) for p in Path("bin").rglob("*")],
        extras_require={
            "testing": [
                "mypy",
                "flake8",
            ]
        },
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
        ],
    )

if __name__ == "__main__":
    main()
