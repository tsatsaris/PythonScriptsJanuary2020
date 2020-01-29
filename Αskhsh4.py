# Άσκηση 4:
#     Γράψτε μια συνάρτηση η οποία μετατρέπει ένα string σε αριθμό 
#     σύμφωνα με την αναπαράσταση των αριθμών σε ASCII code και 
#     μετά ελέγχει αν ο αριθμός είναι πρώτος. Για τον έλεγχο αν ένας 
#     αριθμός είναι πρώτος ΔΕΝ μπορείτε να χρησιμοποιήσετε εξωτερική βιβλιοθήκη.
# Βήματα:
#     1)Για κάθε γράμμα που δινει ο χρήστης το σπάω σε χαρακτήρες και ταυτόχρονα βάζω 
#     σε λίστα numbersFromWords[] το ascii αριθμό του με την ord(letters)
#     2)Για κάθε αριθμό στην λίστα μου τον προσθέτω σε μία μεταβλητή Sum οπου κρατάω το σύνολο
#     3)Για να είναι ένας αριθμός πρώτος πρεπει να διαιρείτε με τον αυτό του και το 1 μόνο
#     4)Το ελέγχω και εκτυπώνω ανάλογο μύνημα


word = input()

numbersFromWords = []
list(word)
sum = 0
#pairnw kathe gramma kai to kanw arithmo

for letter in word:
    numbersFromWords.append(ord(letter))

for number in numbersFromWords:
    sum += number

#to / gyrnaei float opote // gia na gyrisei int
for i in range (2, sum//2):
    if (sum % i) == 0:
        print(sum, "is not prime")
        break
    else:
        print(sum, "is a prime number")





