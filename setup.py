__author__ = 'daniil'
from cx_Freeze import setup, Executable

base = "win32GUI"

includes = ['gzip', 'distutils', 'pkg_resources']
packages = []
buildOptions = {"packages": packages, "includes": includes, "optimize" : 2,"compressed" : True}

setup(
        name = "tc4u",
        version = "1.0",
        description = "TrueCrypt For You",
        author = "Daniil Leksin",
        classifiers = [
              'Development Status :: 1 - Beta',
              'Environment :: Win application',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: Python Software Foundation License',
              'Operating System :: Microsoft :: Windows',
              'Programming Language :: Python',
              ],
        options = dict(build_exe=buildOptions),
        executables = [Executable('main.py',
                       base=base, includes=includes, copyDependentFiles=True,
                       targetName='tc4u.exe' )]
    )
