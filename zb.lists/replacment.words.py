'''
Julissa Paramo
10 / 6 / 23
Replacement Words
'''
# compares words in the same index of two sentence
# only prints the words that are different from eachother
# code assumes both sentences are the same length

sentence1 = input() # user inputs two sentences

sentence2 = input()


sentence1list = sentence1.split() # splits up sentences and turns them into lists

sentence2list = sentence2.split()


for num in range (len(sentence1list)): # iterates through the indexes
  
    if sentence1list[num] != sentence2list[num]: # if the words at those indexes are different, then . . .
      
        print(sentence1list[num], sentence2list[num]) # they will print side by side
