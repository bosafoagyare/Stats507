# Stats507  

This is a Repo for STATS 507 Fall 2021. It contains a file called ![STATS 507 HW 2.py](./STATS 507 HW 2.py) which reads and cleans several data files from the National Health and Nutrition Examination Survey ![NHANES](https://www.cdc.gov/nchs/nhanes/index.htm).  
Specifically, data from four (4) cohorts spanning the years 2011 through 2018 are imported and cleaned. The links to the various cohorts can be found ![here](https://wwwn.cdc.gov/nchs/nhanes/Default.aspx).  

The following analyses are implemented in the `STATS 507 HW 2.py`:
+ The demographic datasets are read and columns namely SEQN, RIDAGEYR, RIDRETH3, DMDEDUC2, DMDMARTL, RIDSTATR, SDMVPSU, SDMVSTRA, WTMEC2YR, WTINT2YR are extracted as well as a new `cohort` column added to help identify which cohort each case belongs. The various columns are given appropriated names and data types and then finally saved and exported as `.feather` format
+ This process is repeated for the oral health and dentition data, where the columns extracted in this case are: SEQN, OHDDESTS, tooth counts (OHXxxTC), and coronal cavities (OHXxxCTC)
+ Finally, the number of cases are reported for both datasets
