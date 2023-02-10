def countLetters(letters):
    count =0
    for index in letters:
        count=count+1
    return count

def countLetter_a(letters):
    count_a=0
    for index in letters:
        if(index=='a' or index=='A'):
            count_a=count_a+1
    return count_a

sentence="Hi this is programing with QamamrAbbas"
totalletters=countLetters(sentence)
total_a_letters=countLetter_a(sentence)
print('Total Letters in Sentence are ', totalletters)
print('Total a_letters in Sentence are ', total_a_letters)
