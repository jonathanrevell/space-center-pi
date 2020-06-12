# space-center-pi

## Running on a Raspberry Pi

1. git clone https://github.com/jonathanrevell/space-center-pi
1. python main.py

## Installation outside of a Raspberry Pi device

1. Make sure python 3 is installed
1. It may be worthwhile to install [pyenv](https://github.com/pyenv/pyenv)
1. Install the python libraries
1. Install klein
1. Import https://gpiozero.readthedocs.io/en/stable/


## Installing Klein
A better web server https://pypi.org/project/klein/0.2.3/

    pip install klein

    // Or with pyenv
    pyenv exec pip install klein


### Running on Mac/Windows
1. Install gpiozero pigpio https://gpiozero.readthedocs.io/en/stable/remote_gpio.html
1. Run the program

    GPIOZERO_PIN_FACTORY=mock python3 main.py

    // Or with pyenv
    GPIOZERO_PIN_FACTORY=mock pyenv exec python main.py

    //Running with a remote IP address
    PIGPIO_ADDR=192.168.1.137 python3 main.py

    // Running remotely with pyenv
    PIGPIO_ADDR=192.168.1.137 pyenv exec python main.py


Checking the pinout in the terminal on the Raspberry Pi itself:

https://gpiozero.readthedocs.io/en/stable/cli_tools.html?highlight=mock#envvar-GPIOZERO_PIN_FACTORY
