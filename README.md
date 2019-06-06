# labelme_kai

This program is modified version of labelme(https://github.com/wkentaro/labelme).

Specializes in continuous annotation.


## Changes
- Save as default name without File Select Dialog.
    default name : original_file_name.json
    expsample : IMG_001.png -> IMG_001.json

- Store Label for each create mode. (ContinuationLabel)

- Add ClearContinuationLabel command that clear the above label in the current mode.

- Show shortcuts


## How to use
(TODO : change to command)

1. Clone this repo.
2. Move into repo.
3. `pyhton main.py`


## Shortcuts

| shortcuts | action |
|:--        |:--     |
| N         | Create Polygons |
| P         | Create Point |
| L         | Create Line |
| R         | Create Rectangle |
| C         | Create Circle
| B         | Clear ContinuationLabel |
| S         | Save   |
| A         | Prev image |
| D         | Next image |
| Ctrl(cmd) + Z | Undo |

