#!/usr/bin/python3

def open_text_file(file_name):
    file_out=open(file_name, 'r')
    line_of_text=file_out.readline()
#    print(list_of_lines)
    return(line_of_text)

def count_letter(string, letter):
    count_letter=0
    for i in range(len(string)):
        if (string[i]==letter):
            count_letter+=1
    return(count_letter)

def main():
    line_of_text=open_text_file("/home/william/Documents/scripts/text_file.txt")
#    print(line_of_text)
    count_E=count_letter(line_of_text, "E")
#    alphabet=[["A", 0], ["B", 0], ["C", 0]]
#    for i in range(len(alphabet)):
#        alphabet[i][1]=count_letter(line_of_text, alphabet[i][0])
#    print(alphabet)
    alphabet_dict={}
    for i in range(len(line_of_text)):
        if line_of_text[i] in alphabet_dict.keys():
            alphabet_dict[line_of_text[i]]+=1
        else:
            alphabet_dict[line_of_text[i]]=1
#    print(alphabet_dict)
    for letter in alphabet_dict.keys():
        alphabet_dict[letter]=round(alphabet_dict[letter]*100/(len(line_of_text)-1923), 2)
    print(alphabet_dict)


if __name__=="__main__":
    main()
