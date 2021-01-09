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

 Updated at: 2021-01-09T06:36:01.127483+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 3.13967%                                                          | 31.39673%                                                          | 313.96735%                                                          |                                                 5498 |                              153944 |
| Alaska               | 3.06584%                                                          | 30.65840%                                                          | 306.58401%                                                          |                                                  801 |                               22428 |
| Arizona              | 6.62963%                                                          | 66.29630%                                                          | 662.96299%                                                          |                                                17234 |                              482552 |
| Arkansas             | 3.99337%                                                          | 39.93367%                                                          | 399.33674%                                                          |                                                 4304 |                              120512 |
| California           | 3.77996%                                                          | 37.79964%                                                          | 377.99645%                                                          |                                                53341 |                             1493548 |
| Colorado             | 1.68863%                                                          | 16.88634%                                                          | 168.86345%                                                          |                                                 3473 |                               97244 |
| Connecticut          | 6.64171%                                                          | 66.41709%                                                          | 664.17093%                                                          |                                                 8457 |                              236796 |
| Delaware             | 3.50804%                                                          | 35.08037%                                                          | 350.80369%                                                          |                                                 1220 |                               34160 |
| Florida              | 3.98025%                                                          | 39.80252%                                                          | 398.02517%                                                          |                                                30531 |                              854868 |
| Georgia              | 2.73712%                                                          | 27.37124%                                                          | 273.71237%                                                          |                                                10379 |                              290612 |
| Hawaii               | 0.63480%                                                          | 6.34803%                                                           | 63.48031%                                                           |                                                  321 |                                8988 |
| Idaho                | 2.40976%                                                          | 24.09761%                                                          | 240.97613%                                                          |                                                 1538 |                               43064 |
| Illinois             | 2.04987%                                                          | 20.49871%                                                          | 204.98711%                                                          |                                                 9277 |                              259756 |
| Indiana              | 3.02367%                                                          | 30.23669%                                                          | 302.36687%                                                          |                                                 7270 |                              203560 |
| Iowa                 | 1.78380%                                                          | 17.83796%                                                          | 178.37956%                                                          |                                                 2010 |                               56280 |
| Kansas               | 6.12512%                                                          | 61.25121%                                                          | 612.51207%                                                          |                                                 6373 |                              178444 |
| Kentucky             | 5.45814%                                                          | 54.58143%                                                          | 545.81434%                                                          |                                                 8709 |                              243852 |
| Louisiana            | 4.14146%                                                          | 41.41461%                                                          | 414.14612%                                                          |                                                 6876 |                              192528 |
| Maine                | 2.17466%                                                          | 21.74657%                                                          | 217.46570%                                                          |                                                 1044 |                               29232 |
| Maryland             | 1.72844%                                                          | 17.28441%                                                          | 172.84408%                                                          |                                                 3732 |                              104496 |
| Massachusetts        | 3.65737%                                                          | 36.57365%                                                          | 365.73651%                                                          |                                                 9003 |                              252084 |
| Michigan             | 2.66350%                                                          | 26.63501%                                                          | 266.35006%                                                          |                                                 9500 |                              266000 |
| Minnesota            | 1.56095%                                                          | 15.60953%                                                          | 156.09529%                                                          |                                                 3144 |                               88032 |
| Mississippi          | 3.06235%                                                          | 30.62347%                                                          | 306.23467%                                                          |                                                 3255 |                               91140 |
| Missouri             | 2.15745%                                                          | 21.57451%                                                          | 215.74510%                                                          |                                                 4729 |                              132412 |
| Montana              | 2.28972%                                                          | 22.89718%                                                          | 228.97178%                                                          |                                                  874 |                               24472 |
| Nebraska             | 2.19437%                                                          | 21.94366%                                                          | 219.43664%                                                          |                                                 1516 |                               42448 |
| Nevada               | 3.09257%                                                          | 30.92571%                                                          | 309.25706%                                                          |                                                 3402 |                               95256 |
| New Hampshire        | 2.60702%                                                          | 26.07025%                                                          | 260.70246%                                                          |                                                 1266 |                               35448 |
| New Jersey           | 7.54206%                                                          | 75.42059%                                                          | 754.20589%                                                          |                                                23925 |                              669900 |
| New Mexico           | 2.45037%                                                          | 24.50367%                                                          | 245.03667%                                                          |                                                 1835 |                               51380 |
| New York             | 2.71054%                                                          | 27.10537%                                                          | 271.05372%                                                          |                                                18832 |                              527296 |
| North Carolina       | 5.18428%                                                          | 51.84283%                                                          | 518.42834%                                                          |                                                19419 |                              543732 |
| North Dakota         | 1.49542%                                                          | 14.95416%                                                          | 149.54164%                                                          |                                                  407 |                               11396 |
| Ohio                 | 3.42374%                                                          | 34.23737%                                                          | 342.37366%                                                          |                                                14293 |                              400204 |
| Oklahoma             | 5.67293%                                                          | 56.72925%                                                          | 567.29251%                                                          |                                                 8017 |                              224476 |
| Oregon               | 1.16973%                                                          | 11.69727%                                                          | 116.97268%                                                          |                                                 1762 |                               49336 |
| Pennsylvania         | 2.22609%                                                          | 22.26092%                                                          | 222.60916%                                                          |                                                10178 |                              284984 |
| Rhode Island         | 4.25804%                                                          | 42.58039%                                                          | 425.80386%                                                          |                                                 1611 |                               45108 |
| South Carolina       | 4.86778%                                                          | 48.67779%                                                          | 486.77786%                                                          |                                                 8951 |                              250628 |
| South Dakota         | 2.22504%                                                          | 22.25038%                                                          | 222.50381%                                                          |                                                  703 |                               19684 |
| Tennessee            | 7.10540%                                                          | 71.05398%                                                          | 710.53981%                                                          |                                                17330 |                              485240 |
| Texas                | 3.14340%                                                          | 31.43398%                                                          | 314.33982%                                                          |                                                32552 |                              911456 |
| Utah                 | 4.40355%                                                          | 44.03551%                                                          | 440.35511%                                                          |                                                 5042 |                              141176 |
| Vermont              | 1.24297%                                                          | 12.42971%                                                          | 124.29706%                                                          |                                                  277 |                                7756 |
| Virginia             | 1.76716%                                                          | 17.67157%                                                          | 176.71567%                                                          |                                                 5387 |                              150836 |
| Washington           | 3.17840%                                                          | 31.78403%                                                          | 317.84032%                                                          |                                                 8644 |                              242032 |
| West Virginia        | 3.88406%                                                          | 38.84056%                                                          | 388.40564%                                                          |                                                 2486 |                               69608 |
| Wisconsin            | 2.16837%                                                          | 21.68372%                                                          | 216.83715%                                                          |                                                 4509 |                              126252 |
| Wyoming              | 2.43832%                                                          | 24.38321%                                                          | 243.83206%                                                          |                                                  504 |                               14112 |
| Puerto Rico          | 1.90162%                                                          | 19.01622%                                                          | 190.16224%                                                          |                                                 2169 |                               60732 |
| District of Columbia | 1.95197%                                                          | 19.51969%                                                          | 195.19688%                                                          |                                                  492 |                               13776 |