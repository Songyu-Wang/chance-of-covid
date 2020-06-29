# What are the chance of encountering people with COVID if I go out today?
I do not know, but I would like to know

## Basic idea
Calculate the percentage of people may have COVID today in state population

### How can I find out how many people may have COVID today?
Please note this is an over simplified educated guess. Do not over interpret the result 
1. Using API https://covidtracking.com/ to get new case increase counts for the last 14 days for each state
2. Find the maximum increase count in the past 14 days
3. `Max value * 14 * 2` (This is by no means accurate. Too many factors are involved. I hope this is a conservative educated guess by using max value and `* 2` as fault tolerance mitigators ) 

### How can I find out population in each state?
https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html

## Note
This project is under MIT license. I created it for personal reference. Feel free to do whatever you want with it. However, I am not responsible for any outcome regardless how you use or not use those data 

## Result

 Updated at: 2020-06-29T12:12:49.494699+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 0.65215%                                                          | 6.52148%                                                           | 65.21475%                                                           |                                                 1142 |                               31976 |
| Alaska               | 0.11100%                                                          | 1.10998%                                                           | 11.09980%                                                           |                                                   29 |                                 812 |
| Arizona              | 1.48372%                                                          | 14.83723%                                                          | 148.37230%                                                          |                                                 3857 |                              107996 |
| Arkansas             | 0.87309%                                                          | 8.73085%                                                           | 87.30852%                                                           |                                                  941 |                               26348 |
| California           | 0.50661%                                                          | 5.06608%                                                           | 50.66078%                                                           |                                                 7149 |                              200172 |
| Colorado             | 0.15753%                                                          | 1.57535%                                                           | 15.75346%                                                           |                                                  324 |                                9072 |
| Connecticut          | 0.12409%                                                          | 1.24085%                                                           | 12.40854%                                                           |                                                  158 |                                4424 |
| Delaware             | 0.38818%                                                          | 3.88184%                                                           | 38.81844%                                                           |                                                  135 |                                3780 |
| Florida              | 1.24957%                                                          | 12.49573%                                                          | 124.95730%                                                          |                                                 9585 |                              268380 |
| Georgia              | 0.58677%                                                          | 5.86771%                                                           | 58.67714%                                                           |                                                 2225 |                               62300 |
| Hawaii               | 0.05339%                                                          | 0.53395%                                                           | 5.33947%                                                            |                                                   27 |                                 756 |
| Idaho                | 0.44341%                                                          | 4.43409%                                                           | 44.34086%                                                           |                                                  283 |                                7924 |
| Illinois             | 0.20108%                                                          | 2.01076%                                                           | 20.10761%                                                           |                                                  910 |                               25480 |
| Indiana              | 0.21669%                                                          | 2.16689%                                                           | 21.66893%                                                           |                                                  521 |                               14588 |
| Iowa                 | 0.43663%                                                          | 4.36631%                                                           | 43.66306%                                                           |                                                  492 |                               13776 |
| Kansas               | 0.54591%                                                          | 5.45908%                                                           | 54.59075%                                                           |                                                  568 |                               15904 |
| Kentucky             | 0.23377%                                                          | 2.33768%                                                           | 23.37682%                                                           |                                                  373 |                               10444 |
| Louisiana            | 0.88358%                                                          | 8.83584%                                                           | 88.35840%                                                           |                                                 1467 |                               41076 |
| Maine                | 0.11040%                                                          | 1.10399%                                                           | 11.03993%                                                           |                                                   53 |                                1484 |
| Maryland             | 0.25936%                                                          | 2.59359%                                                           | 25.93587%                                                           |                                                  560 |                               15680 |
| Massachusetts        | 0.15153%                                                          | 1.51527%                                                           | 15.15270%                                                           |                                                  373 |                               10444 |
| Michigan             | 0.12561%                                                          | 1.25605%                                                           | 12.56051%                                                           |                                                  448 |                               12544 |
| Minnesota            | 0.25619%                                                          | 2.56187%                                                           | 25.61869%                                                           |                                                  516 |                               14448 |
| Mississippi          | 1.54858%                                                          | 15.48578%                                                          | 154.85784%                                                          |                                                 1646 |                               46088 |
| Missouri             | 0.33076%                                                          | 3.30757%                                                           | 33.07574%                                                           |                                                  725 |                               20300 |
| Montana              | 0.09693%                                                          | 0.96933%                                                           | 9.69331%                                                            |                                                   37 |                                1036 |
| Nebraska             | 0.36332%                                                          | 3.63315%                                                           | 36.33153%                                                           |                                                  251 |                                7028 |
| Nevada               | 0.99904%                                                          | 9.99040%                                                           | 99.90403%                                                           |                                                 1099 |                               30772 |
| New Hampshire        | 0.15033%                                                          | 1.50326%                                                           | 15.03261%                                                           |                                                   73 |                                2044 |
| New Jersey           | 0.12736%                                                          | 1.27356%                                                           | 12.73560%                                                           |                                                  404 |                               11312 |
| New Mexico           | 0.40728%                                                          | 4.07282%                                                           | 40.72817%                                                           |                                                  305 |                                8540 |
| New York             | 0.11587%                                                          | 1.15866%                                                           | 11.58657%                                                           |                                                  805 |                               22540 |
| North Carolina       | 0.45945%                                                          | 4.59455%                                                           | 45.94547%                                                           |                                                 1721 |                               48188 |
| North Dakota         | 0.15432%                                                          | 1.54318%                                                           | 15.43182%                                                           |                                                   42 |                                1176 |
| Ohio                 | 0.23643%                                                          | 2.36425%                                                           | 23.64254%                                                           |                                                  987 |                               27636 |
| Oklahoma             | 0.34107%                                                          | 3.41069%                                                           | 34.10690%                                                           |                                                  482 |                               13496 |
| Oregon               | 0.34720%                                                          | 3.47200%                                                           | 34.72004%                                                           |                                                  523 |                               14644 |
| Pennsylvania         | 0.24627%                                                          | 2.46274%                                                           | 24.62742%                                                           |                                                 1126 |                               31528 |
| Rhode Island         | 0.38589%                                                          | 3.85893%                                                           | 38.58930%                                                           |                                                  146 |                                4088 |
| South Carolina       | 0.87230%                                                          | 8.72295%                                                           | 87.22955%                                                           |                                                 1604 |                               44912 |
| South Dakota         | 0.28802%                                                          | 2.88021%                                                           | 28.80206%                                                           |                                                   91 |                                2548 |
| Tennessee            | 0.57811%                                                          | 5.78108%                                                           | 57.81080%                                                           |                                                 1410 |                               39480 |
| Texas                | 0.57901%                                                          | 5.79006%                                                           | 57.90064%                                                           |                                                 5996 |                              167888 |
| Utah                 | 0.59040%                                                          | 5.90401%                                                           | 59.04007%                                                           |                                                  676 |                               18928 |
| Vermont              | 0.08975%                                                          | 0.89745%                                                           | 8.97452%                                                            |                                                   20 |                                 560 |
| Virginia             | 0.22208%                                                          | 2.22084%                                                           | 22.20837%                                                           |                                                  677 |                               18956 |
| Washington           | 0.20187%                                                          | 2.01868%                                                           | 20.18676%                                                           |                                                  549 |                               15372 |
| West Virginia        | 0.08906%                                                          | 0.89055%                                                           | 8.90552%                                                            |                                                   57 |                                1596 |
| Wisconsin            | 0.27075%                                                          | 2.70746%                                                           | 27.07459%                                                           |                                                  563 |                               15764 |
| Wyoming              | 0.22738%                                                          | 2.27383%                                                           | 22.73831%                                                           |                                                   47 |                                1316 |
| Puerto Rico          | 0.23496%                                                          | 2.34963%                                                           | 23.49630%                                                           |                                                  268 |                                7504 |
| District of Columbia | 0.22218%                                                          | 2.22175%                                                           | 22.21753%                                                           |                                                   56 |                                1568 |