from cx_Freeze import setup, Executable

setup(
    name='Gerador de PDF',
    version='1.0',
    description='Projeto adicionar textos, um titulo como cabeçalho, um tituto pro texto',
    executables=[Executable('app.py')]
)
