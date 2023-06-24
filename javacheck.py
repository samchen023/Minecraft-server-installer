import re
import subprocess

def get_java_version():
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        output = result.stderr
        version_line = output.splitlines()[0]
        version_match = re.search(r'(\d+)', version_line)
        if version_match:
            version = version_match.group(1)
            return version
        else:
            return None
    except FileNotFoundError:
        return None

java_version = get_java_version()

if java_version:
    print(f"{java_version}")
else:
    print("Java is not installed or the 'java' command is not accessible.")
