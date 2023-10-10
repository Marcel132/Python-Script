from cx_Freeze import setup, Executable 

setup (
  name = 'Manager',
  version = '2.0',
  description = "Aktualizacja programu",
  executables = [Executable('script.py')]
)
