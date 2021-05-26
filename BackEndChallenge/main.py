import pandas as pd
import DataProcess as dp
import os.path as path

def main(name):
    file = input(f'Hello {name}, please enter the file path : \n')

    if path.exists(file):
        df = pd.read_excel(file)
        data_processor = dp.DataProcessor(df)

        print(data_processor.get_json())

if __name__ == '__main__':
    main('Femme Palette')