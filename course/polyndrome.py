#polyndrome




a=input("enter a string1:")
if a==a[::-1]:
    print("polyndrome")
else:
        print(" not polyndrome")


'''
original_string = input("Enter any word, phrase, or number: ")
# 1. Clean the string:
#    - Make everything lowercase with .lower()
#    - Remove all non-alphanumeric characters (letters and numbers)
clean_string = ''.join(char for char in original_string.lower() if char.isalnum())


Let's use the example: original_string = "Taco Cat"
     .lower() -> Normalize the Case
          It first turns everything into lowercase.
          "Taco Cat" becomes "taco cat".
      for char in ... if char.isalnum() -> Filter the Characters
           It then loops through the lowercase string and keeps only the characters that are letters or numbers (isalnum). It throws away spaces, punctuation, etc.
           "taco cat" produces a sequence of characters: t, a, c, o, c, a, t.
      ''.join(...) -> Rebuild the String
           Finally, it takes all the kept characters and joins them together into a new string, using '' (nothing) as the glue.
           The sequence t, a, c, o, c, a, t becomes "tacocat".
'''


    
