#1
import pandas as pd

file = 'C:/Users/mishk/Downloads/NISPUF17.csv'


# def proportion_of_education(file):
#     df = pd.read_csv(file, sep = ',')

#     df = df.dropna(subset='EDUC1')

#     children_count = len(df)

#     df['EDUC1'] = df['EDUC1'].replace([1,2,3,4], ['<12','12','>12','colledge graduate'], regex = True)

#     data_1 = df.groupby('EDUC1')['EDUC1'].count()
#     print(data_1)

#     d = {data_1.index[0]: round(float(data_1[0])/children_count,1),
#         data_1.index[1]: round(float(data_1[1])/children_count,1),
#         data_1.index[2]: round(float(data_1[2])/children_count,1),
#         data_1.index[3]: round(float(data_1[3])/children_count,1),
        
#     }
#     print(d)
#     # raise NotImplementedError()
# proportion_of_education(file)

# #2
# def average_influenza_doses(file):
#     df = pd.read_csv(file, sep = ',')
#     df = df.dropna(subset='P_NUMFLU')
#     df['CBF_01'] = df['CBF_01'].replace([1,2], ['yes', 'no'], regex=True)
#     # print(df['CBF_01'].unique())
#     # print(df['P_NUMFLU'].unique())
#     data_1 = df.groupby('CBF_01')['P_NUMFLU'].mean()
#     print(data_1)
#     my_tuple = {
#         round(float(data_1['yes']),1), round(float(data_1['no']),1)
#     }
#     print(my_tuple)

# average_influenza_doses(file)

#3

def vrc(file):
    df = pd.read_csv(file, sep = ',')
    df = df.dropna(subset='HAD_CPOX')
    print(df['P_NUMVRC'].unique())
    print(df['HAD_CPOX'].unique())
vrc(file)
