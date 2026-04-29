if __name__ =='__main__':
   sentence = input("Enter a sentence: ")
   # Count the number of words in the sentence  
   word_count = len(sentence.split())
   print(f"Number of words in the sentence: {word_count}")
   
   #Char count in the sentence
   char_count =len(sentence)
   print(f"Number of characters in the sentence: {char_count}")
   
   #Count the vowels in the sentence
   vowels = 'aeiouAEIOU'
   vowel_count = sum(1 for char in sentence if char in vowels)
   print(f"Number of vowels in the sentence: {vowel_count}")
   
   #count upper case in the sentence
   uppercase_count = sum(1 for char in sentence if (char.isupper()))
   print(f"Number of uppercase characters in the sentence: {uppercase_count}")

   #count lower case in the sentence
   lowercase_count = sum(1 for char in sentence if (char.islower()))
   print(f"Number of uppercase characters in the sentence: {lowercase_count}")