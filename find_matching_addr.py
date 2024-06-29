def find_string_list_similarity(l1,l2):
    '''
        Find if 2 list of strings match wrt to "l2"

        input:
            1. l1: (string list **preferably the shorter one) 1
            2. l2: (string list) 2
        output:
            - list of floats of similarity in % wrt to "l2"
    '''
    cnt = 0
    for s1 in l1:
        for s2 in l2:
            if s1 == s2:
                # if matching string, increase counter
                cnt += 1
                break

    return cnt/len(l2)*100

def find_matching_addr(addr1,addr2):
    '''
        Find if 2 address lists have addresses of different spelling refering to the same location

        input:
            1. a1: (string list **of same length as output) address 1 
            2. a2: (string list) address 2
        output:
            1. list of "a2" of highest matching similarity
            2. list highest similarity % of 2 address list
    '''
    match = [] # output list of highest similarity addresses
    sim = [] # output list of similarity

    # store max similarity index & value
    max_sim = [0,0] # [0] is index of max similarity, [1] is value of max similarity
    
    for a1 in addr1:
        # reset max_sim
        max_sim[0] = 0
        max_sim[1] = 0
        
        # iterate through list of length we want to keep
        for i in range(len(addr2)):
            s = find_string_list_similarity([x for x in re.split(r"[,|.|\s]",addr2[i]) if x!=''], [x for x in re.split(r"[,|.|\s]",a1) if x!='']) # find similarity
            if s > max_sim[1]:
                # if current similarity is higher than max, record its index & value
                max_sim[0] = i
                max_sim[1] = s

        # add similarity value & address with highest similarity into output list
        sim.extend([max_sim[1]])
        match.extend([addr2[max_sim[0]]])
            
    return match, sim