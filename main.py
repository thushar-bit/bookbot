def counts(file_contents):
    print(len(file_contents.split()))





def number_of_letter_cout(file_contents):
    lowers = file_contents.lower()
    names_dict = {}
    
    for name in lowers:
        if (name.isalpha()):
            if name in names_dict:
                names_dict[name] += 1
            else:
                names_dict[name] = 1
    myKeys = list(names_dict.keys())
    myKeys.sort()
    sorted_dict = {i: names_dict[i] for i in myKeys}

    return sorted_dict
def total_counts(sorted_dict):
    total_count = 0
    for name in sorted_dict:
        size = sorted_dict[name]
        total_count = total_count + size
    return total_count





with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    #counts(file_contents)
    dic = number_of_letter_cout(file_contents)
    t = total_counts(dic)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{t} words found in the document\n")
    for name in dic:
        size = dic[name]
        print(f"The '{name}' character was found {size} times")
    print("--- End report ---")

