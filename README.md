# make qa reduced dataset

`version 2.3`

`author: yghuang`

### Totally New Version!

Better structure and do not need to specify run numbers!

Just use STAR-submit to submit the jobs and get the QAtree, and merge them directly with hadd!

Revision: 2.3 on 21.06.2023 by yghuang

### Introcution

1. Modify settings in `conf.py` and run `python3 MakeDbConf.py`.

2. Using `./prepare.sh PATH` and `star-submit -u ie Csubmit.xml` to submit the jobs.

3. Will create the reduced qa histograms, and all the qa processes can be done based on this. 

### Change log

2023 June 23 by yghuang (2.3):

> New version. With some bugs fixed.

2022 May 19 by yghuang (1.2):

> Reimplement

2022 Feb. 28 by yghuang (1.1.Alter):

> Alter: based on the official bad runs, we only need to check some variables about proton, and the DCAxy issue.

2021 October 12 by yghuang (1.1):

> Update: Using allocate jobs system to submit jobs instead of star-submit. (due to the lack of run number information if using the previous star-submit version.)

2021 October 11 by yghuang (1.0):

> A release version.
