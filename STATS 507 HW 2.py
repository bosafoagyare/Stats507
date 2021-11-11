# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---


# Modules for the codes
import math
import numpy as np
import pandas as pd
import scipy.stats as spstat
import statistics as st
import re
import warnings
from timeit import Timer
from collections import defaultdict
from IPython.core.display import display, HTML
from prettytable import PrettyTable
from collections import defaultdict


# # Question 3

# ### (a) NHANES Demographic Dataset

# +
import warnings
warnings.filterwarnings('ignore')
## URLs
url_Dem_11_12 = "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT"
url_Dem_13_14 = "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT"
url_Dem_15_16 = "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT"
url_Dem_17_18 = "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT"

## Read Data
df_Dem_11_12 = pd.read_sas(url_Dem_11_12, format = "xport")
df_Dem_13_14 = pd.read_sas(url_Dem_13_14, format = "xport")
df_Dem_15_16 = pd.read_sas(url_Dem_15_16, format = "xport")
df_Dem_17_18 = pd.read_sas(url_Dem_17_18, format = "xport")



## new names for demo cols
demo_cols = {
    'SEQN': 'id',
    'RIDAGEYR': 'age',
    'RIAGENDR': 'gender',
    'RIDRETH3': 'race',
    'DMDEDUC2': 'education',
    'DMDMARTL': 'marital_status',
    'RIDSTATR': 'exam_status',
    'SDMVPSU': 'psu',
    'SDMVSTRA': 'strata',
    'WTMEC2YR': 'exam_wt',
    'WTINT2YR': 'interview_wt',
    'cohort': 'cohort'
    }

# columns to convert to integer
demo_int = ('id', 'age', 'psu', 'strata')

# levels for categorical variables
demo_cat = {
    'gender': {1: 'Male', 2: 'Female'},
    'race': {1: 'Mexican American',
             2: 'Other Hispanic',
             3: 'Non-Hispanic White',
             4: 'Non-Hispanic Black',
             6: 'Non-Hispanic Asian',
             7: 'Other/Multiracial'
             },
    'education': {1: 'Less than 9th grade',
                  2: '9-11th grade (Includes 12th grade with no diploma)',
                  3: 'High school graduate/GED or equivalent',
                  4: 'Some college or AA degree',
                  5: 'College graduate or above',
                  7: 'Refused',
                  9: "Don't know"
                  },
    'marital_status': {1: 'Married',
                       2: 'Widowed',
                       3: 'Divorced',
                       4: 'Separated',
                       5: 'Never married',
                       6: 'Living with partner',
                       77: 'Refused',
                       99: "Don't know"
                       },
    'exam_status': {1: 'Interviewed only',
                    2: 'Both interviewed and MEC examined'
                    }
    }



## merge data
demo_data = df_Dem_11_12.append([df_Dem_13_14, df_Dem_15_16, df_Dem_17_18],
                          ignore_index=True)

## Create categorical column based on cohort
min_max = {
    "c_11_12": [df_Dem_11_12["SEQN"].min(), df_Dem_11_12["SEQN"].max()],
    "c_13_14": [df_Dem_13_14["SEQN"].min(), df_Dem_13_14["SEQN"].max()],
    "c_15_16": [df_Dem_13_14["SEQN"].min(), df_Dem_13_14["SEQN"].max()],
    "c_17_18": [df_Dem_17_18["SEQN"].min(), df_Dem_17_18["SEQN"].max()]
}

def cohorts(x, metric=min_max):
    if (x["SEQN"] >= metric["c_11_12"][0]) and (x["SEQN"] <= metric["c_11_12"][1]):
        return ("2011-2012")
    elif (x["SEQN"] >= metric["c_13_14"][0]) and (x["SEQN"] <= metric["c_13_14"][1]):
        return ("2013-2014")
    elif (x["SEQN"] >= metric["c_15_16"][0]) and (x["SEQN"] <= metric["c_15_16"][1]):
        return ("2015-2016")
    elif (x["SEQN"] >= metric["c_17_18"][0]) and (x["SEQN"] <= metric["c_17_18"][1]):
        return ("2017-2018")

