# SQLite Database Inspector (Python)

A CLI util to quickly inspect the structure of a SQLite database file.

## Features

-   **List Tables**: Shows all tables in the database.
-   **Show Schema**: Displays the definition (CREATE statement) for a table.
-   **Row Count**: Quickly see how many rows are in each table.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
# General Info
python run_inspector.py --db my.db

# Show tables
python run_inspector.py --db my.db --info tables

# Show schema of a specific table
python run_inspector.py --db my.db --table users --info schema
```

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
