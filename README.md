Author of the code: Gonzalo Martínez Fornos
gmartinez@icm.csic.es

ICM CSIC

Inside the project folder you will find several subfolders. The structure is organized this way because each folder has a specific function.
If any folder is removed or renamed, the code will stop working (if changes are made, they must also be updated in the code).

Folders:

lib → This folder contains all the project scripts. The main script is called main.py.

acolite_py_win → This folder is empty, but it needs to be filled in. 
	The code uses a program called ACOLITE, which you will need to download and add to this folder. 
	More information is available in the ACOLITE section.

input and tmp → These are intermediate processing folders used by the code to format files.
	In input, you must place the TriOS files you want to process.
	WARNING: Files placed in the input folder will be deleted during processing. Make a copy of them before running the program.

output → This folder contains sections separated by station. Inside, you will find the files processed by the program at different processing stages, as well as the generated plots.

Sentinel-2 → This folder stores all the processing performed with Sentinel data. It includes an output folder where images and other information are saved.

************** HOW TO USE IT **************

Before running the code, you must update the directories:

Update the required paths in the main.py script.

Fill in the second row of the station.txt file with the longitude and latitude of the station and your Sentinel-2 credentials (https://documentation.dataspace.copernicus.eu/Registration.html).

Additionally, add the TriOS sensor codes in the same document.


************** ACOLITE **************
Download URL → https://github.com/acolite/acolite/releases 
Attention: The Acolite user manual is located at the same download URL.
Publication → Vanhellemont, Q., & Ruddick, K. (2016, May). Acolite for Sentinel-2: Aquatic applications of MSI imagery. In Proceedings of the 2016 ESA living planet symposium, Prague, Czech Republic (Vol. 9).

For the program to work, you must download Acolite and place its folders in the acolite_py_win folder.
In case of Acolite updates that cause errors or if you are using Acolite on a system other than Windows, the following lines of code can be changed:
	functions.py → line 137 to 161:
			These lines of code create the configuration file required by the Acolite program. Variables can be changed and added (see the Acolite manual for instructions). 
			This .txt configuration file will be saved in the Sentinel > output > NDCI_doc folder.
			
	acolite_fun.py → lines 62 to 68:
			These lines of code simply execute the necessary command to run Acolite in a system terminal. 
			These commands are (taken from the 2025 manual):
					Windows: dist\acolite\acolite.exe --cli --settings=settings_file
					Linux and Mac: dist/acolite/acolite --cli --settings=settings_file
