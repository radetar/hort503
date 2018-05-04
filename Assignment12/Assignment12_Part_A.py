import re
import pandas as pd
from io import StringIO

text = pd.read_csv("TAIR10_functional_descriptions.txt", sep="/t")

results = re.sub('.*?(^AT\dG\d+\.\d+|IPR\d+|$).*?’,r'\1,',text, 0, re.M)
results_io = StringIO(results)
df = pd.read_csv(results_io, sep=",", header=None)
df.columns = ['Transcript ID','IPR1', 'IPR2’,'IPR3', 'IPR4', 'IPR5', 'IPR6', 'IPR7’]

annots = df.melt(id_vars = 'Transcript ID’,value_name='IPR Term')
annots = annots.drop('variable', axis=1)
annots = annots.dropna()

