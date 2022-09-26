from py2exe import freeze

freeze(
    windows=["./boba.py"],
    data_files=None,
    zipfile='library.zip',
)