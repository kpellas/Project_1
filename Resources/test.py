
# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
raw_data = pd.read_csv(file_one, encoding="ISO-8859-1",low_memory=False)
raw_data.head()
