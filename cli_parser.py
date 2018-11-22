import argparse

parser = argparse.ArgumentParser(description='Replay: a tool to query thermostat data, stored locally.')
parser.add_argument('--field', required=True, type=str, action='append', help='the field you would like to query')
parser.add_argument('path', type=str, help='the path to the file you would like to process')
parser.add_argument('timestamp', type=str, help='the timestamp that you would like to query to')
