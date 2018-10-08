# COMS3000 2018 - Assignment 3

>TODO: About the project

## Requirements

- Python3

## Folder Overview

```bash
<repo>
|-- python
    |-- target_processor.py (Converts raw into targets.json)
|-- target
    |-- processed
        |-- targets.json (Processed JSON file with user and pwd info)
    |-- raw
        |-- passwd9 (Raw user info)
        |-- shadow9 (Raw password info)
```

## Running

1. Open a command prompt in `<repo>\bin\john-the-ripper\windows\`
2. Run `john.exe ..\..\..\targets\raw\shadow`
3. Profit?

## Configuration

Modify `<repo>\bin\john-the-ripper\windows\john.conf` (To add rules etc) and `<repo>\bin\john-the-ripper\windows\password.lst` (To add password guesses)