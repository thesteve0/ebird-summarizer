
class summarizer:

    ## Takes a list containing the procesed lists and caluclates the summary data to a dictionary
    # There are two elements to the dict
    # 1. metadata - contains the information for the effort page
    # 2. species - a list of dicts - each containing six letter code, common name, and count  - sorted alpha ascending

    def summarize_lists(self, list_of_surveys, bird_lookup):

        species_counts = {}
        metadata = {"miles": 0, "hours": 0}

        for list in list_of_surveys:
            metadata["miles"] = metadata["miles"] + list["distance"]
            metadata["hours"] = metadata["hours"] + list["duration"]
            for species in list["species_list"]:

                # We have already added this species to the dict before
                if (species["code"] in species_counts):
                    species_counts[species["code"]]["count"] += int(species["count"])
                # This is the first time we see this species
                else:
                    #add the common name here once
                    common_name = bird_lookup[species["code"]]["common_name"]
                    count = int(species["count"])
                    species_counts[species["code"]] = {"count": count, "common_name": common_name}





        # sort the species list before adding to resultS
        species_counts = dict(sorted(species_counts.items()))
        print("finished tabulating results")
        results = {'metadata': metadata, "counts": species_counts}
        return results
