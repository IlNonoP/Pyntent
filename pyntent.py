def get_intent(phrase):
    result_id = 0
    result_cent = 0
    with open("intent/INDEX.txt", "r") as f:
        data_file = f.readlines()
    
    #print(data_file)
    
    for data in data_file:
        intent_data = data.split("|")
        intent_id = intent_data[0]
        intent_file = str(intent_data[1])
        intent_file = intent_file.replace("\n", "")
        
        with open("./intent/"+intent_file+".txt") as file:
            intent_verify_data = file.readlines()

        words_tot_verify = 0
        words_verify_present = 0
        for line in intent_verify_data:
            words_count_verify = line.split(" ")
            for word in words_count_verify:
                if word.lower() in phrase.lower():
                    words_verify_present = words_verify_present + 1
                words_tot_verify = words_tot_verify + 1

        result_temp = (words_verify_present / words_tot_verify) * 100

        if result_temp > result_cent:
            result_id = intent_id
            result_cent = result_temp

    #print("RESULT ID="+str(result_id))
    #print("RESULT CENT="+str(result_cent))

    return(int(intent_id), float(result_cent))


        



#get_intent("Che tempo c'è oggi?")