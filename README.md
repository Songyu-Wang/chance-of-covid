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

 Updated at: 2020-12-12T12:26:25.627532+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.70396%                                                          | 27.03957%                                                          | 270.39567%                                                          |                                                 4735 |                              132580 |
| Alaska               | 3.52897%                                                          | 35.28970%                                                          | 352.89695%                                                          |                                                  922 |                               25816 |
| Arizona              | 4.73699%                                                          | 47.36989%                                                          | 473.69887%                                                          |                                                12314 |                              344792 |
| Arkansas             | 2.62297%                                                          | 26.22967%                                                          | 262.29669%                                                          |                                                 2827 |                               79156 |
| California           | 2.51341%                                                          | 25.13410%                                                          | 251.34096%                                                          |                                                35468 |                              993104 |
| Colorado             | 2.93530%                                                          | 29.35297%                                                          | 293.52969%                                                          |                                                 6037 |                              169036 |
| Connecticut          | 6.38411%                                                          | 63.84114%                                                          | 638.41144%                                                          |                                                 8129 |                              227612 |
| Delaware             | 2.70866%                                                          | 27.08665%                                                          | 270.86645%                                                          |                                                  942 |                               26376 |
| Florida              | 1.48736%                                                          | 14.87363%                                                          | 148.73634%                                                          |                                                11409 |                              319452 |
| Georgia              | 1.59866%                                                          | 15.98655%                                                          | 159.86553%                                                          |                                                 6062 |                              169736 |
| Hawaii               | 0.28082%                                                          | 2.80816%                                                           | 28.08163%                                                           |                                                  142 |                                3976 |
| Idaho                | 3.60054%                                                          | 36.00541%                                                          | 360.05406%                                                          |                                                 2298 |                               64344 |
| Illinois             | 2.77131%                                                          | 27.71314%                                                          | 277.13144%                                                          |                                                12542 |                              351176 |
| Indiana              | 3.51860%                                                          | 35.18602%                                                          | 351.86021%                                                          |                                                 8460 |                              236880 |
| Iowa                 | 2.10772%                                                          | 21.07719%                                                          | 210.77187%                                                          |                                                 2375 |                               66500 |
| Kansas               | 5.99153%                                                          | 59.91527%                                                          | 599.15272%                                                          |                                                 6234 |                              174552 |
| Kentucky             | 2.70369%                                                          | 27.03689%                                                          | 270.36894%                                                          |                                                 4314 |                              120792 |
| Louisiana            | 3.20789%                                                          | 32.07886%                                                          | 320.78857%                                                          |                                                 5326 |                              149128 |
| Maine                | 0.88944%                                                          | 8.89443%                                                           | 88.94430%                                                           |                                                  427 |                               11956 |
| Maryland             | 1.75623%                                                          | 17.56229%                                                          | 175.62292%                                                          |                                                 3792 |                              106176 |
| Massachusetts        | 2.71164%                                                          | 27.11642%                                                          | 271.16419%                                                          |                                                 6675 |                              186900 |
| Michigan             | 3.02518%                                                          | 30.25176%                                                          | 302.51760%                                                          |                                                10790 |                              302120 |
| Minnesota            | 4.47930%                                                          | 44.79299%                                                          | 447.92994%                                                          |                                                 9022 |                              252616 |
| Mississippi          | 2.58347%                                                          | 25.83473%                                                          | 258.34728%                                                          |                                                 2746 |                               76888 |
| Missouri             | 2.28154%                                                          | 22.81542%                                                          | 228.15420%                                                          |                                                 5001 |                              140028 |
| Montana              | 3.44244%                                                          | 34.42436%                                                          | 344.24361%                                                          |                                                 1314 |                               36792 |
| Nebraska             | 3.38129%                                                          | 33.81293%                                                          | 338.12929%                                                          |                                                 2336 |                               65408 |
| Nevada               | 2.90349%                                                          | 29.03489%                                                          | 290.34893%                                                          |                                                 3194 |                               89432 |
| New Hampshire        | 2.44434%                                                          | 24.44343%                                                          | 244.43430%                                                          |                                                 1187 |                               33236 |
| New Jersey           | 1.90088%                                                          | 19.00883%                                                          | 190.08826%                                                          |                                                 6030 |                              168840 |
| New Mexico           | 3.10335%                                                          | 31.03353%                                                          | 310.33527%                                                          |                                                 2324 |                               65072 |
| New York             | 1.62226%                                                          | 16.22263%                                                          | 162.22634%                                                          |                                                11271 |                              315588 |
| North Carolina       | 2.01295%                                                          | 20.12951%                                                          | 201.29511%                                                          |                                                 7540 |                              211120 |
| North Dakota         | 3.73670%                                                          | 37.36704%                                                          | 373.67038%                                                          |                                                 1017 |                               28476 |
| Ohio                 | 6.16119%                                                          | 61.61193%                                                          | 616.11929%                                                          |                                                25721 |                              720188 |
| Oklahoma             | 4.42753%                                                          | 44.27528%                                                          | 442.75280%                                                          |                                                 6257 |                              175196 |
| Oregon               | 1.44324%                                                          | 14.43238%                                                          | 144.32384%                                                          |                                                 2174 |                               60872 |
| Pennsylvania         | 2.81794%                                                          | 28.17937%                                                          | 281.79371%                                                          |                                                12884 |                              360752 |
| Rhode Island         | 4.77609%                                                          | 47.76087%                                                          | 477.60867%                                                          |                                                 1807 |                               50596 |
| South Carolina       | 1.92514%                                                          | 19.25141%                                                          | 192.51409%                                                          |                                                 3540 |                               99120 |
| South Dakota         | 4.08609%                                                          | 40.86094%                                                          | 408.60942%                                                          |                                                 1291 |                               36148 |
| Tennessee            | 3.36738%                                                          | 33.67376%                                                          | 336.73765%                                                          |                                                 8213 |                              229964 |
| Texas                | 1.58599%                                                          | 15.85991%                                                          | 158.59908%                                                          |                                                16424 |                              459872 |
| Utah                 | 3.49699%                                                          | 34.96989%                                                          | 349.69890%                                                          |                                                 4004 |                              112112 |
| Vermont              | 1.00515%                                                          | 10.05146%                                                          | 100.51459%                                                          |                                                  224 |                                6272 |
| Virginia             | 1.44272%                                                          | 14.42724%                                                          | 144.27242%                                                          |                                                 4398 |                              123144 |
| Washington           | 2.55809%                                                          | 25.58092%                                                          | 255.80924%                                                          |                                                 6957 |                              194796 |
| West Virginia        | 2.22638%                                                          | 22.26380%                                                          | 222.63799%                                                          |                                                 1425 |                               39900 |
| Wisconsin            | 2.74641%                                                          | 27.46412%                                                          | 274.64116%                                                          |                                                 5711 |                              159908 |
| Wyoming              | 3.94776%                                                          | 39.47757%                                                          | 394.77572%                                                          |                                                  816 |                               22848 |
| Puerto Rico          | 1.35367%                                                          | 13.53668%                                                          | 135.36676%                                                          |                                                 1544 |                               43232 |
| District of Columbia | 1.55523%                                                          | 15.55227%                                                          | 155.52271%                                                          |                                                  392 |                               10976 |