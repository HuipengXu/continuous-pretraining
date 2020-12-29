import os
import random

from tqdm import tqdm
import pandas as pd


def main():
    total_files = [file for file in os.listdir() if file.endswith('.csv')]
    with open('../multi-task-data/input.txt', 'w', encoding='utf8') as f:
        for file in tqdm(total_files, total=len(total_files), desc='Iterate files'):
            df = pd.read_csv(file, header=None, sep='\t')
            for _, row in tqdm(df.iterrows(), total=len(df), desc=f'Iterate {file}'):
                text = row[1]
                if 'NLI' in file:
                    text += row[2]
                f.write(text)
                f.write('\n')
    with open('../multi-task-data/input.txt', 'r', encoding='utf8') as f:
        texts = f.readlines()
        random.shuffle(texts)
        train_input = texts[5000:]
        dev_input = texts[:5000]

    with open('../multi-task-data/train_input.txt', 'w', encoding='utf8') as f:
        f.write(''.join(train_input))
    with open('../multi-task-data/dev_input.txt', 'w', encoding='utf8') as f:
        f.write(''.join(dev_input))

    with open('../multi-task-data/debug_train_input.txt', 'w', encoding='utf8') as f0:
        with open('../multi-task-data/train_input.txt', 'r', encoding='utf8') as f:
            texts = f.readlines()
            random.shuffle(texts)
            debug_train_input = texts[:500]
        f0.write(''.join(debug_train_input))

    with open('../multi-task-data/debug_dev_input.txt', 'w', encoding='utf8') as f0:
        with open('../multi-task-data/dev_input.txt', 'r', encoding='utf8') as f:
            texts = f.readlines()
            random.shuffle(texts)
            debug_dev_input = texts[:100]
        f0.write(''.join(debug_dev_input))


if __name__ == '__main__':
    main()
