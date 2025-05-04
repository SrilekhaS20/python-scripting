# 📝 File Renamer

## A simple Python script that renames a file using command-line arguments. It accepts the current filename and the new filename as positional arguments and performs a file rename operation.

---

### 📂 Requirements

##### - Python 3.x

---

### 🚀 How to Use

```bash
python file_renamer.py <old_filename> <new_filename>
```
### 📌 Example
bash
```
python file_renamer.py old_file.txt new_file.txt
```
##### This command will rename old_file.txt to new_file.txt if the file exists and permissions are adequate.

### 🧾 Arguments

| Argument   | Type   | Description                        | Required |
|------------|--------|------------------------------------|----------|
| `old_name` | string | The current name of the file       | ✅ Yes   |
| `new_name` | string | The new name you want to give      | ✅ Yes   |

### ❗ Error Handling
##### If the old file does not exist, the script prints:

arduino
```
File not found
```
##### If an unexpected error occurs (e.g., permission issues), it prints:

nginx
```
An error occurred: <error message>
```
### 🔐 Set Read-Only to Test Error
##### Use the following command to make a file read-only and test permission-related errors:

bash
```
chmod 444 old_file.txt
```
##### To revert back to writable:

bash
```
chmod 644 old_file.txt
```
