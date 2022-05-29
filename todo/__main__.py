# Provides an entry-point script to run the app from the package using the python -m rptodo command
from todo import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()