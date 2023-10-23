from cx_Freeze import setup, Executable 

setup (
  name = 'Manager',
  version = '3.5.5',
  description = "Stworzono okno użytkownika, metodę wybierania folderów oraz podstawowy design",
  executables = [Executable('script.py')]
)
