#############
# Κλαση Player

class Player:
    
    ##############
    # Κατασκευαστης
    
    def __init__(self, name, score, skip, fifty, reply):
        self.name = name
        self.score = score
        self.skip = skip
        self.fifty = fifty
        self.reply = reply

    #################
    # Μεθοδος εμφανισης ονομα παικτων
    
    def display_Players(self):
        print("Παίκτη "+self.name+" παίξε.")
        print()

    #################
    # Μεθοδος εμφανισης αν οι παικτες απαντησαν σωστα/λαθος
    
    def display_Cor_Wro(self):
        if(self.reply):
            print("Ο παίκτης " +self.name+ " απάντησε σωστά!")
        else:
            print("Ο παίκτης " +self.name+ " απάντησε λάθος.")

    ##############
    # Μεθοδος βοηθειων 50-50 και skip
    
    def display_Help(self):

            if(self.skip and self.fifty):
                help_response = input("Έχεις διαθέσιμες τις βοήθειες '50-50' και 'skip this question'. Θέλεις να χρησιμοποιήσεις βοήθεια; Γράψε 'ν'(για ναι) ή 'ο'(για όχι).")
                while(True):
        
                    if (help_response == "ν"):
            
                        while(True):
                            help_response_options = input("Διάλεξε τη βοήθεια που θέλεις γράφοντας '50' (για '50-50') ή 'σ' (για 'skip this question').")

                            if(help_response_options == "50"):
                            
                                self.fifty = False
                                if (ask[1] == 1):
                                    print("%d) %s"%(1,ask[2]))
                                    print("%d) %s"%(2,ask[3]))
                                elif (ask[1] == 2):
                                    print("%d) %s"%(2,ask[3]))
                                    print("%d) %s"%(3,ask[4]))
                                elif (ask[1] == 3):
                                    print("%d) %s"%(3,ask[4]))
                                    print("%d) %s"%(4,ask[5]))
                                elif (ask[1] == 4):
                                    print("%d) %s"%(3,ask[4]))
                                    print("%d) %s"%(4,ask[5]))
                                break
                        
                            elif (help_response_options == "σ"):
                            
                                self.skip = False
                            
                                for answer in skip_question:
                                    print(answer[0]+';')
                                    w = 1
                                    for option in answer[2:]:
                                        print ("%d) %s" % (w,option))
                                        w = w + 1
                    
                                break
                
                
                            else:
                                help_response_options = input("Διάλεξε τη βοήθεια που θέλεις γράφοντας ΜΟΝΟ '50' (για '50-50') ή 'σ' (για 'skip this question').")
                        break

        
                    elif(help_response == "ο"):
                        break
                    else:
                        help_response = input("Έχεις διαθέσιμες τις βοήθειες '50-50' και 'skip this question'. Θέλεις να χρησιμοποιήσεις βοήθεια; Γράψε ΜΟΝΟ 'ν'(για ναι) ή 'ο'(για όχι).")
                
            #############################################
            # Με βοηθεια '50-50' διαθεσιμη
            
            elif(not(self.skip) and self.fifty):
                help_response = input("Έχεις διαθέσιμη τη βοήθεια '50-50'. Θέλεις να τη χρησιμοποιήσεις; Γράψε 'ν'(για ναι) ή 'ο'(για όχι).")
                while(True):

                    if (help_response == "ν"):

                       self.fifty = False
                       if (ask[1] == 1):
                            print("%d) %s"%(1,ask[2]))
                            print("%d) %s"%(2,ask[3]))
                       elif (ask[1] == 2):
                            print("%d) %s"%(2,ask[3]))
                            print("%d) %s"%(3,ask[4]))
                       elif (ask[1] == 3):
                            print("%d) %s"%(3,ask[4]))
                            print("%d) %s"%(4,ask[5]))
                       elif (ask[1] == 4):
                            print("%d) %s"%(3,ask[4]))
                            print("%d) %s"%(4,ask[5]))
                       break


                    elif(help_response == "ο"):
                        break

                    else:
                        help_response = input("Έχεις διαθέσιμη τη βοήθεια '50-50'. Θέλεις να τη χρησιμοποιήσεις; Γράψε ΜΟΝΟ 'ν'(για ναι) ή 'ο'(για όχι).")
                
            ###############################################
            # Με βοηθεια 'skip' διαθεσιμη
            
            elif(self.skip and not(self.fifty)):
                help_response = input("Έχεις διαθέσιμη τη βοήθεια 'skip this question'. Θέλεις να τη χρησιμοποιήσεις; Γράψε 'ν'(για ναι) ή 'ο'(για όχι).")
                while(True):

                    if (help_response == "ν"):
                
                        self.skip = False
                    
                        for answer in skip_question:
                            print(answer[0]+';')
                            w = 1
                            for option in answer[2:]:
                                print ("%d) %s" % (w,option))
                                w = w + 1
                    
                        break
            

                    elif(help_response == "ο"):
                        break

                    else:
                        help_response = input("Έχεις διαθέσιμη τη βοήθεια 'skip this question'. Θέλεις να τη χρησιμοποιήσεις; Γράψε ΜΟΝΟ 'ν'(για ναι) ή 'ο'(για όχι).")

            #######################################
            # Χωρις βοηθειες
            
            else:
                print("Δεν υπάρχουν διαθέσιμες βοήθειες.")

        
