# import  libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# get dataset
columns = ["square_id", "time_interval", "country_code", "sms_in", "sms_out", "call_in", "call_out", "internet_traffic"]

df = pd.read_csv("data/sms-call-internet-mi-2013-12-21.txt", sep="\t", names=columns)


def country_code_mapping(x):
    return 0 if x in [0, 39] else 1


df["country_code"] = df["country_code"].apply(country_code_mapping)

grouped_ds = (
    df.groupby(["square_id", "time_interval", "country_code"])
    .agg({"sms_in": "sum", "sms_out": "sum", "call_in": "sum", "call_out": "sum", "internet_traffic": "sum"})
    .reset_index()
)
# Merge the country codes

# Merge the sms-in and sms-out
# join sms_out and sms_in to sms_activities
df["cell_activities"] = df["sms_out"] + df["sms_in"] + df["call_in"] + df["call_out"] + df["internet_traffic"]
print(df)


# Categorical encode
# Encoding categorical data
labelencoder_X = LabelEncoder()
df[:, 2] = labelencoder_X.fit_transform(df[:, 2])


def checkPrint(_self):
    print("hello I am human")
