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

 Updated at: 2020-12-21T12:30:04.177404+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 3.05401%                                                          | 30.54015%                                                          | 305.40149%                                                          |                                                 5348 |                              149744 |
| Alaska               | 2.43813%                                                          | 24.38128%                                                          | 243.81275%                                                          |                                                  637 |                               17836 |
| Arizona              | 4.73699%                                                          | 47.36989%                                                          | 473.69887%                                                          |                                                12314 |                              344792 |
| Arkansas             | 2.81967%                                                          | 28.19666%                                                          | 281.96662%                                                          |                                                 3039 |                               85092 |
| California           | 3.80618%                                                          | 38.06184%                                                          | 380.61842%                                                          |                                                53711 |                             1503908 |
| Colorado             | 2.27453%                                                          | 22.74527%                                                          | 227.45269%                                                          |                                                 4678 |                              130984 |
| Connecticut          | 6.38411%                                                          | 63.84114%                                                          | 638.41144%                                                          |                                                 8129 |                              227612 |
| Delaware             | 3.04222%                                                          | 30.42216%                                                          | 304.22156%                                                          |                                                 1058 |                               29624 |
| Florida              | 1.70808%                                                          | 17.08076%                                                          | 170.80757%                                                          |                                                13102 |                              366856 |
| Georgia              | 1.60657%                                                          | 16.06567%                                                          | 160.65669%                                                          |                                                 6092 |                              170576 |
| Hawaii               | 0.39947%                                                          | 3.99471%                                                           | 39.94711%                                                           |                                                  202 |                                5656 |
| Idaho                | 3.60054%                                                          | 36.00541%                                                          | 360.05406%                                                          |                                                 2298 |                               64344 |
| Illinois             | 2.45291%                                                          | 24.52907%                                                          | 245.29071%                                                          |                                                11101 |                              310828 |
| Indiana              | 3.07815%                                                          | 30.78153%                                                          | 307.81530%                                                          |                                                 7401 |                              207228 |
| Iowa                 | 1.59477%                                                          | 15.94767%                                                          | 159.47665%                                                          |                                                 1797 |                               50316 |
| Kansas               | 5.62919%                                                          | 56.29191%                                                          | 562.91907%                                                          |                                                 5857 |                              163996 |
| Kentucky             | 2.70369%                                                          | 27.03689%                                                          | 270.36894%                                                          |                                                 4314 |                              120792 |
| Louisiana            | 2.66340%                                                          | 26.63400%                                                          | 266.34004%                                                          |                                                 4422 |                              123816 |
| Maine                | 1.22897%                                                          | 12.28973%                                                          | 122.89728%                                                          |                                                  590 |                               16520 |
| Maryland             | 1.63859%                                                          | 16.38592%                                                          | 163.85915%                                                          |                                                 3538 |                               99064 |
| Massachusetts        | 2.42321%                                                          | 24.23213%                                                          | 242.32126%                                                          |                                                 5965 |                              167020 |
| Michigan             | 2.75434%                                                          | 27.54340%                                                          | 275.43400%                                                          |                                                 9824 |                              275072 |
| Minnesota            | 2.62641%                                                          | 26.26413%                                                          | 262.64125%                                                          |                                                 5290 |                              148120 |
| Mississippi          | 2.58347%                                                          | 25.83473%                                                          | 258.34728%                                                          |                                                 2746 |                               76888 |
| Missouri             | 1.77925%                                                          | 17.79247%                                                          | 177.92469%                                                          |                                                 3900 |                              109200 |
| Montana              | 2.56218%                                                          | 25.62178%                                                          | 256.21785%                                                          |                                                  978 |                               27384 |
| Nebraska             | 2.67782%                                                          | 26.77822%                                                          | 267.78218%                                                          |                                                 1850 |                               51800 |
| Nevada               | 2.77531%                                                          | 27.75314%                                                          | 277.53140%                                                          |                                                 3053 |                               85484 |
| New Hampshire        | 2.44434%                                                          | 24.44343%                                                          | 244.43430%                                                          |                                                 1187 |                               33236 |
| New Jersey           | 1.96708%                                                          | 19.67082%                                                          | 196.70824%                                                          |                                                 6240 |                              174720 |
| New Mexico           | 2.48242%                                                          | 24.82415%                                                          | 248.24151%                                                          |                                                 1859 |                               52052 |
| New York             | 1.82751%                                                          | 18.27511%                                                          | 182.75112%                                                          |                                                12697 |                              355516 |
| North Carolina       | 2.25429%                                                          | 22.54292%                                                          | 225.42916%                                                          |                                                 8444 |                              236432 |
| North Dakota         | 2.13841%                                                          | 21.38409%                                                          | 213.84087%                                                          |                                                  582 |                               16296 |
| Ohio                 | 6.16119%                                                          | 61.61193%                                                          | 616.11929%                                                          |                                                25721 |                              720188 |
| Oklahoma             | 3.51683%                                                          | 35.16831%                                                          | 351.68314%                                                          |                                                 4970 |                              139160 |
| Oregon               | 1.05023%                                                          | 10.50231%                                                          | 105.02314%                                                          |                                                 1582 |                               44296 |
| Pennsylvania         | 2.78754%                                                          | 27.87536%                                                          | 278.75356%                                                          |                                                12745 |                              356860 |
| Rhode Island         | 4.83952%                                                          | 48.39521%                                                          | 483.95212%                                                          |                                                 1831 |                               51268 |
| South Carolina       | 2.33954%                                                          | 23.39536%                                                          | 233.95357%                                                          |                                                 4302 |                              120456 |
| South Dakota         | 3.11759%                                                          | 31.17585%                                                          | 311.75854%                                                          |                                                  985 |                               27580 |
| Tennessee            | 6.57485%                                                          | 65.74851%                                                          | 657.48508%                                                          |                                                16036 |                              449008 |
| Texas                | 1.91673%                                                          | 19.16727%                                                          | 191.67274%                                                          |                                                19849 |                              555772 |
| Utah                 | 3.22450%                                                          | 32.24496%                                                          | 322.44964%                                                          |                                                 3692 |                              103376 |
| Vermont              | 0.62822%                                                          | 6.28216%                                                           | 62.82162%                                                           |                                                  140 |                                3920 |
| Virginia             | 1.44272%                                                          | 14.42724%                                                          | 144.27242%                                                          |                                                 4398 |                              123144 |
| Washington           | 1.34211%                                                          | 13.42107%                                                          | 134.21068%                                                          |                                                 3650 |                              102200 |
| West Virginia        | 2.55604%                                                          | 25.56040%                                                          | 255.60403%                                                          |                                                 1636 |                               45808 |
| Wisconsin            | 2.26455%                                                          | 22.64551%                                                          | 226.45512%                                                          |                                                 4709 |                              131852 |
| Wyoming              | 3.70586%                                                          | 37.05860%                                                          | 370.58603%                                                          |                                                  766 |                               21448 |
| Puerto Rico          | 1.35367%                                                          | 13.53668%                                                          | 135.36676%                                                          |                                                 1544 |                               43232 |
| District of Columbia | 1.19419%                                                          | 11.94192%                                                          | 119.41923%                                                          |                                                  301 |                                8428 |