from cx_Freeze import setup, Executable 

setup (
  name = 'Manager',
  version = '3.2',
  description = "Dodanie możlwości utworzenia kont użytkownika",
  executables = [Executable('script.py')]
)
