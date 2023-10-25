import itertools
import numpy as np

def is_stable_matching(men_pref, women_pref, current_matching):
    n = len(men_pref)
    
    for man in range(n):
        for ind in range(n):
            better_women = men_pref[man][:ind]
            
            for better_woman in better_women:
                her_pref = women_pref[better_woman]
                
                for her_ind in range(n):
                    if her_pref[her_ind] == man:
                        this_mans_index = her_ind
                        break
                
                for match_ind in range(n):
                    if current_matching[match_ind] == better_woman:
                        she_is_matched_to = match_ind
                        break        
                        
                for her_ind in range(n):
                    if her_pref[her_ind] == she_is_matched_to:
                        she_is_matched_to_index_in_pref = her_ind
                        break
    
                if this_mans_index < she_is_matched_to_index_in_pref:
                    return False
    # for man in range(n):
    #     woman = current_matching[man]
    #     # print(women_pref[woman])
    #     # print(man)
        
    #     for ind in range(n):
    #         # print(women_pref[ind])
    #         if women_pref[woman][ind] == man:
    #             woman_index = ind
    #             break
    #     # woman_index = np.where(women_pref[woman] == man)
        
    #     # print(women_pref[woman])
    #     # print(woman_index)
    #     for other_man in women_pref[woman][:woman_index]:
    #         # other_woman_index = np.where(women_pref[woman] == other_man)[0]
            
    #         for ind in range(n):
    #             if men_pref[other_man][ind] == woman:
    #                 other_woman_index = ind
    #                 break
            
    #         if other_woman_index < current_matching[other_man]:
    #             return False
            # if other_woman_index < women_pref.shape[1]:
            
            # other_woman = women_pref[woman][other_woman_index]
            # if men_pref[other_man][woman] < men_pref[other_man][other_woman]:
            #     return False
    return True

def generate_all_matchings(men_pref, women_pref):
    n = len(men_pref)
    women_indices = list(range(n))
    all_matchings = []

    for men_order in itertools.permutations(women_indices):
        current_matching = [0] * n  # Current matching for each man
        for man, woman in enumerate(men_order):
            current_matching[man] = woman
            
        # print(current_matching)

        if is_stable_matching(men_pref,women_pref , current_matching):
            all_matchings.append(current_matching)

    return all_matchings

# Example preferences (lower number indicates higher preference)
# men_pref = np.array([[0,1, 2,3], [1,0,3,2], [2,3,0,1],[3,2,1,0] ])
# women_pref = np.array([[3,2,0,1], [2,3,1,0], [0,1,3,2],[1,0,2,3] ])

men_pref = np.array([[1,2,3,4],[2,1,4,3],[3,4,1,2],[4,3,2,1]])
women_pref = np.array([[3,4,2,1],[4,3,1,2],[1,2,4,3],[2,1,3,4]])

all_ones = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])

men_pref = men_pref - all_ones
women_pref = women_pref - all_ones


all_matchings = generate_all_matchings(men_pref.tolist(), women_pref.tolist())

print(len(all_matchings))

# all_matchings = np.array(all_matchings)
# all_matchings += all_ones

# for matching in all_matching

for matching in all_matchings:
    print("Matching:", matching)
