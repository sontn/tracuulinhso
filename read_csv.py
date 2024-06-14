import pandas as pd

from check_phone_number_array import tam_mot_linh_so_func

file_path = '/home/ws0561/Downloads/DuongDz_3.csv'

df = pd.read_csv(file_path, header=None, names=['PhoneNumber'])

for number in df['PhoneNumber']:
    tam_mot_linh_so_func(str(number))