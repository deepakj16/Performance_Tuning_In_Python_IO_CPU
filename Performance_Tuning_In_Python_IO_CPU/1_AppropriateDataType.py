from Python_Classics import Pandas as pd
import numpy as np
moma=pd.read_csv("D:\Python\DE_Path\Data\MoMAExhibitions1929to1989.csv")

#To know size
print(moma[:5])
print(moma.info())
print(moma._data)
#To know data type blocks
#float & object would consume atleast  8 bytes of memory



#Estimate ~ 7.1MB

print(moma.size) # 28 columns * 34558 rows = 933066
total_bytes = moma.size*8  # size of each column
total_mega_bytes = total_bytes / (1024*1024)   # to convert bytes to MB
print('The etsimated dataframe size in MB is ' + str(total_mega_bytes))
#print('The etsimated dataframe size in MB is ' + str(moma.size*8/(1024*1024)))


#Actual ~ 45.6

print(moma.info(memory_usage="deep"))
#print(moma.memory_usage(deep=True)) #for each column


#Actual for Object data type

obj_cols = moma.select_dtypes(include=['object'])
obj_cols_mem = obj_cols.memory_usage(deep=True)
obj_cols_sum = obj_cols_mem.sum()/(1024*1024)
print(obj_cols_sum)


#Actual for Object float type

float_cols = moma.select_dtypes(include=['float'])
float_cols_mem = float_cols.memory_usage(deep=True)
float_cols_sum = float_cols_mem.sum()/(1024*1024)
print(float_cols_sum)



#Reducing the size
#Conversion from float64 to int16

col_max = moma['ExhibitionSortOrder'].max()
col_min = moma['ExhibitionSortOrder'].min()
print("Size in Bytes for ExhibitionSortOrder before change: ")
print(moma['ExhibitionSortOrder'].memory_usage(deep=True))
if col_max <  np.iinfo("int8").max and col_min > np.iinfo("int8").min:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int8")
elif col_max <  np.iinfo("int16").max and col_min > np.iinfo("int16").min:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int16")
elif col_max <  np.iinfo("int32").max and col_min > np.iinfo("int32").min:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int32")
elif col_max <  np.iinfo("int64").max and col_min > np.iinfo("int64").min:
    moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int64")
print(moma['ExhibitionSortOrder'].dtype)
print("Size in Bytes for ExhibitionSortOrder after change: ")
print(moma['ExhibitionSortOrder'].memory_usage(deep=True))


#Conversion from float64 to lower dtypes for all float columns

float_cols = moma.select_dtypes(include=['float32','float64'])
#print(float_cols.dtypes)
print("Size in Bytes for all float columns before change: ")
print(moma.select_dtypes(include=['float']).memory_usage(deep=True).sum())
for col in float_cols.columns:
    moma[col] = pd.to_numeric(moma[col], downcast='float')
print("Size in Bytes for all float columns after change: ")
print(moma.select_dtypes(include=['float32','float64']).memory_usage(deep=True).sum())
#print(moma.select_dtypes(include=['float32','float64']).dtypes)
#Converting object to datetime

print(moma[["ExhibitionBeginDate", "ExhibitionEndDate"]].memory_usage(deep=True))
moma["ExhibitionBeginDate"] = pd.to_datetime(moma["ExhibitionBeginDate"])
moma["ExhibitionEndDate"] = pd.to_datetime(moma["ExhibitionEndDate"])
print(moma[["ExhibitionBeginDate", "ExhibitionEndDate"]].memory_usage(deep=True))



#Converting from Object to Category

print("Size in Bytes for ConstituentType before change: ")
print(moma['ConstituentType'].memory_usage(deep=True))
moma['ConstituentType'] = moma['ConstituentType'].astype('category')
print("Size in Bytes for ConstituentType after change: ")
print(moma['ConstituentType'].memory_usage(deep=True))
#print(moma['ConstituentType'].cat.codes)


#Converting from Object to Category for all objects which has 50% of unique values

obj_cols = moma.select_dtypes(include=['object'])
print("Size in Bytes for all object columns before change: ")
print(moma.select_dtypes(include=['object']).memory_usage(deep=True).sum())
for col in obj_cols.columns:
    num_unique_values = len(moma[col].unique())
    num_total_values = len(moma[col])
    if num_unique_values / num_total_values < 0.5:
        moma[col] = moma[col].astype('category')
        #print(col)
print("Size in Bytes for all object columns after change: ")
print(moma.select_dtypes(include=['object','category']).memory_usage(deep=True).sum())
print(moma.info(memory_usage='deep'))



#Selecting only Required columns
'''
keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']
moma=pd.read_csv("D:\Python\DE_Path\Data\MoMAExhibitions1929to1989.csv", parse_dates=["ExhibitionBeginDate", "ExhibitionEndDate"], usecols=keep_cols)

print(moma.memory_usage(deep="True").sum()/(1024*1024))

num_rows = 0
chunk_iter = pd.read_csv("D:\Python\DE_Path\Data\MoMAExhibitions1929to1989.csv", chunksize=1000)
for chunk in chunk_iter:
    num_rows= num_rows + len(chunk)
print(num_rows)
'''