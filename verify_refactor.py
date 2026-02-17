import os
import subprocess
import sys

def run_command(cmd):
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        print(f"STDOUT:\n{result.stdout}")
        print(f"STDERR:\n{result.stderr}")
        return result.returncode
    except subprocess.TimeoutExpired:
        print("Command timed out after 60 seconds")
        return 130
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

if __name__ == "__main__":
    venv_python = "./venv/bin/python"
    
    with open("refactor_log.txt", "w") as f:
        # 1. Makemigrations
        f.write("--- Makemigrations ---\n")
        res = subprocess.run(f"{venv_python} manage.py makemigrations committee_options", shell=True, capture_output=True, text=True)
        f.write(res.stdout + "\n" + res.stderr + "\n")
        
        # 2. Migrate
        f.write("--- Migrate ---\n")
        res = subprocess.run(f"{venv_python} manage.py migrate committee_options", shell=True, capture_output=True, text=True)
        f.write(res.stdout + "\n" + res.stderr + "\n")
        
        # 3. Seed content
        f.write("--- Seed Content ---\n")
        res = subprocess.run(f"{venv_python} manage.py seed_content", shell=True, capture_output=True, text=True)
        f.write(res.stdout + "\n" + res.stderr + "\n")
        
    print("Verification complete! Check refactor_log.txt")
