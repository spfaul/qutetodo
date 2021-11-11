# QuteTodo
A minimalist To-Do list built using the Qt Framework.
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Naereen/StrapDown.js.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/Naereen/StrapDown.js/stargazers/)
[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/issues/)
![asdasd](https://user-images.githubusercontent.com/69741305/141303273-0986f8a0-c254-4a26-855b-de9e87b28867.png)


## Installation
### Building From Source
1. Download The Repo Locally
```bash
git clone https://github.com/t0a5ted/qutetodo.git
```
2. Install All Dependencies (WINDOWS)
```bash
cd qutetodo
python -m pip install -r requirements.txt
```
3. Done! Run `main.py` To Start **QuteTodo**!  (WINDOWS)
```bash
python main.py
```

## Usage
A default configuration file is provided at `config/config.ini`. Syntax of the configuration file is similar to that of Microsoft Windows INI files. 

QuteTodo will use the configuration profile specified under `[PROGRAM]`. If a profile other than `DEFAULT` is being used, any key-value pairs which are not specified in the profile will fallback to the respective key-value pair in `[DEFAULT]` .

Below are the available configuration keys and their usages.

| Name            | Purpose                                                                                                                                                                                   | Usage                                                    |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| Title           | Set the text of the title of the window                                                                                                                                                   | Title = [STRING]  e.g. Title = Hello World!              |
| StartupHeight   | Set the height of the window at startup                                                                                                                                                   | StartupHeight = [INT]  e.g. StartupHeight = 300          |
| StartupWidth    | Set the width of the window at startup                                                                                                                                                    | StartupWidth = [INT]  e.g. StartupWidth = 300            |
| Opacity         | Set the opacity of the window (from 0 to 1)                                                                                                                                               | Opacity = [FLOAT]  e.g. Opacity = 0.7                    |
| DoAutoSave      | If enabled, will automatically save todos and their progress between sessions.                                                                                                            | DoAutoSave = [BOOL]  e.g. AutoSave = yes                 |
| SaveFile        | Relative or Absolute file path of the file which progress will be saved in. It is  recommended not to edit the contents of the file as it might mess up the reading/writing of progress.  | SaveFile = [STRING]  e.g. SaveFile = saves/autosave.todo |
| WindowStayOnTop | If enabled, the window acts as an overlay over other applications to keep you focused. Fullscreen applications may disrupt this feature.                                                  | WindowStayOnTop = [BOOL]  e.g. WindowStayOnTop = no      |



## Contributing
Feel free to make PRs or file an issue to help fix bugs and make feature requests.
> **NOTE: Not all PRs may be merged. It really depends on what I feel is best for the project.**

## License
This project is licensed under the MIT License. See LICENSE.txt for more.

## Credit
This project was inspired by and makes use of several components in [Wanderson Magalhaes](https://github.com/Wanderson-Magalhaes "wanderson")'s [PyOneDark](https://github.com/Wanderson-Magalhaes/PyOneDark_Qt_Widgets_Modern_GUI)

## FYI
Support the project by giving the repo a ⭐!
