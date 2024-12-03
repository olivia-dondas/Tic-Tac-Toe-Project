# Base de python


                            # //// VIDEO 1 //////

# degre_celsius = float(input ("Entrez une température en degré celsius " ))
# farheinet = (degre_celsius * 9/5) + 32
# print(farheinet, "F°" )

                            # //// VIDEO 2 /////

# moyenne = float(input("Quelle est votre moyenne " ))

# if moyenne >= 12 and moyenne  <14 :
#     print("Votre mention est ASSEZ BIEN")

# elif moyenne >= 14 and moyenne < 16 : 
#     print("Votre mention est BIEN")

# elif moyenne >= 16 and moyenne < 20 :
#     print("Votre mention est TRES BIEN")

# elif moyenne < 10 :
#     print ("Vos resultat ne sont pas suffisant")

# else : 
#     ("Veuillez rentrer une moyenne compris entre 0 et 20 ")

                    # //// CORRECTION //////

# moyenne = float(input("Quelle est votre moyenne ? " ))

# if 12 <= moyenne < 14 : 
#     print("Assez bien")
# elif 14 <= moyenne < 16 :
#     print("Bien")
# elif 16 <= moyenne < 18 :
#     print("Très bien")
# elif moyenne >= 18 :
#     print("Les félicitations du jury")
# else : 
#     print("Pas de mention")


                                        #/////VIDEO 3////

nb_vies = 7

mot_mystere = 'python'
mot_public = '_' * len(mot_mystere)

while nb_vies > 0 and mot_mystere != mot_public :
    lettre = input ('Entre une lettre : ' )

    if lettre in mot_mystere : 
        for i in range(len(mot_mystere)) : 
            if mot_mystere[i] == lettre : 
                mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
    else : 
        nb_vies -= 1
    if mot_public == mot_mystere : 
        print("Bravo ! Le mot est ", mot_mystere)
    elif nb_vies == 0 :
        print("Vous avez perdu")
    else:
        print("Vous avez, " , nb_vies , "vies")
        print("le mot est ", mot_public)


                            #////VIDEO 4 ////////
