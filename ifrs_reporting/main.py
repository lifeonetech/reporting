import argparse
from . import statements

def main():
    parser = argparse.ArgumentParser(description="Generate simple IFRS reports from YAML data")
    parser.add_argument('input', help='Path to YAML file with financial data')
    parser.add_argument('-o', '--output', help='Optional output path for generated report (txt)')
    args = parser.parse_args()

    data = statements.load_data(args.input)
    report = statements.generate_report(data)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
    else:
        print(report)

if __name__ == '__main__':
    main()
