import os
import subprocess
import sys

if __name__ == '__main__':
    python_executable = 'python' if sys.version_info[0] < 3 else 'python3'
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'main.py')

    subprocess.run([python_executable, script_path])

