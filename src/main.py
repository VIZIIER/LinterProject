import sys
from analyzer import run_analysis

def main():
    # Assume the first argument is the directory to analyze.
    # In a real application, you'd want to use argparse for robust argument parsing.
    target_directory = sys.argv[1]
    report = run_analysis(target_directory)
    print(report)

if __name__ == "__main__":
    main()
