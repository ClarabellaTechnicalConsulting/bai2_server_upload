##
# Parses BIA2 files and prepares for SQL inserts
#
from datetime import datetime
from bai_codes import bai_codes


class BAI2File:
    def __init__(self, file_name: str, path: str):
        self.file_name = file_name
        with open(path) as file:
            self.lines: list[str] = [line.strip() for line in file.readlines()]
        self.accounts: list[dict] = []
        self.transactions: list[dict] = []
        self.parse()

    def parse(self):
        tracker: bool = True
        cur_account: dict = {'AccountNo': 0,
                             'OpeningBalance': 0,
                             'ClosingBalance': 0,
                             'TotalCredits': 0,
                             'TotalDebits': 0,
                             'CreditCount': 0,
                             'DebitCount': 0,
                             'FileDate': '',
                             'DataLoadDT': '',
                             'FileName': self.file_name}

        cur_transaction: dict = {'BAI2FileDate': '',
                                 'AccountNo': 0,
                                 'Amount': 0.0,
                                 'Description': '',
                                 'Name': '',
                                 'DataLoadDT': '',
                                 'FileName': ''}

        file_date: str = self.lines[0][22:28]
        file_date = '20' + file_date[0:2] + '-' + file_date[2:4] + '-' + file_date[4:]
        for line in self.lines[2:]:
            rec_type: str = line[0:2]
            if rec_type == '03':
                tracker = True
                cur_account = {'AccountNo': line[3:13],
                               'OpeningBalance': 0,
                               'ClosingBalance': 0,
                               'TotalCredits': 0,
                               'TotalDebits': 0,
                               'CreditCount': 0,
                               'DebitCount': 0,
                               'FileDate': file_date,
                               'DataLoadDT': datetime.today().strftime('%Y-%m-%d'),
                               'FileName': self.file_name}
            elif rec_type == '88':
                if tracker:
                    line_list = line.split(',')
                    if line_list[1] in bai_codes:
                        cur_account[bai_codes[line_list[1]]] = int(line_list[2]) / 100
                else:
                    cur_transaction['Description'] += line[3:]
            elif rec_type == '49':
                self.accounts.append(cur_account)
            elif rec_type == '16':
                tracker = False
                if cur_transaction['AccountNo']:
                    self.transactions.append(cur_transaction)
                line_list = line.split(',')
                cur_transaction = {'BAI2FileDate': file_date,
                                   'AccountNo': cur_account['AccountNo'],
                                   'Amount': int(line_list[2]) / 100,
                                   'Description': '',
                                   'Name': bai_codes[line_list[1]],
                                   'DataLoadDT': datetime.today().strftime('%Y-%m-%d'),
                                   'FileName': self.file_name}
                if 100 <= int(line_list[1]) < 400:
                    cur_account['CreditCount'] += 1
                elif 400 <= int(line_list[1]) < 700:
                    cur_account['DebitCount'] += 1
            elif rec_type == '99':
                self.transactions.append(cur_transaction)