demo_data["cohort"] = demo_data.apply(cohorts, axis=1)

## Rename columns and change Data types

# (1) Subset needed columns and change data types
demo_data = demo_data[list(demo_cols.keys())].rename(columns=demo_cols)

# (2) categorical variables
for col, d in demo_cat.items():
    demo_data[col] = pd.Categorical(demo_data[col])
    demo_data['cohort'] = pd.Categorical(demo_data['cohort'])

# (3) integer variables
for col in demo_int:
    demo_data[col] = pd.to_numeric(demo_data[col], downcast='integer')

## Save and export to feather format
demo_data.to_feather("demo_data.feather")



#----------------------------------------------------------------------------------------------------------------

#### (b) NHANES Oral Health and Dentition Dataset

# +
## Read Data
df_OxyDen_11_12 = pd.read_sas("OHXDEN_G.XPT", format = "xport")
df_OxyDen_13_14 = pd.read_sas("OHXDEN_H.XPT", format = "xport")
df_OxyDen_15_16 = pd.read_sas("OHXDEN_I.XPT", format = "xport")
df_OxyDen_17_18 = pd.read_sas("OHXDEN_J.XPT", format = "xport")

## Rowbind data and select needed cols
df_Oxy = df_OxyDen_11_12.append([df_OxyDen_13_14, df_OxyDen_15_16, df_OxyDen_17_18],
                                ignore_index=True)
df_OxyDen_cols = list(df_OxyDen_11_12.columns)
r = re.compile("^OHX.*TC")
df_OxyDen_filt_cols = list(filter(r.match, df_OxyDen_cols))
df_OxyDen_filt_cols.extend(["SEQN", "OHDDESTS"])
df_Oxy_1 = df_Oxy[df_OxyDen_filt_cols]

## Drop duplicates by specified columns
df_Oxy_1 = df_Oxy_1.drop_duplicates(df_OxyDen_filt_cols,
                       keep="last").reset_index(drop=True)

## Create categorical column based on cohort
min_max_oxy = {
    "c_11_12": [df_OxyDen_11_12["SEQN"].min(), df_OxyDen_11_12["SEQN"].max()],
    "c_13_14": [df_OxyDen_13_14["SEQN"].min(), df_OxyDen_13_14["SEQN"].max()],
    "c_15_16": [df_OxyDen_15_16["SEQN"].min(), df_OxyDen_15_16["SEQN"].max()],
    "c_17_18": [df_OxyDen_17_18["SEQN"].min(), df_OxyDen_17_18["SEQN"].max()]
}


def cohorts_oxy(x, metric=min_max_oxy):
    if (x["SEQN"] >= metric["c_11_12"][0]) and (x["SEQN"] <= metric["c_11_12"][1]):
        return ("2011-2012")
    elif (x["SEQN"] >= metric["c_13_14"][0]) and (x["SEQN"] <= metric["c_13_14"][1]):
        return ("2013-2014")
    elif (x["SEQN"] >= metric["c_15_16"][0]) and (x["SEQN"] <= metric["c_15_16"][1]):
        return ("2015-2016")
    elif (x["SEQN"] >= metric["c_17_18"][0]) and (x["SEQN"] <= metric["c_17_18"][1]):
        return ("2017-2018")


df_Oxy_1["cohort"] = df_Oxy_1.apply(cohorts_oxy, axis=1)

## Export to feather format
df_Oxy_1.to_feather('NHANES_oral_dentist_data_Y11_Y18.feather')

# -


#----------------------------------------------------------------------------------
# (c) Number of cases in the datasets

# +
demo = "Number of cases in the demographic dataset is: "
oral = "Number of cases in the oral health and dentition dataset is: "

print(demo + str(df4.shape[0]))
print(oral + str(df_Oxy_1.shape[0]))
# -
