from ebird.api import  get_checklist
from file_reader import file_reader
from summarizer import summarizer

api_key = "PUT YOUR EBIRD API KEY HERE"


def process_single_list(list_id):

    the_checklist = get_checklist(api_key, list_id)
    result = {}
    if "durationHrs" in the_checklist:
        result["duration"] = the_checklist["durationHrs"]
    else:
        result["duration"] = 0

    result["observer_count"] = the_checklist["numObservers"]

    if "effortDistanceKm" in the_checklist:
        result["distance"] = the_checklist["effortDistanceKm"]
    else:
        result["distance"] = 0

    result["species_list"] = []
    for species in the_checklist["obs"]:
        species_obs = {}
        species_obs["code"] = species["speciesCode"]
        species_obs["count"] = species["howManyStr"]
        result["species_list"].append(species_obs)
    print("ingested checklist: " + list_id)
    return (result)

def print_results(results):
    metadata = results["metadata"]
    counts = results["counts"]

    # print the metadata to a csv file
    with open("./section_metadata.csv", 'w') as metadata_out:
        metadata_out.write("'hours', " + str(metadata["hours"]))
        metadata_out.write("\n")
        metadata_out.write("'miles', " + str(metadata["miles"]))

    # print the counts to a different csv file
    with open("./section_counts.csv", 'w') as counts_out:
        counts_out.write('"common name", "count", "six letter code"\n')
        for count in counts:
            counts_out.write('"' + counts[count]['common_name'] + '", ' + str(counts[count]['count']) + ', "' + count + '" \n')

def main():
    file_worker = file_reader()
    print("fetching and compliling your section results")

    # Read in the JSON for species lookup
    bird_lookup = file_worker.read_species_codes()
    print(len(bird_lookup))

    # read the list of ids from a file and turn into a list
    surveys = file_worker.read_ebird_surveys()
    print(len(surveys))

    # Cycle through the lists and turn them into just the information we need for each list
    # I think this is actually redundant. We could skip this step and just do it on the original lists

    all_observations = []
    for survey in surveys:
        all_observations.append(process_single_list(survey))
        print(len(all_observations))

    # Now calculate the totals
    calculator = summarizer()
    results = calculator.summarize_lists(all_observations, bird_lookup)

    print("time to print")

    # Finally write two files for tabulation spreadsheet
    print_results(results)
    # 1. An effort file
    # 2. A file with a species per line containing count, 6 letter, and common name.

if __name__ == "__main__":

    main()
