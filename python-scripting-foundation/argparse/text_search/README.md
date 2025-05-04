# 🔍 Text Search in File

## This Python script allows you to search for a specific string in a text file using command-line arguments. It supports both case-sensitive and case-insensitive search.

---

### 📄 Description

##### - Search for any string in a given file.
##### - Supports case-insensitive search with `-i` or `--ignore-case`.
##### - Uses Python's `argparse` for command-line arguments.

---

### 🚀 Usage

```bash
python search.py --file log.txt --search ERROR
```

##### For case-insensitive search:

```bash
python search.py --file log.txt --search error -i
```

### 🧾 Arguments

| Argument            | Type   | Description                          | Required |
|---------------------|--------|--------------------------------------|----------|
| `--file`            | string | Path to the file to be searched      | ✅ Yes   |
| `--search`          | string | The text to search for               | ✅ Yes   |
| `-i`, `--ignore-case` | flag   | Enable case-insensitive search     | ❌ No    |

### 📝 Example log.txt

```yaml
[2025-04-30 10:15:23] INFO Starting application
[2025-04-30 10:15:25] INFO Connecting to database...
[2025-04-30 10:15:27] WARNING Connection is slow
[2025-04-30 10:16:02] ERROR Failed to fetch user data: TimeoutError
[2025-04-30 10:17:12] ERROR Invalid input format: expected JSON
[2025-04-30 10:16:02] error Failed to fetch user data: TimeoutError
```

### ✅ Example Output

```bash
python search.py --file log.txt --search error -i
```

##### Output:

```pgsql
[2025-04-30 10:16:02] ERROR Failed to fetch user data: TimeoutError
[2025-04-30 10:17:12] ERROR Invalid input format: expected JSON
[2025-04-30 10:16:02] error Failed to fetch user data: TimeoutError
```

###⚠️ Error Handling
##### Displays File not found if the file is missing.

### 📂 Project Structure

```pgsql
.
├── search_text.py
└── log.txt
```
