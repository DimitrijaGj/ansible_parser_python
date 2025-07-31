# import pandas as pd

# df1 = pd.read_csv('server_inventory_report.csv')
# df2 = pd.read_csv('server_inventory_report_old.csv')

# diff = pd.concat([df1, df2]).drop_duplicates(keep=False)

# print(diff)
# diff.to_csv('differences.csv', index=False)

import pandas as pd

df1 = pd.read_csv('server_inventory_report.csv')
df2 = pd.read_csv('server_inventory_report_old.csv')

key_col = 'servername'  # change to your key column

merged = df1.merge(df2, on=key_col, how='inner', suffixes=('_old', '_new'))

# Identify columns to compare (all except key)
cols_to_compare = [col for col in df1.columns if col != key_col]

# Create boolean DataFrame: True where different
diff_mask = (merged[[col + '_old' for col in cols_to_compare]].values !=
             merged[[col + '_new' for col in cols_to_compare]].values)

# Get rows where any column differs
changed_rows = merged[diff_mask.any(axis=1)]

print(changed_rows)
changed_rows.to_csv('different_rows.csv', index=False)