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

 Updated at: 2020-12-11T18:20:11.777072+00:00

| State                | Chance of encountering 1 person with COVID if you meet 1 person   | Chance of encountering 1 person with COVID if you meet 10 people   | Chance of encountering a person with COVID if you meet 100 people   |   Max count of new case increase in the past 14 days |   Estimated people count with COVID |
|:---------------------|:------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|-----------------------------------------------------:|------------------------------------:|
| Alabama              | 2.70396%                                                          | 27.03957%                                                          | 270.39567%                                                          |                                                 4735 |                              132580 |
| Alaska               | 3.52897%                                                          | 35.28970%                                                          | 352.89695%                                                          |                                                  922 |                               25816 |
| Arizona              | 4.73699%                                                          | 47.36989%                                                          | 473.69887%                                                          |                                                12314 |                              344792 |
| Arkansas             | 2.62297%                                                          | 26.22967%                                                          | 262.29669%                                                          |                                                 2827 |                               79156 |
| California           | 2.18623%                                                          | 21.86230%                                                          | 218.62298%                                                          |                                                30851 |                              863828 |
| Colorado             | 2.93530%                                                          | 29.35297%                                                          | 293.52969%                                                          |                                                 6037 |                              169036 |
| Connecticut          | 6.38411%                                                          | 63.84114%                                                          | 638.41144%                                                          |                                                 8129 |                              227612 |
| Delaware             | 2.70866%                                                          | 27.08665%                                                          | 270.86645%                                                          |                                                  942 |                               26376 |
| Florida              | 2.18952%                                                          | 21.89523%                                                          | 218.95230%                                                          |                                                16795 |                              470260 |
| Georgia              | 1.59866%                                                          | 15.98655%                                                          | 159.86553%                                                          |                                                 6062 |                              169736 |
| Hawaii               | 0.28082%                                                          | 2.80816%                                                           | 28.08163%                                                           |                                                  142 |                                3976 |
| Idaho                | 3.60054%                                                          | 36.00541%                                                          | 360.05406%                                                          |                                                 2298 |                               64344 |
| Illinois             | 2.77131%                                                          | 27.71314%                                                          | 277.13144%                                                          |                                                12542 |                              351176 |
| Indiana              | 3.51860%                                                          | 35.18602%                                                          | 351.86021%                                                          |                                                 8460 |                              236880 |
| Iowa                 | 2.10772%                                                          | 21.07719%                                                          | 210.77187%                                                          |                                                 2375 |                               66500 |
| Kansas               | 5.99153%                                                          | 59.91527%                                                          | 599.15272%                                                          |                                                 6234 |                              174552 |
| Kentucky             | 3.51968%                                                          | 35.19685%                                                          | 351.96846%                                                          |                                                 5616 |                              157248 |
| Louisiana            | 3.20789%                                                          | 32.07886%                                                          | 320.78857%                                                          |                                                 5326 |                              149128 |
| Maine                | 0.88944%                                                          | 8.89443%                                                           | 88.94430%                                                           |                                                  427 |                               11956 |
| Maryland             | 1.75623%                                                          | 17.56229%                                                          | 175.62292%                                                          |                                                 3792 |                              106176 |
| Massachusetts        | 2.71164%                                                          | 27.11642%                                                          | 271.16419%                                                          |                                                 6675 |                              186900 |
| Michigan             | 4.86944%                                                          | 48.69440%                                                          | 486.94399%                                                          |                                                17368 |                              486304 |
| Minnesota            | 4.47930%                                                          | 44.79299%                                                          | 447.92994%                                                          |                                                 9022 |                              252616 |
| Mississippi          | 2.58347%                                                          | 25.83473%                                                          | 258.34728%                                                          |                                                 2746 |                               76888 |
| Missouri             | 2.28154%                                                          | 22.81542%                                                          | 228.15420%                                                          |                                                 5001 |                              140028 |
| Montana              | 3.44244%                                                          | 34.42436%                                                          | 344.24361%                                                          |                                                 1314 |                               36792 |
| Nebraska             | 4.16293%                                                          | 41.62927%                                                          | 416.29274%                                                          |                                                 2876 |                               80528 |
| Nevada               | 2.90349%                                                          | 29.03489%                                                          | 290.34893%                                                          |                                                 3194 |                               89432 |
| New Hampshire        | 2.15193%                                                          | 21.51928%                                                          | 215.19279%                                                          |                                                 1045 |                               29260 |
| New Jersey           | 1.90088%                                                          | 19.00883%                                                          | 190.08826%                                                          |                                                 6030 |                              168840 |
| New Mexico           | 3.10335%                                                          | 31.03353%                                                          | 310.33527%                                                          |                                                 2324 |                               65072 |
| New York             | 1.62226%                                                          | 16.22263%                                                          | 162.22634%                                                          |                                                11271 |                              315588 |
| North Carolina       | 2.13789%                                                          | 21.37893%                                                          | 213.78929%                                                          |                                                 8008 |                              224224 |
| North Dakota         | 3.73670%                                                          | 37.36704%                                                          | 373.67038%                                                          |                                                 1017 |                               28476 |
| Ohio                 | 6.16119%                                                          | 61.61193%                                                          | 616.11929%                                                          |                                                25721 |                              720188 |
| Oklahoma             | 4.42753%                                                          | 44.27528%                                                          | 442.75280%                                                          |                                                 6257 |                              175196 |
| Oregon               | 1.44324%                                                          | 14.43238%                                                          | 144.32384%                                                          |                                                 2174 |                               60872 |
| Pennsylvania         | 2.81794%                                                          | 28.17937%                                                          | 281.79371%                                                          |                                                12884 |                              360752 |
| Rhode Island         | 4.77609%                                                          | 47.76087%                                                          | 477.60867%                                                          |                                                 1807 |                               50596 |
| South Carolina       | 1.75220%                                                          | 17.52205%                                                          | 175.22045%                                                          |                                                 3222 |                               90216 |
| South Dakota         | 6.76690%                                                          | 67.66901%                                                          | 676.69011%                                                          |                                                 2138 |                               59864 |
| Tennessee            | 3.36738%                                                          | 33.67376%                                                          | 336.73765%                                                          |                                                 8213 |                              229964 |
| Texas                | 1.58599%                                                          | 15.85991%                                                          | 158.59908%                                                          |                                                16424 |                              459872 |
| Utah                 | 5.36426%                                                          | 53.64262%                                                          | 536.42624%                                                          |                                                 6142 |                              171976 |
| Vermont              | 1.00515%                                                          | 10.05146%                                                          | 100.51459%                                                          |                                                  224 |                                6272 |
| Virginia             | 1.44272%                                                          | 14.42724%                                                          | 144.27242%                                                          |                                                 4398 |                              123144 |
| Washington           | 2.55809%                                                          | 25.58092%                                                          | 255.80924%                                                          |                                                 6957 |                              194796 |
| West Virginia        | 2.22638%                                                          | 22.26380%                                                          | 222.63799%                                                          |                                                 1425 |                               39900 |
| Wisconsin            | 2.74641%                                                          | 27.46412%                                                          | 274.64116%                                                          |                                                 5711 |                              159908 |
| Wyoming              | 4.89599%                                                          | 48.95993%                                                          | 489.59930%                                                          |                                                 1012 |                               28336 |
| Puerto Rico          | 1.27301%                                                          | 12.73009%                                                          | 127.30086%                                                          |                                                 1452 |                               40656 |
| District of Columbia | 1.55523%                                                          | 15.55227%                                                          | 155.52271%                                                          |                                                  392 |                               10976 |