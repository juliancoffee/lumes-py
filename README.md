What can it do?
==========

Simple wrapper around maim and xclip for doing screenshots.</br>
For help write</br>
`$ lumes -h`

Requirements
----------

1. maim
2. xclip

Installation
------------
To upgrade pip
</br>`$ python3 -m pip install -U pip`
</br>To be sure you use proper version of python
</br>`$ python3 -m pip install lumes`
</br>To upgrade lumes
</br>`$ python3 -m pip install -U lumes`

Features
-----------

1. Selection area
2. Move screen to clipboard (by default)
3. Save screenshot in file
4. Save screenshots in directory

Examples
----------
For just get picture of your screen and copy it to clipboard
</br>`$ lumes `
</br>The same but with selection of area
</br>`$ lumes -s `
</br>Save in file
</br>`$ lumes -f img.png`
</br>Choose selection and save in directory with screenshots (if you have that directory)
</br>`$ lumes -s -d $HOME/Screenshots/`

In future
----------

1. Wayland support
2. Shell-completions support
3. Integrations with xdotool
