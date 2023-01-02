# Downloaded the CSV version of eBird Taxonomy v2022 on Dec 26 2022
# https://www.birds.cornell.edu/clementschecklist/download/
# deleted all columns EXCEPT SPECIES_CODE, PRIMARY_COM_NAME, SCI_NAME
# Just turned it into a dict keyed on 6 letter code

import json
class file_reader:


    def read_species_codes(self):

        with open("./bird_lookup.json") as bird_lookup:
            bird_data = json.load(bird_lookup)
            ## print(len(bird_data))
            # if we need to sort on genus order be sure to add an id number that reflects position in the list
            # just iterate through the list and add an id number
            return bird_data

    def read_ebird_surveys(self):
        with open('survey_lists.txt') as surveys_list:
            surveys = [line.rstrip() for line in surveys_list]
            return surveys