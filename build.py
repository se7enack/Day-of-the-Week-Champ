"""
This build.py script is for py2applet to build a binary from python source code (cryptocreeper.py)

Usage:
    python3 build.py py2app
"""

from setuptools import setup

APP = ['game.py']
DATA_FILES = ['bad.mp3','good.mp3','perfect.mp3']
OPTIONS = {
    'iconfile':'icon.ico'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)