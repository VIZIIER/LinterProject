import sys
from analyzer import run_analysis

def main():
    target_directory = sys.argv[1]
    report = run_analysis(target_directory)
    print(report)

if __name__ == "__main__":
    main()
