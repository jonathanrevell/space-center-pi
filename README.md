# space-center-pi

## Running on a Raspberry Pi

1. git clone https://github.com/jonathanrevell/space-center-pi
1. python main.py

## Installation outside of a Raspberry Pi device

1. Make sure python 3 is installed
1. Install the python libraries
1. Import https://gpiozero.readthedocs.io/en/stable/

### Running on Mac/Windows
1. Install gpiozero pigpio https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

    GPIOZERO_PIN_FACTORY=mock python main.py


Checking the pinout in the terminal on the Raspberry Pi itself:

https://gpiozero.readthedocs.io/en/stable/cli_tools.html?highlight=mock#envvar-GPIOZERO_PIN_FACTORY
