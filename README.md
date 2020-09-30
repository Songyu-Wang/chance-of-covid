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

 Updated at: 2020-09-30T06:20:27.063234+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 1.40023%                                                          | 14.00233%                                                          | 140.02327%                                                          |                                                 2452 |                               68656 |
| Alaska               | 0.99898%                                                          | 9.98982%                                                           | 99.89816%                                                           |                                                  261 |                                7308 |
| Arizona              | 0.67435%                                                          | 6.74350%                                                           | 67.43496%                                                           |                                                 1753 |                               49084 |
| Arkansas             | 1.00762%                                                          | 10.07620%                                                          | 100.76201%                                                          |                                                 1086 |                               30408 |
| California           | 0.30500%                                                          | 3.04999%                                                           | 30.49993%                                                           |                                                 4304 |                              120512 |
| Colorado             | 0.34473%                                                          | 3.44728%                                                           | 34.47284%                                                           |                                                  709 |                               19852 |
| Connecticut          | 0.43980%                                                          | 4.39796%                                                           | 43.97963%                                                           |                                                  560 |                               15680 |
| Delaware             | 0.40831%                                                          | 4.08312%                                                           | 40.83125%                                                           |                                                  142 |                                3976 |
| Florida              | 0.46580%                                                          | 4.65803%                                                           | 46.58033%                                                           |                                                 3573 |                              100044 |
| Georgia              | 0.60233%                                                          | 6.02331%                                                           | 60.23307%                                                           |                                                 2284 |                               63952 |
| Hawaii               | 0.33026%                                                          | 3.30256%                                                           | 33.02558%                                                           |                                                  167 |                                4676 |
| Idaho                | 0.84451%                                                          | 8.44513%                                                           | 84.45132%                                                           |                                                  539 |                               15092 |
| Illinois             | 0.61980%                                                          | 6.19800%                                                           | 61.98004%                                                           |                                                 2805 |                               78540 |
| Indiana              | 0.48703%                                                          | 4.87031%                                                           | 48.70311%                                                           |                                                 1171 |                               32788 |
| Iowa                 | 1.04987%                                                          | 10.49866%                                                          | 104.98658%                                                          |                                                 1183 |                               33124 |
| Kansas               | 1.95777%                                                          | 19.57770%                                                          | 195.77704%                                                          |                                                 2037 |                               57036 |
| Kentucky             | 0.61294%                                                          | 6.12937%                                                           | 61.29365%                                                           |                                                  978 |                               27384 |
| Louisiana            | 0.58966%                                                          | 5.89658%                                                           | 58.96583%                                                           |                                                  979 |                               27412 |
| Maine                | 0.09165%                                                          | 0.91652%                                                           | 9.16522%                                                            |                                                   44 |                                1232 |
| Maryland             | 0.31586%                                                          | 3.15862%                                                           | 31.58619%                                                           |                                                  682 |                               19096 |
| Massachusetts        | 0.24334%                                                          | 2.43337%                                                           | 24.33369%                                                           |                                                  599 |                               16772 |
| Michigan             | 0.44158%                                                          | 4.41580%                                                           | 44.15804%                                                           |                                                 1575 |                               44100 |
| Minnesota            | 0.72983%                                                          | 7.29835%                                                           | 72.98349%                                                           |                                                 1470 |                               41160 |
| Mississippi          | 1.08382%                                                          | 10.83817%                                                          | 108.38167%                                                          |                                                 1152 |                               32256 |
| Missouri             | 0.90650%                                                          | 9.06504%                                                           | 90.65035%                                                           |                                                 1987 |                               55636 |
| Montana              | 0.89860%                                                          | 8.98596%                                                           | 89.85963%                                                           |                                                  343 |                                9604 |
| Nebraska             | 0.74545%                                                          | 7.45448%                                                           | 74.54477%                                                           |                                                  515 |                               14420 |
| Nevada               | 0.54725%                                                          | 5.47245%                                                           | 54.72450%                                                           |                                                  602 |                               16856 |
| New Hampshire        | 0.15856%                                                          | 1.58563%                                                           | 15.85631%                                                           |                                                   77 |                                2156 |
| New Jersey           | 0.23643%                                                          | 2.36428%                                                           | 23.64282%                                                           |                                                  750 |                               21000 |
| New Mexico           | 0.35120%                                                          | 3.51197%                                                           | 35.11970%                                                           |                                                  263 |                                7364 |
| New York             | 0.17114%                                                          | 1.71136%                                                           | 17.11358%                                                           |                                                 1189 |                               33292 |
| North Carolina       | 1.63973%                                                          | 16.39728%                                                          | 163.97275%                                                          |                                                 6142 |                              171976 |
| North Dakota         | 1.86284%                                                          | 18.62841%                                                          | 186.28406%                                                          |                                                  507 |                               14196 |
| Ohio                 | 0.27547%                                                          | 2.75470%                                                           | 27.54703%                                                           |                                                 1150 |                               32200 |
| Oklahoma             | 1.19162%                                                          | 11.91619%                                                          | 119.16185%                                                          |                                                 1684 |                               47152 |
| Oregon               | 0.32662%                                                          | 3.26621%                                                           | 32.66206%                                                           |                                                  492 |                               13776 |
| Pennsylvania         | 0.25415%                                                          | 2.54148%                                                           | 25.41480%                                                           |                                                 1162 |                               32536 |
| Rhode Island         | 0.47047%                                                          | 4.70472%                                                           | 47.04723%                                                           |                                                  178 |                                4984 |
| South Carolina       | 1.44929%                                                          | 14.49294%                                                          | 144.92939%                                                          |                                                 2665 |                               74620 |
| South Dakota         | 1.83257%                                                          | 18.32571%                                                          | 183.25705%                                                          |                                                  579 |                               16212 |
| Tennessee            | 0.96638%                                                          | 9.66383%                                                           | 96.63833%                                                           |                                                 2357 |                               65996 |
| Texas                | 1.72080%                                                          | 17.20796%                                                          | 172.07961%                                                          |                                                17820 |                              498960 |
| Utah                 | 1.23233%                                                          | 12.32331%                                                          | 123.23306%                                                          |                                                 1411 |                               39508 |
| Vermont              | 0.03590%                                                          | 0.35898%                                                           | 3.58981%                                                            |                                                    8 |                                 224 |
| Virginia             | 0.40743%                                                          | 4.07427%                                                           | 40.74269%                                                           |                                                 1242 |                               34776 |
| Washington           | 0.36329%                                                          | 3.63288%                                                           | 36.32881%                                                           |                                                  988 |                               27664 |
| West Virginia        | 0.39528%                                                          | 3.95280%                                                           | 39.52801%                                                           |                                                  253 |                                7084 |
| Wisconsin            | 1.39557%                                                          | 13.95568%                                                          | 139.55676%                                                          |                                                 2902 |                               81256 |
| Wyoming              | 0.81277%                                                          | 8.12774%                                                           | 81.27735%                                                           |                                                  168 |                                4704 |
| Puerto Rico          | 1.14764%                                                          | 11.47637%                                                          | 114.76366%                                                          |                                                 1309 |                               36652 |
| District of Columbia | 0.24598%                                                          | 2.45980%                                                           | 24.59798%                                                           |                                                   62 |                                1736 |