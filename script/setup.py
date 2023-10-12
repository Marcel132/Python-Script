from cx_Freeze import setup, Executable 

setup (
  name = 'Manager',
  version = '~~',
  description = "Dodanie możlwości utworzenia kont użytkownika",
  executables = [Executable('script.py')]
)
