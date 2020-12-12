import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, required=True, help='input file path')
parser.add_argument('-o', '--output', type=str, required=True, help='output file path')
args = parser.parse_args()

input_file = args.input
output_file = args.output

# json to csv
if '.json' in input_file and '.csv' in output_file:
    print('Converting ' + input_file + ' to ' + output_file + ' ...')
    df = pd.read_json(input_file)
    df.to_csv(output_file, encoding='utf-8')
    print('Success!!')

# csv to json
elif '.csv' in input_file and '.json' in output_file:
    print('Converting ' + input_file + ' to ' + output_file + ' ...')
    df = pd.read_csv(input_file, encoding='utf-8')
    json = df.to_json(output_file, orient="records")
    print('Success!!')

else:
    print('Check the extension of the input and output files.')
