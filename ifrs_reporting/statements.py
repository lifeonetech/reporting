import yaml
from typing import Dict


def load_data(path: str) -> Dict:
    """Load financial data from a YAML file."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_report(data: Dict) -> str:
    """Generate a simple textual IFRS report from data."""
    balance_sheet = data.get('balance_sheet', {})
    income_statement = data.get('income_statement', {})

    report_lines = []
    report_lines.append('IFRS REPORT')
    report_lines.append('============')
    report_lines.append('\nBALANCE SHEET')

    assets = balance_sheet.get('assets', {})
    liabilities = balance_sheet.get('liabilities', {})
    equity = balance_sheet.get('equity', {})

    total_assets = sum(_flatten_values(assets))
    total_liabilities = sum(_flatten_values(liabilities))
    total_equity = sum(_flatten_values(equity))

    report_lines.append(f'Total Assets: {total_assets}')
    report_lines.append(f'Total Liabilities: {total_liabilities}')
    report_lines.append(f'Total Equity: {total_equity}')
    report_lines.append(f'Assets = Liabilities + Equity: {total_assets == total_liabilities + total_equity}')

    report_lines.append('\nINCOME STATEMENT')
    revenue = income_statement.get('revenue', 0)
    cost_of_sales = income_statement.get('cost_of_sales', 0)
    operating_expenses = income_statement.get('operating_expenses', 0)
    finance_costs = income_statement.get('finance_costs', 0)
    income_tax_expense = income_statement.get('income_tax_expense', 0)

    gross_profit = revenue - cost_of_sales
    operating_profit = gross_profit - operating_expenses
    profit_before_tax = operating_profit - finance_costs
    profit_for_year = profit_before_tax - income_tax_expense

    report_lines.append(f'Revenue: {revenue}')
    report_lines.append(f'Cost of Sales: {cost_of_sales}')
    report_lines.append(f'Gross Profit: {gross_profit}')
    report_lines.append(f'Operating Expenses: {operating_expenses}')
    report_lines.append(f'Operating Profit: {operating_profit}')
    report_lines.append(f'Finance Costs: {finance_costs}')
    report_lines.append(f'Profit Before Tax: {profit_before_tax}')
    report_lines.append(f'Income Tax Expense: {income_tax_expense}')
    report_lines.append(f'Profit for the Year: {profit_for_year}')

    return '\n'.join(report_lines)


def _flatten_values(section: Dict) -> list:
    """Recursively collect all numeric values from a nested dict."""
    values = []
    for value in section.values():
        if isinstance(value, dict):
            values.extend(_flatten_values(value))
        elif isinstance(value, (int, float)):
            values.append(value)
    return values
