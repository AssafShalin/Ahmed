from cx_Freeze import setup, Executable
print('testing')
setup(
        name = "Ahmad",
        version = "2.0",
        description = "Random Desktop",
        executables = [Executable("Ahmed.py",icon="icon.ico")]
)