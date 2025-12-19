# Elegoo™ Centauri Carbon Filament Dryer Script
This script was created to dry the filament using the built-in heated bed inside of Centauri Carbon printer.

## Installing
1. Install
    - [Firefox](https://firefox.com)
    - and [Python](https://www.python.org/downloads) with pip
3. Install dependency: `pip install selenium`
4. Download the repository:
    - by [Downloading the ZIP](https://github.com/Valytia/ECCFilamentDryerScript/archive/refs/heads/main.zip) file and then extracting the files
    - or by using git: `git clone https://github.com/Valytia/ECCFilamentDryerScript.git`
5. Inside of the downloaded folder, the script is ready to be configured and used.

## Configuring
Inside of ecc_dryer_script.py, you can edit three parameters at the beginning of the file:
1. `IP` that points to the printer's IP
2. `TEMP` that is desired bed temperature in Celsius
3. There's also `INTERVAL` that sets the delay between settings of the temperature, but it should be kept as it is since it doesn't actually differ between Centauri Carbon printers.

## Usage
To run:
1. Open up the script's folder in the command-line/terminal
2. Run by executing `python ecc_dryer_script.py` command
3. Done! Enjoy drying your filament :)

## License
This script is licensed under GPLv3 License.
