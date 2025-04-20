def find_matches_slot(database, query_id):
    matches = []
    for tournament, rounds in database.items():
        for round_name, slots in rounds.items():
            for slot_name, slot_data in slots.items():
                if slot_data.get("id") == query_id:
                    matches.append((tournament, round_name, slot_name))
    
    return matches

def find_matches(database, query_id):
    matches = []
    for tname in database:
        for id in database[tname]:
            if query_id in database[tname][id]:
                matches.append(tname)
                break  # Stop after finding the slug in this tournament    
    return matches