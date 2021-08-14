import pandas as pd
from datetime import datetime
import numpy as np


start = datetime.now()
print("Downloading data for Season 2020")
Season_2020 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/2021/D1.csv")
print("Downloading data for Season 2020 completed successfully")
#Season_2020_c = pd.concat(Season_2020, axis=0, ignore_index=True)
print("Downloading data for Season 2019")
Season_2019 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1920/D1.csv")
print("Downloading data for Season 2019 completed successfully")
#Season_2019_c = pd.concat(Season_2019, axis=0, ignore_index=True)
print("Downloading data for Season 2018")
Season_2018 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1819/D1.csv")
print("Downloading data for Season 2018 completed successfully")
#Season_2018_c = pd.concat(Season_2018, axis=0, ignore_index=True)
print("Downloading data for Season 2017")
Season_2017 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1718/D1.csv")
#Season_2017_c = pd.concat(Season_2017, axis=0, ignore_index=True)
print("Downloading data for Season 2016")
Season_2016 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1617/D1.csv")
#Season_2016_c = pd.concat(Season_2016, axis=0, ignore_index=True)
print("Downloading data for Season 2015")
Season_2015 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1516/D1.csv")
#Season_2015_c = pd.concat(Season_2015, axis=0, ignore_index=True)
print("Downloading data for Season 2014")
Season_2014 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1415/D1.csv")
#Season_2014_c = pd.concat(Season_2014, axis=0, ignore_index=True)
print("Downloading data for Season 2013")
Season_2013 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1314/D1.csv")
#Season_2013_c = pd.concat(Season_2013, axis=0, ignore_index=True)
print("Downloading data for Season 2012")
Season_2012 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1213/D1.csv")
#Season_2012_c = pd.concat(Season_2012, axis=0, ignore_index=True)
print("Downloading data for Season 2011")
Season_2011 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1112/D1.csv")
#Season_2011_c = pd.concat(Season_2011, axis=0, ignore_index=True)
print("Downloading data for Season 2010")
Season_2010 = pd.read_csv(r"https://www.football-data.co.uk/mmz4281/1011/D1.csv")
#Season_2010_c = pd.concat(Season_2010, axis=0, ignore_index=True)

print("Defining list of all seasons")
Season_list = [
               Season_2020,
               Season_2019,
               Season_2018,
               Season_2017,
               Season_2016,
               Season_2015,
               Season_2014,
               Season_2013,
               Season_2012,
               Season_2011,
               Season_2010,
               ]
print("Concatenating all data into one dataframe")
db_concat = pd.concat(Season_list)
print("Saving csv")
db_concat.to_csv(r'data/data_raw.csv', index = False)
print("File Saved")
print("Success")
end = datetime.now()
time_taken = end - start
print('Time taken to complete: ', time_taken)