# INI Parser
## Introduction
`*.ini` files are an important part of configuration file types. Along with `*.conf`, `*.cfg`, `*.yml`, `ini` files are also used at a large extent. Reading the values of such files is crucial while playing with configurations. So, the **INIParser** gives a wrapper class for Python to use the `ini` files in Python. **INIParser** allows to read, write, update, delete the settings in such files. Also it is light-weight and end-user friendly. Anyone with minimum exposure to Python can use this. Also it is safe for the files as it allows to create backup of the files and avoid loss of data during the any file operations.

### Sample `ini` file
```
; Sample ini file
; Comments either start with semicolon ';'
# or with hash symbol '#'.
[ThisIsASection]
someKey=itsValue
anotherKey=9089

; An ini file can contain multiple sections
[INIParser]
version=1.0alpha
contributor=AtharvaKale
github_repo=/alphakilo7/ini-parser.git
; eof 
```

## Usage
Simply clone the directory!
```
git clone https://github.com/alphakilo7/ini-reader.git
```
and done!
Following manual will show how to use the reader in python
---
**operations.py**
```
# Recommended import format
import INIParser as inip


def run():
	# initiate parser
	ini = inip.INIParser("/usr/share/manager/manage.ini", backup=True)

	# Get section configuration
	SVALUE = ini.get("section_name")

	# Get value of particular key
	KVALUE = ini.get("section_name", "key_name")

	# Create an empty section
	ini.set("new_section")

	# Create a new key under section
	ini.set("new_section", "new_key", "value")

	# Delete a section
	ini.delete("section_name")

	# Delete a key under a section
	ini.delete("section_name", "key")

	# AND FINALLY, DO NOT FORGET TO COMMIT THE CHANGES TO THE FILE
	ini.commit()

run()

```

#### Few Limitations (as of now)
1. As of now, the in file comments are tracked, but in the final output, it is likely to be misplaced. Please use with caution.
2. The comments after key-value pairs are not read as comments but are considered as part of value of the key. Highly recommended not to use such style of commenting.
