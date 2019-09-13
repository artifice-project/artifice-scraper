from artifice.etc import (
    terminal_output,
    artifice_version,
    artifice_logo,
    artifice_help
)

def main():
    terminal_output(
        artifice_version(),
        artifice_logo(),
        artifice_help(),
    )


if __name__ == '__main__':
    main()
