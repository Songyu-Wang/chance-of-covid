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

 Updated at: 2020-10-02T12:35:11.809543+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.40023%                                                          | 14.00233%                                                          | 140.02327%                                                          |                                                 2452 |                               68656 |
| Alaska               | 0.99898%                                                          | 9.98982%                                                           | 99.89816%                                                           |                                                  261 |                                7308 |
| Arizona              | 0.49316%                                                          | 4.93164%                                                           | 49.31638%                                                           |                                                 1282 |                               35896 |
| Arkansas             | 1.04288%                                                          | 10.42878%                                                          | 104.28775%                                                          |                                                 1124 |                               31472 |
| California           | 0.30500%                                                          | 3.04999%                                                           | 30.49993%                                                           |                                                 4304 |                              120512 |
| Colorado             | 0.34473%                                                          | 3.44728%                                                           | 34.47284%                                                           |                                                  709 |                               19852 |
| Connecticut          | 0.43980%                                                          | 4.39796%                                                           | 43.97963%                                                           |                                                  560 |                               15680 |
| Delaware             | 0.50033%                                                          | 5.00327%                                                           | 50.03266%                                                           |                                                  174 |                                4872 |
| Florida              | 0.46580%                                                          | 4.65803%                                                           | 46.58033%                                                           |                                                 3573 |                              100044 |
| Georgia              | 0.60233%                                                          | 6.02331%                                                           | 60.23307%                                                           |                                                 2284 |                               63952 |
| Hawaii               | 0.33026%                                                          | 3.30256%                                                           | 33.02558%                                                           |                                                  167 |                                4676 |
| Idaho                | 0.96202%                                                          | 9.62024%                                                           | 96.20243%                                                           |                                                  614 |                               17192 |
| Illinois             | 0.61980%                                                          | 6.19800%                                                           | 61.98004%                                                           |                                                 2805 |                               78540 |
| Indiana              | 0.48703%                                                          | 4.87031%                                                           | 48.70311%                                                           |                                                 1171 |                               32788 |
| Iowa                 | 1.04987%                                                          | 10.49866%                                                          | 104.98658%                                                          |                                                 1183 |                               33124 |
| Kansas               | 1.95777%                                                          | 19.57770%                                                          | 195.77704%                                                          |                                                 2037 |                               57036 |
| Kentucky             | 0.61670%                                                          | 6.16697%                                                           | 61.66969%                                                           |                                                  984 |                               27552 |
| Louisiana            | 0.58966%                                                          | 5.89658%                                                           | 58.96583%                                                           |                                                  979 |                               27412 |
| Maine                | 0.11248%                                                          | 1.12482%                                                           | 11.24823%                                                           |                                                   54 |                                1512 |
| Maryland             | 0.36357%                                                          | 3.63565%                                                           | 36.35654%                                                           |                                                  785 |                               21980 |
| Massachusetts        | 0.30630%                                                          | 3.06304%                                                           | 30.63038%                                                           |                                                  754 |                               21112 |
| Michigan             | 0.44158%                                                          | 4.41580%                                                           | 44.15804%                                                           |                                                 1575 |                               44100 |
| Minnesota            | 0.72983%                                                          | 7.29835%                                                           | 72.98349%                                                           |                                                 1470 |                               41160 |
| Mississippi          | 1.08382%                                                          | 10.83817%                                                          | 108.38167%                                                          |                                                 1152 |                               32256 |
| Missouri             | 0.90650%                                                          | 9.06504%                                                           | 90.65035%                                                           |                                                 1987 |                               55636 |
| Montana              | 1.12390%                                                          | 11.23900%                                                          | 112.39004%                                                          |                                                  429 |                               12012 |
| Nebraska             | 0.75269%                                                          | 7.52685%                                                           | 75.26851%                                                           |                                                  520 |                               14560 |
| Nevada               | 0.54725%                                                          | 5.47245%                                                           | 54.72450%                                                           |                                                  602 |                               16856 |
| New Hampshire        | 0.15856%                                                          | 1.58563%                                                           | 15.85631%                                                           |                                                   77 |                                2156 |
| New Jersey           | 0.23643%                                                          | 2.36428%                                                           | 23.64282%                                                           |                                                  750 |                               21000 |
| New Mexico           | 0.37123%                                                          | 3.71227%                                                           | 37.12272%                                                           |                                                  278 |                                7784 |
| New York             | 0.19891%                                                          | 1.98915%                                                           | 19.89147%                                                           |                                                 1382 |                               38696 |
| North Carolina       | 1.63973%                                                          | 16.39728%                                                          | 163.97275%                                                          |                                                 6142 |                              171976 |
| North Dakota         | 1.86284%                                                          | 18.62841%                                                          | 186.28406%                                                          |                                                  507 |                               14196 |
| Ohio                 | 0.31787%                                                          | 3.17869%                                                           | 31.78688%                                                           |                                                 1327 |                               37156 |
| Oklahoma             | 1.19162%                                                          | 11.91619%                                                          | 119.16185%                                                          |                                                 1684 |                               47152 |
| Oregon               | 0.32662%                                                          | 3.26621%                                                           | 32.66206%                                                           |                                                  492 |                               13776 |
| Pennsylvania         | 0.25415%                                                          | 2.54148%                                                           | 25.41480%                                                           |                                                 1162 |                               32536 |
| Rhode Island         | 0.50748%                                                          | 5.07476%                                                           | 50.74757%                                                           |                                                  192 |                                5376 |
| South Carolina       | 1.44929%                                                          | 14.49294%                                                          | 144.92939%                                                          |                                                 2665 |                               74620 |
| South Dakota         | 2.36430%                                                          | 23.64301%                                                          | 236.43008%                                                          |                                                  747 |                               20916 |
| Tennessee            | 0.96638%                                                          | 9.66383%                                                           | 96.63833%                                                           |                                                 2357 |                               65996 |
| Texas                | 1.72080%                                                          | 17.20796%                                                          | 172.07961%                                                          |                                                17820 |                              498960 |
| Utah                 | 1.23233%                                                          | 12.32331%                                                          | 123.23306%                                                          |                                                 1411 |                               39508 |
| Vermont              | 0.03590%                                                          | 0.35898%                                                           | 3.58981%                                                            |                                                    8 |                                 224 |
| Virginia             | 0.40743%                                                          | 4.07427%                                                           | 40.74269%                                                           |                                                 1242 |                               34776 |
| Washington           | 0.36329%                                                          | 3.63288%                                                           | 36.32881%                                                           |                                                  988 |                               27664 |
| West Virginia        | 0.39528%                                                          | 3.95280%                                                           | 39.52801%                                                           |                                                  253 |                                7084 |
| Wisconsin            | 1.44270%                                                          | 14.42696%                                                          | 144.26956%                                                          |                                                 3000 |                               84000 |
| Wyoming              | 0.81277%                                                          | 8.12774%                                                           | 81.27735%                                                           |                                                  168 |                                4704 |
| Puerto Rico          | 1.14764%                                                          | 11.47637%                                                          | 114.76366%                                                          |                                                 1309 |                               36652 |
| District of Columbia | 0.24598%                                                          | 2.45980%                                                           | 24.59798%                                                           |                                                   62 |                                1736 |