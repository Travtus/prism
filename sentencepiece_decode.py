import pandas as pd
import os
import sentencepiece as spm

from collections import defaultdict

with open('paraphrases_5.txt','r') as paraphrased:
    doc = paraphrased.read()

ref2paraphrase = {}

bundles = doc.split('\nS')

for bundle in bundles:
    lines = bundle.split('\n')
    reference = lines[0][lines[0].find('▁'):]
    hypotheses = [line[line.find('▁'):] for line in lines if line[0]=='H']
    reference_decoded = ''.join(reference.split()).replace('▁',' ')
    hypothesis_decoded = [''.join(hypothesis.split()).replace('▁',' ') for hypothesis in hypotheses]
    ref2paraphrase[reference_decoded]=hypothesis_decoded

for i, (ref, paras) in enumerate(ref2paraphrase.items()):
    print(ref, paras)
    # exit()
    csv = pd.DataFrame(data={ref: paras})
    csv.to_csv(f'paraphrased/sentence_{i}_paraphrased.csv', index=False)
