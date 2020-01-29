# Άσκηση 9:
#     Γράψτε ένα πρόγραμμα σε Python το οποίο 
#     παίρνει έναν αριθμό τον τριπλασιάζει, προσθέτει 
#     ένα και στην συνέχεια προσθέτει τα ψηφία του. 
#     Η διαδικασία επαναμβάνεται μέχρι ο αριθμός να γίνει μονοψήφιος
# Βήματα:
#     1)Ζητάμε απο τον χρήστη να εισάγει έναν αριθμό και τον αναγκάζουμε να βάλει Integer μεσω μιας while
#     2)Στη συνέχεια εχω την συνάρτηση manipulateNumber οπου δέχεται τον αριθμό οπου έβαλε ο χρήστης
#     3)Ο αριθμός τριπλασιάζεται και προσθέτετε 1 σε αυτόν
#     4)Ύστερα κάθε κάθε νούμερό του το βάζω σε λίστα splitted[]
#     5)Για κάθε νούμερο στη λίστα το προσθέτω σε μεταβλητή summed
#     6)Εάν το μήκος της λίστας splitted[] είναι >1 κάνει feedback Loop και δίνει τον αριθμό
#     που έχει εώς τώρα πίσω στην συνάρτηση
#     7)Τέλος εκτυπώνω τον αριθμό σε κάθε βήμα



sum = 0
trippled = 0
splitted = []


def manipulateNumber(number):
    summed = 0
    print(number, "the number before")
    trippled = (number*3) +1
    print(trippled, "the number multiplied by 3 + 1")
    splitted = [int(x) for x in str(trippled)]
    for number in splitted:
        summed += number
    if (len(str(summed)) == 1):
        print(summed, "final number")
    else:
        letsGoAgain = summed
        manipulateNumber(letsGoAgain)

   
while True:    
    try:    
        inputNumber = int(input())    
        break
    except:
        print("Please enter a integer")

manipulateNumber(inputNumber)  
       