####################
# Εμφανισε Περιγραφη

def display_Begin():
    print("Οι 10 επομενες ερωτησεις θα απαντηθουν με τη σειρα που οι παικτες"
              " εχουν δωσει τα ονοματα τους")
    print("Οι παικτες μπορουν να απαντησουν γραφωντας 1,2,3 ή 4")
    print()


    
#################
# Δηλωση των ονοματων των παικτων

num_players = []
for i in range(3):
    name = input("Συμπληρωσε το ονομα σου παιχτη "+str(i+1)+": ")
    num_players.append(name)

player1 = Player(num_players[0],0,True,True, False)
player2 = Player(num_players[1],0,True,True, False)
player3 = Player(num_players[2],0,True,True, False)
display_Begin()

#################
# Πινακας 10 ερωτησεων και απαντησεων

questions=[

        ['Α)Ποιο από τα παρακάτω νησιά ανήκει στο σύμπλεγμα των Κυκλάδων', 2, 'Η Αντίμηλος', 'Τα Κουφονήσια','Η Ανάφη', 'Η Γυάρος'],
        ['Β)Ποιο απο τα παρακάτω ειναι μηχανή αναζητησης στο διαδίκτυο', 2, 'Photoshop', 'Google', 'Wikipedia', 'Outlook'],
        ['Γ)Μετά απο ποιο ιστορικό γεγονός ξεκίνησε η Οθωμανική περίοδος στην Ελλαδα', 2, 'Εκατονταετής Πόλεμος', 'Άλωση της Κωνσταντινούπολης', 'Ελληνική Επανασταση', 'Γαλλική Επανασταση'],
        ['Δ)Ποιο απο τα παρακάτω όργανα του ανθρώπινου σωματος είναι το πιο ανθεκτικό στο πέρασμα του χρόνου', 4, 'Μάτι', 'Καρδιά', 'Εγκέφαλος', 'Συκώτι'],
        ['Ε)Περιφερειακή συσκευή του υπολογιστή που αποτελεί συσκευή εισόδου ...', 1, 'Web camera', 'Plotter', 'Ηχεία', 'Ακουστικά'],
        ['Ζ)Απο πού λεγεται πως εμπνεύστηκαν το σχήμα του "Pac-Man" οι δημιουργοί του πασίγνωστου παιχνιδιού', 3, 'Από το στόμα ενός ψαριού', 'Απο ένα κομμένο μπαλάκι τένις', 'Από μία πίτσα που της έλειπε ένα κομμάτι', 'Από ενα γιαπωνέζικο φρούτο'],
        ['Η)Πότε γεννήθηκε ο Αλή Πασάς', 1, '1744', '1544', '1844', '1944'],
        ['Θ)Ο "νυμφίος" ειναι ο ...', 2, 'Ύπουλος', 'Γαμπρός', 'Κουμπάρος', 'Νεαρός'],
        ['Ι)Πότε υπογράφτηκε η Συνθήκη του Παρισιού, με την οποία η Αγγλία υποχρεώθηκε να αναγνωρίσει τις 13 αμερικάνικες αποικίες ως ανεξάρτητο κράτος', 1, '1783', '1483', '1883', '1683'],
        ['K)Ο Κώστας Κεντέρης κάνει περήφανη την Ελλάδα με χρυσό ολυμπιακό μετάλλιο στο σπριντ των 200μ. Ηταν το...', 4, '2012', '2008', '2004', '2000'],

      ]

###############
# Ερωτηση του skip

