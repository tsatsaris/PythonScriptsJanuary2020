# Άσκηση 2:
#     Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει ένα κείμενο 
#     από ένα αρχείο και χαρακτιρίζει κάθε λέξη ως καλή ή κακή, 
#     ανάλογα με τα σύμφωνα που περιέχουν. Αν τα σύμφωνα f,c,k, και r 
#     είναι περισσότερα των άλλων, τότε η λέξη είναι “κακή”
# Βήματα:
#     1)Αρχικά σπάω το κείμενο σε λέξεις και το βάζω σε μια λίστα words[]
#     2)Στη συνέχεια καλώ την compareLetters() με την λέξη οπου επεξεργάζομαι 
#     3)Στην συνάρτηση αυτή αρχικοποιώ το μέγεθος της λέξης τον μετρητή "κακων" γραμμάτων
#     και το index οπου είναι η θέση στην λέξη 
#     4)όσο το index ειναι μικότερο απο το μήκος συγκρίνω τα γράμματα απο τη λέξη badletters
#     5)εάν βρεθέι ο χαρακτήρας ανεβαίνει η τιμή του badWordValue κατα 1
#     6)Συγκρίνετε η τιμη του badWordValue με το μέγεθος της λέξεις - badWordValue και εάν ειναι
#     μεγαλύτερη τοτε η λέξη χαρακτιρίζεται ως "bad" αλλλιώς ως "good"
#     7)βάζω τον χαρακτηρισμό σε μία λίστα και καθώς η σύγκριση με την λίστα με τις λέξεις είναι παράλληλα
#     θα δημιουργήσω ενα Dictionary{} οπου με Key-Value Pairs θα φαίνεται ο χαρακτηρισμός της λέξης
#     8)Tέλος τυπώνω το Dictionary και κλείνω το αρχείο 

    



wordsDictionary = {}
grades = []
words = []
badletters = "fckr"
evaluation = ""

lengthOfWord = 0
    
def compareLetters(word):
    lengthOfWord = len(word)
    badWordValue = 0
    index = 0    
    while index <= lengthOfWord:
        for letter in word:
            for char in badletters:                    
                if char is letter:
                    badWordValue +=1 
        index += 1
    if (badWordValue >= lengthOfWord-badWordValue):
        evaluation = "bad"
    else:
        evaluation = "good"
    grades.append(evaluation)

#splittarw se lekseis 
with open("Erwtima2.txt", "r") as file :
    for line in file :
        for word in line.split():
            words.append(word)
            compareLetters(word)
    wordsDictionary = dict(zip(words, grades))
    print(wordsDictionary)
  
file.close()



