# Elegoo Centauri Carbon Filament Dryer Script
This script was created to dry the filament using the built-in hot bed inside of Centauri Carbon printer.

### Installing
1. Install [Firefox](https://firefox.com)
2. Install dependency: `pip install selenium`
3. Clone this github repository:
`git clone https://github.com/Valytia/ECCFilamentDryerScript.git`
4. Inside of the downloaded folder, the script is ready to be configured and used.

### Configuring
Inside of ecc_dryer_script.py, you can edit three parameters at the beginning of the file:
1. `IP` that points to the printer's IP
2. `TEMP` that is desired bed temperature in Celsius
3. There's also `INTERVAL` that sets the delay between settings of the temperature, but it should be kept as it is since it doesn't actually differ between Centauri Carbon printers.

### Usage
To run:
1. Open up the folder with the script in the terminal
2. Run with `python ecc_dryer_script.py`
3. Done! Enjoy :)

### License
This script is licensed under GPLv3 License.
