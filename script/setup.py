from cx_Freeze import setup, Executable 

setup (
  name = 'Manager',
  version = '3.5.1',
  description = "Zmiana styli",
  executables = [Executable('script.py')]
)
