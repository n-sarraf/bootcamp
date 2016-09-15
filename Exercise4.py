import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set()

# Load data
g_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
g_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
g_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
g_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
g_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

# Rename existing columns
g_1973 = g_1973.rename(columns = {'yearband':'year', 'beak length':'beak length (mm)', 'beak depth':'beak depth (mm)'})
g_1975 = g_1975.rename(columns = {'Beak length, mm':'beak length (mm)', 'Beak depth, mm':'beak depth (mm)'})
g_1987 = g_1987.rename(columns = {'Beak length, mm':'beak length (mm)', 'Beak depth, mm':'beak depth (mm)'})
g_1991 = g_1991.rename(columns = {'blength':'beak length (mm)', 'bdepth':'beak depth (mm)'})
g_2012 = g_2012.rename(columns = {'blength':'beak length (mm)', 'bdepth':'beak depth (mm)'})

# Add / modify year column
g_1973['year'] = '1973'
g_1975['year'] = '1975'
g_1987['year'] = '1987'
g_1991['year'] = '1991'
g_2012['year'] = '2012'

# Concatenate data from all years
finch_data = pd.concat((g_1973, g_1975, g_1987, g_1991, g_2012), ignore_index=True)

# Drop duplicate birds from same year
finch_data = finch_data.drop_duplicates(subset={'band', 'year'})

# Write file to csv
# finch_data.to_csv('finch_data.csv', index=False)


def bd_bl_data(data, year_number):
    '''
    Slice out beak depth and beak length data for both species for a given year.
    '''

    bd_f_data = data.loc[(data['year'] == year_number) & (data['species'] == 'fortis'), 'beak depth (mm)']
    bl_f_data = data.loc[(data['year'] == year_number) & (data['species'] == 'fortis'), 'beak length (mm)']
    bd_s_data = data.loc[(data['year'] == year_number) & (data['species'] == 'scandens'), 'beak depth (mm)']
    bl_s_data = data.loc[(data['year'] == year_number) & (data['species'] == 'scandens'), 'beak length (mm)']

    return bd_f_data, bl_f_data, bd_s_data, bl_s_data


def plot_bd_bl(bd_f_y, bl_f_y, bd_s_y, bl_s_y, year):
    '''
    Plot beak depth vs beak length data.
    bd_f_y: beak depth, fortis
    bl_f_y: beak length, fortis
    bd_s_y: beak depth, scandens
    bl_s_y: beak length, scandens
    '''

    plt.plot(bd_s_y, bl_s_y, 'r.')
    plt.plot(bd_f_y, bl_f_y, 'b.')
    plt.legend(['scandens', 'fortis'], loc='lower right')
    plt.title('Beak Depth vs. Beak Length ' + year)
    plt.xlabel('beak depth (mm)')
    plt.ylabel('beak length (mm)')
    plt.xlim([6, 13])
    plt.show()
    plt.close()


# Slice out beak depth data, fortis and scandens, 1987
bd_fortis_87, bl_fortis_87, bd_scandens_87, bl_scandens_87 = bd_bl_data(finch_data, '1987')

# Plot beak depth data as ecdf
bd_fortis_x, bd_fortis_y = bootcamp_utils.ecdf(bd_fortis_87)
bd_scandens_x, bd_scandens_y = bootcamp_utils.ecdf(bd_scandens_87)
plt.plot(bd_fortis_x, bd_fortis_y)
plt.plot(bd_scandens_x, bd_scandens_y)
plt.legend(['fortis', 'scandens'], loc='lower right')
plt.title('Beak Depth, 1987')
plt.xlabel('beak depth (mm)')
plt.ylabel('ecdf')
plt.show()

plt.close()


# Plot beak length data as ecdf
bl_fortis_x, bl_fortis_y = bootcamp_utils.ecdf(bl_fortis_87)
bl_scandens_x, bl_scandens_y = bootcamp_utils.ecdf(bl_scandens_87)
plt.plot(bl_fortis_x, bl_fortis_y)
plt.plot(bl_scandens_x, bl_scandens_y)
plt.legend(['fortis', 'scandens'], loc='lower right')
plt.title('Beak Length, 1987')
plt.xlabel('beak length (mm)')
plt.ylabel('ecdf')
plt.show()

plt.close()

# Slice out beak depth and beak length data for all years
bd_fortis_73, bl_fortis_73, bd_scandens_73, bl_scandens_73 = bd_bl_data(finch_data, '1973')
bd_fortis_75, bl_fortis_75, bd_scandens_75, bl_scandens_75 = bd_bl_data(finch_data, '1975')
bd_fortis_91, bl_fortis_91, bd_scandens_91, bl_scandens_91 = bd_bl_data(finch_data, '1991')
bd_fortis_12, bl_fortis_12, bd_scandens_12, bl_scandens_12 = bd_bl_data(finch_data, '2012')

# Plot of beak depth vs. beak length, 1973
plot_bd_bl(bd_fortis_73, bl_fortis_73, bd_scandens_73, bl_scandens_73, '1973')

# Plot of beak depth vs. beak length, 1975
plot_bd_bl(bd_fortis_75, bl_fortis_75, bd_scandens_75, bl_scandens_75, '1975')

# Plot of beak depth vs. beak length, 1987
plot_bd_bl(bd_fortis_87, bl_fortis_87, bd_scandens_87, bl_scandens_87, '1987')

# Plot of beak depth vs. beak length, 1991
plot_bd_bl(bd_fortis_91, bl_fortis_91, bd_scandens_91, bl_scandens_91, '1991')

# Plot of beak depth vs. beak length, 2012
plot_bd_bl(bd_fortis_12, bl_fortis_12, bd_scandens_12, bl_scandens_12, '2012')
