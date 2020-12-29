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

 Updated at: 2020-12-29T06:28:29.088258+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 3.05401%                                                          | 30.54015%                                                          | 305.40149%                                                          |                                                 5348 |                              149744 |
| Alaska               | 2.30799%                                                          | 23.07992%                                                          | 230.79920%                                                          |                                                  603 |                               16884 |
| Arizona              | 3.87991%                                                          | 38.79915%                                                          | 387.99146%                                                          |                                                10086 |                              282408 |
| Arkansas             | 2.97276%                                                          | 29.72758%                                                          | 297.27577%                                                          |                                                 3204 |                               89712 |
| California           | 3.80618%                                                          | 38.06184%                                                          | 380.61842%                                                          |                                                53711 |                             1503908 |
| Colorado             | 1.79803%                                                          | 17.98033%                                                          | 179.80335%                                                          |                                                 3698 |                              103544 |
| Connecticut          | 6.64171%                                                          | 66.41709%                                                          | 664.17093%                                                          |                                                 8457 |                              236796 |
| Delaware             | 2.95308%                                                          | 29.53077%                                                          | 295.30769%                                                          |                                                 1027 |                               28756 |
| Florida              | 2.16254%                                                          | 21.62537%                                                          | 216.25370%                                                          |                                                16588 |                              464464 |
| Georgia              | 2.08310%                                                          | 20.83104%                                                          | 208.31043%                                                          |                                                 7899 |                              221172 |
| Hawaii               | 0.39947%                                                          | 3.99471%                                                           | 39.94711%                                                           |                                                  202 |                                5656 |
| Idaho                | 2.82340%                                                          | 28.23400%                                                          | 282.34004%                                                          |                                                 1802 |                               50456 |
| Illinois             | 1.95066%                                                          | 19.50659%                                                          | 195.06589%                                                          |                                                 8828 |                              247184 |
| Indiana              | 2.69635%                                                          | 26.96347%                                                          | 269.63472%                                                          |                                                 6483 |                              181524 |
| Iowa                 | 1.36580%                                                          | 13.65802%                                                          | 136.58017%                                                          |                                                 1539 |                               43092 |
| Kansas               | 6.12512%                                                          | 61.25121%                                                          | 612.51207%                                                          |                                                 6373 |                              178444 |
| Kentucky             | 3.31099%                                                          | 33.10985%                                                          | 331.09854%                                                          |                                                 5283 |                              147924 |
| Louisiana            | 2.27431%                                                          | 22.74310%                                                          | 227.43103%                                                          |                                                 3776 |                              105728 |
| Maine                | 1.55809%                                                          | 15.58088%                                                          | 155.80876%                                                          |                                                  748 |                               20944 |
| Maryland             | 1.32736%                                                          | 13.27361%                                                          | 132.73610%                                                          |                                                 2866 |                               80248 |
| Massachusetts        | 3.11869%                                                          | 31.18693%                                                          | 311.86929%                                                          |                                                 7677 |                              214956 |
| Michigan             | 2.20846%                                                          | 22.08463%                                                          | 220.84626%                                                          |                                                 7877 |                              220556 |
| Minnesota            | 1.36981%                                                          | 13.69806%                                                          | 136.98057%                                                          |                                                 2759 |                               77252 |
| Mississippi          | 2.47810%                                                          | 24.78102%                                                          | 247.81017%                                                          |                                                 2634 |                               73752 |
| Missouri             | 1.69850%                                                          | 16.98497%                                                          | 169.84965%                                                          |                                                 3723 |                              104244 |
| Montana              | 2.19802%                                                          | 21.98024%                                                          | 219.80243%                                                          |                                                  839 |                               23492 |
| Nebraska             | 2.19581%                                                          | 21.95814%                                                          | 219.58139%                                                          |                                                 1517 |                               42476 |
| Nevada               | 2.71623%                                                          | 27.16226%                                                          | 271.62261%                                                          |                                                 2988 |                               83664 |
| New Hampshire        | 2.12310%                                                          | 21.23098%                                                          | 212.30982%                                                          |                                                 1031 |                               28868 |
| New Jersey           | 1.78456%                                                          | 17.84560%                                                          | 178.45599%                                                          |                                                 5661 |                              158508 |
| New Mexico           | 2.56921%                                                          | 25.69213%                                                          | 256.92128%                                                          |                                                 1924 |                               53872 |
| New York             | 1.82751%                                                          | 18.27511%                                                          | 182.75112%                                                          |                                                12697 |                              355516 |
| North Carolina       | 5.18428%                                                          | 51.84283%                                                          | 518.42834%                                                          |                                                19419 |                              543732 |
| North Dakota         | 1.81508%                                                          | 18.15075%                                                          | 181.50754%                                                          |                                                  494 |                               13832 |
| Ohio                 | 2.73362%                                                          | 27.33624%                                                          | 273.36236%                                                          |                                                11412 |                              319536 |
| Oklahoma             | 3.51683%                                                          | 35.16831%                                                          | 351.68314%                                                          |                                                 4970 |                              139160 |
| Oregon               | 1.01571%                                                          | 10.15711%                                                          | 101.57106%                                                          |                                                 1530 |                               42840 |
| Pennsylvania         | 2.19788%                                                          | 21.97877%                                                          | 219.78772%                                                          |                                                10049 |                              281372 |
| Rhode Island         | 3.08186%                                                          | 30.81858%                                                          | 308.18578%                                                          |                                                 1166 |                               32648 |
| South Carolina       | 3.96285%                                                          | 39.62854%                                                          | 396.28536%                                                          |                                                 7287 |                              204036 |
| South Dakota         | 2.86122%                                                          | 28.61215%                                                          | 286.12155%                                                          |                                                  904 |                               25312 |
| Tennessee            | 6.57485%                                                          | 65.74851%                                                          | 657.48508%                                                          |                                                16036 |                              449008 |
| Texas                | 2.25606%                                                          | 22.56058%                                                          | 225.60584%                                                          |                                                23363 |                              654164 |
| Utah                 | 3.04720%                                                          | 30.47201%                                                          | 304.72015%                                                          |                                                 3489 |                               97692 |
| Vermont              | 0.83014%                                                          | 8.30143%                                                           | 83.01428%                                                           |                                                  185 |                                5180 |
| Virginia             | 1.56869%                                                          | 15.68692%                                                          | 156.86920%                                                          |                                                 4782 |                              133896 |
| Washington           | 1.48367%                                                          | 14.83672%                                                          | 148.36715%                                                          |                                                 4035 |                              112980 |
| West Virginia        | 2.55604%                                                          | 25.56040%                                                          | 255.60403%                                                          |                                                 1636 |                               45808 |
| Wisconsin            | 2.07508%                                                          | 20.75077%                                                          | 207.50772%                                                          |                                                 4315 |                              120820 |
| Wyoming              | 3.70586%                                                          | 37.05860%                                                          | 370.58603%                                                          |                                                  766 |                               21448 |
| Puerto Rico          | 1.21076%                                                          | 12.10761%                                                          | 121.07610%                                                          |                                                 1381 |                               38668 |
| District of Columbia | 1.95197%                                                          | 19.51969%                                                          | 195.19688%                                                          |                                                  492 |                               13776 |