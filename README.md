# flip-screen

> Flip your screen automatically past a certain hour.

# Table of contents
  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Contributing](#contributing)

## Requirements

* Linux

## Installation

1. Go to your installation path: ```cd your/desired/installation/path```
1. Clone the repo: ```git clone https://github.com/timotheechauvin/flip-screen```
1. In ```main.py```, change the value of *invert_hour* to your preferred value.
1. Go to "Startup applications" (type <kbd>Super</kbd> then *startup*, and select it).
1. Click *"Add"*
1. Type:
  * name = ```flip-screen```
  * command = ```/bin/bash -c "sleep 15 && python3 your/path/flip-screen/main.py"``` (don't forget to put your own path!)
  * comment (optional) = ```From https://github.com/timotheechauvin/flip-screen```

Now the main program is working (you'll have to restart your computer, though). Now you may want to be able to revert the screen(s) back to normal on certain circumstances. That's where ```norscr.py``` comes in handy.

1. Go to the end of your ```~/.bashrc``` file
1. Add aliases to norscr and invscr:
  * ```alias norscr='your/path/flip-screen/norscr.py'```
  * ```alias invscr='your/path/flip-screen/invscr.py'```

## Usage
If you've completed the steps above, and restarted your computer, your screen should get inverted at the hour specified by the variable *invert_hour*.

You can also invert and get your screen back to normal by typing respectively ```invscr``` and ```norscr``` in your terminal.

## Contributing

Issues, feedback and pull requests are all warmly welcome!

## License

This project is under the MIT license.