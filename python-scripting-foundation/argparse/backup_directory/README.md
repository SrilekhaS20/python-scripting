# 📁 Directory Backup Script

## This script creates a backup of a specified directory in ZIP format.

### 💻 Usage

```bash
python backup_script.py --source <source_directory> --destination <destination_zip_name>
```
##### Example:

```bash
python backup_script.py --source /path/to/directory --destination /path/to/backup/my_backup
```

### 🧾 Arguments

| Argument      | Type   | Description                                 | Required |
|--------------|--------|---------------------------------------------|---------|
| --source      | string | Path to the directory to be backed up        | ✅ Yes  |
| --destination | string | Path and name for the output ZIP file        | ✅ Yes  |

### ✅ Features

##### Verifies whether the source directory exists.

##### Creates a ZIP file with the given name in the specified location.

##### Prints a success message upon completion.

##### Uses Python's argparse, os, and shutil libraries.

### ⚠️ Error Handling
##### If the source directory does not exist, an error message will be displayed.

##### If the destination path is invalid, the script will throw an exception.

### 🚀 Example Output

```swift
Backup is successful: /path/to/backup/my_backup.zip is created
```
