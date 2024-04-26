import subprocess

def run_command(command):
    # Run a command and return its output.
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return process.stdout
