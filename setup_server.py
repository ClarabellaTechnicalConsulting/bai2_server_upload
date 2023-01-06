#
#
#

import yaml
import os


def create_sql_server():
    config_dict: dict[str] = {'Server': {'Server Type': 'SQL Server',
                                         'Server Address': 'Address',
                                         'Database Name': 'DB Name',
                                         'Username': 'Username',
                                         'Password': 'Password'}}
    config_dict['Server']['Server Address'] = input('Server Address: ')
    config_dict['Server']['Database Name'] = input('Database Name: ')
    config_dict['Server']['Username'] = input('Username: ')
    config_dict['Server']['Password'] = input('Password: ')
    with open(r'./key.yml', 'w') as file:
        yaml.dump(config_dict, file)


def create_mysql():
    print('MySQL')


def create_postgresql():
    config_dict: dict[str] = {'Server': {'Server Type': 'PostgreSQL',
                                         'Server Address': 'Address',
                                         'Database Name': 'DB Name',
                                         'Username': 'Username',
                                         'Password': 'Password'}}
    config_dict['Server']['Server Address'] = input('Server Address: ')
    config_dict['Server']['Database Name'] = input('Database Name: ')
    config_dict['Server']['Username'] = input('Username: ')
    config_dict['Server']['Password'] = input('Password: ')

    with open(r'./key.yml', 'w') as file:
        yaml.dump(config_dict, file)


if 'key.yml' in os.listdir(os.getcwd()):
    os.remove(os.getcwd() + '/key.yml')

server_type_dict: dict = {'0': create_sql_server, '1': create_mysql, '2': create_postgresql}
server_type: str = input('Server Type:\n[0] SQL Server\n[1] MYSQL\n[2] PostgreSQL\n: ')
while server_type not in server_type_dict:
    print('ERROR: Not a valid option')
    server_type = input('Server Type:\n[0] SQL Server\n[1] MYSQL\n[2] PostgreSQL\n: ')
server_type_dict[server_type]()
