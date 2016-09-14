
# Bootcamp Lesson 32

# Practice 1a
df.loc[df['adhesive strength (Pa)'] <= -2000, ['impact time (ms)', 'ad
     ...: hesive strength (Pa)']]

# Practice 1b
df.loc[df['ID'] == 'II', ['impact force (mN)', 'adhesive force (mN)']]

# Practice 1c
df.loc[df['ID'].isin(['III', 'IV']), ['time frog pulls on target (ms)', 'adhesive force (mN)', 'ID']]


# Practice 2a
