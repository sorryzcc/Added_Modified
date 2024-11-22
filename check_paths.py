import pandas as pd
df = pd.read_excel('updated_processed_svn_log.xlsx')    
# print(df['Path'])
    
prefix1 = r'I:\PM_Mainland_Trunk_20230321_r552586\PMGameClient\PMGame/CDNRes/Dev_CDNUpload'
prefix2 = r'I:\PM_Mainland_Trunk_20230321_r552586\PMGameClient\PMGame/CDNRes/Dev'

paths_with_prefix1 = df[df['Path'].str.startswith(prefix1, na=False)]['Path']

paths_with_prefix2 = df[df['Path'].str.startswith(prefix2, na=False)]['Path']

print(paths_with_prefix1.len)