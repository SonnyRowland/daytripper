#!/usr/bin/env python3
import socket
import subprocess
import sys
import time


def wait_for_postgres(host, port, max_attempts=60):
    """Wait for PostgreSQL to be ready"""
    for attempt in range(max_attempts):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            sock.close()

            if result == 0:
                print(f"PostgreSQL is ready! (attempt {attempt + 1})")
                return True

            print(f"Waiting for PostgreSQL... (attempt {attempt + 1}/{max_attempts})")
            time.sleep(1)

        except Exception as e:
            print(f"Connection attempt {attempt + 1} failed: {e}")
            time.sleep(1)

    print(f"Failed to connect to PostgreSQL after {max_attempts} attempts")
    return False


if __name__ == "__main__":
    if wait_for_postgres("postgres", 5432):
        print("Running database population script...")
        result = subprocess.run(["python3", "-m", "app.scripts.populate_db"])
        sys.exit(result.returncode)
    else:
        sys.exit(1)
