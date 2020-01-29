# Άσκηση 1:
#    Γράψτε ένα πρόγραμμα σε Python το οποίο βρίσκει 
#    τις πέντε μεγαλύτερες λέξεις ενός κειμένου το οποίο διαβάζει 
#    από αρχείο και τις εκτυπώνει ανάποδα, έχοντας αφαιρέσει τα φωνήεντα.
# Βήματα:
#    1)Αρχικά χωρίζουμε το κείμενο σε λέξεις και τις βάζουμε σε μία Λίστα words[]
#    2)Με τις 5 μεταβλητές κανω συγκρίσεις για κάθε λέξη ως προς το μήκος τους
#    3)Έχω πεντε μεταβλητες longenst_word - fifth_longest_word οπου γίνουναι οι συγκρίσεις και σιγουρεύουμε 
#    πως θα είναι 5 οι λέξεις
#    4)Τις εισάγω στην λίστα top_longest_words[]
#    5)Καλώ την συναρτηση reverseAndRemove() 
#    6)για κάθε λέξη στη λίστα top_longest_words[] ελέγχω για φωνήεντα απο τη μεταβλητή bannedLetters
#    7)Εάν υπάρχουν τα αφαιρώ και βάζω το κενό στην θέση τους
#    8)Τέλος γυρίζω ανάποδα την λέξη με μία απλή συνάρτηση οπου βάζω τα γράμματα στο Τέλος
#    9)Print τα αποτελέσματα
#    10)κλείνω το αρχείο	



words = []
longest_word = '' 
second_longest_word =''
third_longest_word = ''
fourth_longest_word = ''
fifth_longest_word = ''
top_longest_words = []
bannedLetters = "aeiouy"
finalWords = []

def reverseAndRemove():
    print("Longest Words are:")
    print(top_longest_words)
    for w in top_longest_words:
        revWord = ""

        for char in bannedLetters:
            w = w.replace(char, "")        
        for letter in w:
            revWord = letter + revWord

        finalWords.append(revWord)  
    print("Longest Words wothout vowels and backwards:")
    print(finalWords)

with open("Erwtima1.txt", "r") as file :
    for line in file :
        for word in line.split():
            words.append(word)
            for w in words:
                if len(w) > len(fifth_longest_word):
                    fifth_longest_word = w
                    if len(fifth_longest_word) > len(fourth_longest_word):
                        fourth_longest_word = fifth_longest_word
                        if len(fourth_longest_word) > len(third_longest_word):
                            third_longest_word = fourth_longest_word
                            if len(third_longest_word) > len(second_longest_word):
                                second_longest_word = third_longest_word
                                if  len(second_longest_word) > len(longest_word):
                                    longest_word = second_longest_word
                                top_longest_words.append(longest_word)
reverseAndRemove()  
  
file.close()
