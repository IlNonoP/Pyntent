import string

def get_intent(phrase):
    result_id = 0
    result_cent = 0
    with open("intent/INDEX.txt", "r") as f:
        data_file = f.readlines()
    
    for data in data_file:
        intent_data = data.split("|")
        intent_id = intent_data[0]
        intent_file = str(intent_data[1]).strip()
        
        with open("./intent/"+intent_file+".txt") as file:
            intent_verify_data = file.readlines()
        
        total_percentage = 0
        line_count = 0

        for line in intent_verify_data:
            words_count_verify = line.split(" ")
            words_tot_verify = len(words_count_verify)
            words_verify_present = 0
            
            phrase_words = phrase.lower().translate(str.maketrans('', '', string.punctuation)).split()
            for word in words_count_verify:
                word = word.strip().lower().translate(str.maketrans('', '', string.punctuation))
                if word in phrase_words:
                    words_verify_present += 1
            
            if words_tot_verify > 0:
                line_percentage = (words_verify_present / words_tot_verify) * 100
                total_percentage += line_percentage
                line_count += 1

        if line_count > 0:
            average_percentage = total_percentage / line_count
            if average_percentage > result_cent:
                result_id = intent_id
                result_cent = average_percentage

    return int(result_id), float(result_cent)


#print(get_intent("Che tenmpo fa otra?"))