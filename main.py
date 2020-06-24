import pandas as pd
import us
import requests
import ast
import arrow
COVID_API = "https://covidtracking.com/api/v1/states/{}/daily.csv"
POP_API = "https://api.census.gov/data/2019/pep/population?get=POP&for=state:*"
LIST_OF_STATES_WITH_FIPS = {
    k: v.lower() for k, v in us.states.mapping(
        'fips', 'abbr').items() if v is not None}
prep_data = {'State': [],
             "Possibility_1": [],
             "Possibility_10": [],
             "Possibility_100": [],
             "Max": [],
             "Estimated_existing": []}
raw_pop_data = requests.get(POP_API).text
raw_pop_data = ast.literal_eval(raw_pop_data)
# Data look like this:
# [['POP', 'state'], ['2976149', '28'], ['6137428', '29'], ...]
pop_data = {LIST_OF_STATES_WITH_FIPS[each[1]]: int(
    each[0]) for each in raw_pop_data[1:]}
for fips, state in LIST_OF_STATES_WITH_FIPS.items():
    if not pop_data.get(state, None):
        continue
    max_in_past_14_days = pd.read_csv(COVID_API.format(state.lower())).head(14)[
        'positiveIncrease'].max()
    # Add *2 just in case ppl are lying about the numbers
    guess_current_covid_count = max_in_past_14_days * 14 * 2

    prep_data['State'].append(us.states.lookup(state).name)
    prep_data['Possibility_1'].append("{:.5%}".format(
        guess_current_covid_count / pop_data[state]))
    prep_data['Possibility_10'].append("{:.5%}".format(
        guess_current_covid_count / pop_data[state] * 10))
    prep_data['Possibility_100'].append("{:.5%}".format(
        guess_current_covid_count / pop_data[state] * 100))
    prep_data['Max'].append(max_in_past_14_days)
    prep_data['Estimated_existing'].append(guess_current_covid_count)

df = pd.DataFrame(prep_data, columns=list(prep_data.keys()))
df.sort_values(by=['Possibility_1'])
internal_to_external_name_map = {
    'Possibility_1': 'Chance of encountering 1 person with COVID',
    'Possibility_10': 'Chance of encountering 10 people with COVID',
    'Possibility_100': 'Chance of encountering 100 people with COVID',
    'Max': 'Max count of new case increase in the past 14 days',
    'Estimated_existing': 'Estimated people count with COVID'
}
df = df.rename(internal_to_external_name_map, axis='columns')

with open("README_BASE.md") as b:
    with open("README.md", "w") as f:
        for line in b:
            f.write(line)
        f.write('\n Updated at:' + str(arrow.utcnow())+'\n\n')
df.to_markdown(open('README.md', 'a'),showindex=False)