skip_question=[

        ['Ποιος σκότωσε τη Μέδουσα, σύμφωνα με την ελληνική μυθολογία', 4, 'Θησέας', 'Αχιλλέας', 'Βελλεροφέντης', 'Περσέας']
    ]



p1FirstSkipFalse = True
p2FirstSkipFalse = True
p3FirstSkipFalse = True


####################
# Εμφανιση ερωτησεων και απαντηση των παικτων

for ask in questions:
    for i in range(len(num_players)):

        if (i == 0):
            player1.display_Players()
        elif (i == 1):
            player2.display_Players()
        elif (i == 2):
            player3.display_Players()

        print( ask[0]+';')
        n = 1
        for options in ask[2:]:
            print ("%d) %s" % (n,options))
            n = n + 1
            
        ####################
        # Εμφανιση Βοηθειων
        
        if (i == 0):
            player1.display_Help()
        elif (i == 1):
            player2.display_Help()
        elif (i == 2):
            player3.display_Help()
    
        response = input("Δώσε απάντηση 1,2,3 ή 4:")
        print()

        #################
        # Απαντηση των παικτων.-Ελεγχος-
        
        flag = False
        while (True):
            answers = [1,2,3,4]
            for m in str(answers):            
                if (response == m):
                   flag = True
                   break
            if(flag):
                break
            else:
                print("Δωσε μια απο τις δοσμενες απαντησεις (1,2,3,4)")
                response = input("Δωσε απαντηση: ")

        ######################
        # Εμφανιση σωστης/λαθος απαντησης για skip
        
        if (i == 0):
            if (player1.skip == False and p1FirstSkipFalse):
                for answer in skip_question:
                    if (int(response) == answer[1]):
                        player1.score += 10
                        player1.reply = True
                        p1FirstSkipFalse = False
            else:
                if (int(response) == ask[1]):
                    player1.score += 10
                    player1.reply = True
        
        elif (i == 1):
            if (player2.skip == False and p2FirstSkipFalse):
                for answer in skip_question:
                    if (int(response) == answer[1]):
                        player2.score += 10
                        player2.reply = True
                        p2FirstSkipFalse = False
            else:
                if (int(response) == ask[1]):
                    player2.score += 10
                    player2.reply = True

        elif (i == 2):
            if (player3.skip == False and p3FirstSkipFalse):
                for answer in skip_question:
                    if (int(response) == answer[1]):
                        player3.score += 10
                        player3.reply = True
                        p3FirstSkipFalse = False
            else:
                if (int(response) == ask[1]):
                    player3.score += 10
                    player3.reply = True
        

    #######################################
    # Εμφανιση αν οι παικτες απαντησαν σωστα
    
    player1.display_Cor_Wro()
    player1.reply = False
    player2.display_Cor_Wro()
    player2.reply = False
    player3.display_Cor_Wro()
    player3.reply = False
    print()
    print()


##################
# Προσθεση Βαθμολογιας για καθε παικτη
            
if (player1.fifty == True):
    player1.score += 5
if (player1.skip == True):
    player1.score += 5
if (player2.fifty == True):
    player2.score += 5
if (player2.skip == True):
    player2.score += 5
if (player3.fifty == True):
    player3.score += 5
if (player3.skip == True):
    player3.score += 5

    
##############
# Εμφανιση της βαθμολογιας

print()
print("Το παιχνίδι τελείωσε.")
print("Το σκορ των παικτών είναι:")

print(player1.name+":",player1.score)
print(player2.name+":",player2.score)
print(player3.name+":",player3.score)
print()

##############
# Ο παικτης που νικησε

if (player1.score > player2.score and player1.score > player3.score):
    print("Με νικητή τον παίκτη: ", player1.name)
    
elif (player2.score > player1.score and player2.score > player3.score):
    print("Με νικητή τον παίκτη: ", player2.name)

elif (player3.score > player1.score and player3.score > player2.score):
    print("Με νικητή τον παίκτη: ", player3.name)
    
elif(player1.score == player2.score and player1.score > player3.score):
    print("Νικητές-Ισοπολία: ", player1.name, player2.name)

elif(player1.score == player3.score and player1.score > player2.score):
    print("Νικητές-Ισοπολία: ", player1.name, player3.name)

elif(player2.score == player3.score and player2.score > player1.score):
    print("Νικητές-Ισοπολία: ", player2.name, player3.name)

else:
    print("Ισοπαλία όλοι οι παίκτες")
