import pandas as pd
df = pd.read_csv('output.csv')
tags=['ligand','base','halide','additive']
tagtitles=['additive_*C3_NMR_shift','aryl_halide_*C1_NMR_shift','base_*N1_electrostatic_charge','ligand_*C10_NMR_shift']
for tag in tags:
    df.insert(0,tag,'')
tags.reverse()
# The data was classified into four dimensions
reagents=[]
for tagtitle in tagtitles:
    for i in range(3960):
        if df[tagtitle][i] in reagents:
            df.loc[i:i,tags[tagtitles.index(tagtitle)]]=reagents.index(df[tagtitle][i])
        else:
            reagents.append(df[tagtitle][i])
            df.loc[i:i,tags[tagtitles.index(tagtitle)]]=reagents.index(df[tagtitle][i])
    reagents.clear()

df.to_csv('classified.csv')