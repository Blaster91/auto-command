from cx_Freeze import setup, Executable
base = None
#Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("auto-command.py", base=base)]
#Renseignez ici la liste complète des packages utilisés par votre application
packages = ["time","clipboard","keyboard","configparser"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
#Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "auto-command",
    options = options,
    version = "0.9",
    description = '',
    executables = executables
)
