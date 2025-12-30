# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
from inspector.core import list_tables, get_table_info

def main():
    parser = argparse.ArgumentParser(description="SQLite Inspector")
    parser.add_argument("--db", required=True, help="Path to SQLite DB file")
    parser.add_argument("--info", choices=["tables", "schema"], default="tables", help="Information to show")
    parser.add_argument("--table", help="Specific table to inspect (required for schema)")

    args = parser.parse_args()

    try:
        if args.info == "tables":
            tables = list_tables(args.db)
            print(f"Tables in {args.db}:")
            for t in tables:
                print(f" - {t}")
                
        elif args.info == "schema":
            if not args.table:
                print("Error: --table required for schema inspection.")
                return
            
            info = get_table_info(args.db, args.table)
            print(f"--- Table: {info['name']} ---")
            print(f"Rows: {info['row_count']}")
            print("Schema:")
            print(info['schema'])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
