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

 Updated at: 2020-10-13T12:26:24.795590+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 0.96052%                                                          | 9.60519%                                                           | 96.05185%                                                           |                                                 1682 |                               47096 |
| Alaska               | 1.04874%                                                          | 10.48739%                                                          | 104.87393%                                                          |                                                  274 |                                7672 |
| Arizona              | 0.34391%                                                          | 3.43907%                                                           | 34.39068%                                                           |                                                  894 |                               25032 |
| Arkansas             | 1.92524%                                                          | 19.25241%                                                          | 192.52410%                                                          |                                                 2075 |                               58100 |
| California           | 0.30422%                                                          | 3.04220%                                                           | 30.42198%                                                           |                                                 4293 |                              120204 |
| Colorado             | 0.49740%                                                          | 4.97401%                                                           | 49.74008%                                                           |                                                 1023 |                               28644 |
| Connecticut          | 1.05158%                                                          | 10.51584%                                                          | 105.15843%                                                          |                                                 1339 |                               37492 |
| Delaware             | 0.54058%                                                          | 5.40583%                                                           | 54.05827%                                                           |                                                  188 |                                5264 |
| Florida              | 0.72615%                                                          | 7.26147%                                                           | 72.61473%                                                           |                                                 5570 |                              155960 |
| Georgia              | 0.45359%                                                          | 4.53594%                                                           | 45.35941%                                                           |                                                 1720 |                               48160 |
| Hawaii               | 0.32630%                                                          | 3.26301%                                                           | 32.63007%                                                           |                                                  165 |                                4620 |
| Idaho                | 1.06073%                                                          | 10.60734%                                                          | 106.07337%                                                          |                                                  677 |                               18956 |
| Illinois             | 0.68874%                                                          | 6.88741%                                                           | 68.87408%                                                           |                                                 3117 |                               87276 |
| Indiana              | 0.79772%                                                          | 7.97716%                                                           | 79.77162%                                                           |                                                 1918 |                               53704 |
| Iowa                 | 1.11909%                                                          | 11.19088%                                                          | 111.90877%                                                          |                                                 1261 |                               35308 |
| Kansas               | 1.97507%                                                          | 19.75070%                                                          | 197.50703%                                                          |                                                 2055 |                               57540 |
| Kentucky             | 1.49975%                                                          | 14.99752%                                                          | 149.97517%                                                          |                                                 2393 |                               67004 |
| Louisiana            | 1.29857%                                                          | 12.98573%                                                          | 129.85734%                                                          |                                                 2156 |                               60368 |
| Maine                | 0.11248%                                                          | 1.12482%                                                           | 11.24823%                                                           |                                                   54 |                                1512 |
| Maryland             | 0.36357%                                                          | 3.63565%                                                           | 36.35654%                                                           |                                                  785 |                               21980 |
| Massachusetts        | 0.31077%                                                          | 3.10772%                                                           | 31.07724%                                                           |                                                  765 |                               21420 |
| Michigan             | 0.54167%                                                          | 5.41672%                                                           | 54.16719%                                                           |                                                 1932 |                               54096 |
| Minnesota            | 0.75267%                                                          | 7.52673%                                                           | 75.26732%                                                           |                                                 1516 |                               42448 |
| Mississippi          | 1.44697%                                                          | 14.46971%                                                          | 144.69706%                                                          |                                                 1538 |                               43064 |
| Missouri             | 2.31120%                                                          | 23.11196%                                                          | 231.11962%                                                          |                                                 5066 |                              141848 |
| Montana              | 1.89151%                                                          | 18.91506%                                                          | 189.15060%                                                          |                                                  722 |                               20216 |
| Nebraska             | 1.57051%                                                          | 15.70506%                                                          | 157.05063%                                                          |                                                 1085 |                               30380 |
| Nevada               | 0.73269%                                                          | 7.32690%                                                           | 73.26902%                                                           |                                                  806 |                               22568 |
| New Hampshire        | 0.44686%                                                          | 4.46860%                                                           | 44.68597%                                                           |                                                  217 |                                6076 |
| New Jersey           | 0.40918%                                                          | 4.09178%                                                           | 40.91784%                                                           |                                                 1298 |                               36344 |
| New Mexico           | 0.64764%                                                          | 6.47645%                                                           | 64.76446%                                                           |                                                  485 |                               13580 |
| New York             | 0.26426%                                                          | 2.64260%                                                           | 26.42601%                                                           |                                                 1836 |                               51408 |
| North Carolina       | 0.64820%                                                          | 6.48202%                                                           | 64.82023%                                                           |                                                 2428 |                               67984 |
| North Dakota         | 2.41030%                                                          | 24.10303%                                                          | 241.03026%                                                          |                                                  656 |                               18368 |
| Ohio                 | 0.44075%                                                          | 4.40752%                                                           | 44.07525%                                                           |                                                 1840 |                               51520 |
| Oklahoma             | 1.08477%                                                          | 10.84769%                                                          | 108.47691%                                                          |                                                 1533 |                               42924 |
| Oregon               | 0.31998%                                                          | 3.19982%                                                           | 31.99820%                                                           |                                                  482 |                               13496 |
| Pennsylvania         | 0.49233%                                                          | 4.92330%                                                           | 49.23297%                                                           |                                                 2251 |                               63028 |
| Rhode Island         | 0.71099%                                                          | 7.10995%                                                           | 71.09946%                                                           |                                                  269 |                                7532 |
| South Carolina       | 0.92777%                                                          | 9.27766%                                                           | 92.77657%                                                           |                                                 1706 |                               47768 |
| South Dakota         | 3.26001%                                                          | 32.60013%                                                          | 326.00132%                                                          |                                                 1030 |                               28840 |
| Tennessee            | 1.21567%                                                          | 12.15667%                                                          | 121.56668%                                                          |                                                 2965 |                               83020 |
| Texas                | 0.67654%                                                          | 6.76537%                                                           | 67.65375%                                                           |                                                 7006 |                              196168 |
| Utah                 | 1.31093%                                                          | 13.10934%                                                          | 131.09342%                                                          |                                                 1501 |                               42028 |
| Vermont              | 0.14359%                                                          | 1.43592%                                                           | 14.35923%                                                           |                                                   32 |                                 896 |
| Virginia             | 0.60491%                                                          | 6.04908%                                                           | 60.49076%                                                           |                                                 1844 |                               51632 |
| Washington           | 0.26107%                                                          | 2.61067%                                                           | 26.10674%                                                           |                                                  710 |                               19880 |
| West Virginia        | 0.59683%                                                          | 5.96826%                                                           | 59.68260%                                                           |                                                  382 |                               10696 |
| Wisconsin            | 1.57446%                                                          | 15.74462%                                                          | 157.44618%                                                          |                                                 3274 |                               91672 |
| Wyoming              | 1.17562%                                                          | 11.75619%                                                          | 117.56189%                                                          |                                                  243 |                                6804 |
| Puerto Rico          | 0.91618%                                                          | 9.16180%                                                           | 91.61804%                                                           |                                                 1045 |                               29260 |
| District of Columbia | 0.41658%                                                          | 4.16579%                                                           | 41.65787%                                                           |                                                  105 |                                2940 |