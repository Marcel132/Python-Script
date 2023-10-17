from cx_Freeze import setup, Executable 

setup (
  name = 'Manager',
  version = '3.5.3',
  description = "Update styles, add comments and change some code",
  executables = [Executable('script.py')]
)
