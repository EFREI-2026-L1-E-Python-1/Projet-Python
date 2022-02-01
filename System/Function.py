class Function :

  # Class for Managing the Databases

  class Reader :

    # Class for Managing the Reader Database

    def display(self) :

      # Function that Display a Reader
      
      print("Afficher Lecteur\n")
      
      reader = open ( "Database/readers.txt", "r" )
      readerVerification = reader.readlines()
      reader.close()
      pseudo = str ( input ( "Entrer un pseudonyme : ") )
      verification = False
      for line in readerVerification:
          line = line.split(",")
          if pseudo == line[0] :
              verification = True
      if verification:

        readers = Function().Tool().file_to_matrix('Database/readers.txt')
        booksReads = Function().Tool().file_to_matrix('Database/booksread.txt')
        book = Function().Tool().file_to_matrix('Database/books.txt')
        
        gender = {1:"Homme", 2:"Femme", 3:"Genre non renseigné"}
        age = {1:"Moins de 18ans", 2:"Entre 18 et 25ans", 3:"Plus de 25ans"}
        readingStyle = {1:"Science-Fiction",2:"Biographie",3:"Horreur",4:"Romance",5:"Fable",6:"Histoire",7:"Comedie"}
        for line in readers :
          __reader = line.split(",")
          if __reader[ 0 ] == pseudo :
            print("Pseudo:", pseudo,
              "\nGenre:", gender[int(__reader[1])],
              "\nÂge:", age[int(__reader[2])],
              "\nType de lecture préféré:",
              readingStyle[int(__reader[3])] )
            booksReads_Target = []
            for __book in booksReads :
              __booksReads = __book.split( "," )
              if __booksReads[0] == pseudo :
                for i in range(1,len(__booksReads)) :
                  booksReads_Target.append(book[int(__booksReads[i])-1])
        print("\nLivre Lus :")
        print(*booksReads_Target, sep=", " )
      else:
        print("Le pseudonyme entré n'exite pas dans la base de données")

      
    def add(self) :

      # Function that Add a Reader
      
      readerVerification = Function().Tool().file_to_matrix('Database/readers.txt')
      pseudo = str ( input ( "Entrer un pseudonyme : ") )
      verification = True
      for line in readerVerification:
          line = line.split(",")
          if pseudo == line[0] :
              verification = False
      if verification :
        
        print( "Ajout lecteur\n")
        
        gender = int( Function().Tool().securised_menu( 
          ("Genre"),
          ("Homme", "Femme", "Peu importe") ) )
          
        age = int( Function().Tool().securised_menu( 
          ("Âge"),
          ("<= 18 ANS", "18 ET 25 ANS", "> 25 ANS") ) )
                  
        readingStyle = int( Function().Tool().securised_menu( 
          ("Style de Lecture Préféré"),
          ("Sci-Fi", "Biographie", "Horreur", "Horreur", "Fable", "Histoire", "Comédie") ) )
        
        reader = open( "Database/readers.txt", "a" )
        reader.write( pseudo + "," + str(gender) + "," + str(age) + "," + str(readingStyle) + "\n" )
        reader.close()
        booksRead = open( "Database/booksread.txt" , "a" )
        reading = ","
        library = Function().Tool().file_to_matrix('Database/books.txt')

        booksReads__ = []
        for i in range( len(library) ) :
          print()
          bookRead = int( Function().Tool().securised_menu( 
            (library[i]),
            ("Lu", "Non lu") ) )
          if bookRead==1 :
            booksReads__.append(str(i+1))
            
        for i in range(len(booksReads__)):
          reading += str(booksReads__[i]) + ","
        booksRead.write( pseudo + reading[:-1] + "\n" )
        
        if not reading == "," :
          print("\nL'ajout du Lecteur a bien été effectué")
        else :
          print("\nL'ajout du Lecteur a bien été effectué mais vous n'avez lu aucun livre proposé (vous êtes probablement inculte)")
        booksRead.close()
      else:
        print ("Le pseudonyme entré est déjà dans la base de données")

      
    def edit(self) :

      # Function that Edit a Reader

      books_ = Function().Tool().file_to_matrix('Database/books.txt')
      reader = Function().Tool().file_to_matrix('Database/readers.txt')
      booksRead_ = Function().Tool().file_to_matrix('Database/booksread.txt')
      
      reader_target = input("Entrer le pseudonyme du Lecteur à modifier : ")
      print()

      verification = False
      for line in reader :
          line = line.split(",")
          if reader_target == line[0] :
              verification = True

      if verification :
        for i in range( len( reader ) ) :
            reader_check = reader[i].split(",")
            if reader_check[0] == reader_target :
                reader_index = i

        reader_line = reader[reader_index].split(",")
        
        reader_line[1] = Function().Tool().securised_menu( 
          ("Genre"),
          ("Homme", "Femme", "Peu importe") )
        
        reader_line[2] = Function().Tool().securised_menu( 
          ("Âge"),
          ("<= 18 ANS", "18 ET 25 ANS", "> 25 ANS") )
        
        reader_line[3] = Function().Tool().securised_menu( 
          ("Style de Lecture Préféré"),
          ("Sci-Fi", "Biographie", "Horreur", "Horreur", "Fable", "Histoire", "Comédie") )
        
        reader[reader_index] = ",".join(reader_line)

        reader_file_overwrite = open( "Database/readers.txt", "w" )
        for line in reader :
          reader_file_overwrite.write(line + "\n")
        reader_file_overwrite.close()
        
        booksReads__ = []
        for i in range( len(books_) ) :
          print()
          bookRead = int( Function().Tool().securised_menu( 
            (books_[i]),
            ("Lu", "Non lu") ) )
          if bookRead==1 :
            booksReads__.append(str(i+1))
        
        booksRead_[reader_index] = reader_target + "," + ",".join(booksReads__)

        print(booksRead_[reader_index])

        booksread_file_overwrite = open( "Database/booksread.txt", "w" )
        for line in booksRead_ :
          booksread_file_overwrite.write(line + "\n")
        booksread_file_overwrite.close()
        
        if not booksReads__ == [] :
          print("\nLa modification du Lecteur a bien été effectué")
        else :
          print("\nLa modification du Lecteur a bien été effectué mais vous n'avez lu aucun livre proposé (vous êtes probablement inculte)")
          
      else:
          print ( "Le pseudonyme n'est pas présent dans la base de données" )
      
    def delete(self) :

      # Function that Delete a Reader

      print("Suppression lecteur")
      reader = open ( "Database/readers.txt" , "r" )
      booksRead = open ( "Database/booksread.txt" , "r" )
      pseudo = input ( "Entrer le pseudonyme du lecteur à supprimer : ")
      stockage = -1
      readers = reader.readlines()
      booksReads = booksRead.readlines()
      reader.close ()
      booksRead.close ()
      for i in range ( len(readers) ) :
          line = readers[i].split(",")
          if pseudo == line[0] :
              # validé
              stockage = i
      if stockage == -1 :
          print ( "Pseudo introuvable" )
      else :
          del readers[stockage]
          reader = open ( "Database/readers.txt" , "w+" )
          for element in readers :
              reader.write ( element )
          for j in range ( len(booksReads) ) :
              line = booksReads[j].split(",")
              if pseudo == line[0] :
                  stockage = j
          del booksReads[stockage]
          booksRead = open ( "Database/booksread.txt" , "w+" )
          for element in booksReads :
              booksRead.write ( element )
          print ( "Le lecteur a bien été supprimé")
          reader.close()
          booksRead.close()
  
  class Book :

    # Class for Managing the Books Databases

    def display(self) :

      # Function that Display all Books

      print("Livres\n")
      books = Function().Tool().file_to_matrix('Database/books.txt')
      for i in range(len(books)) :
        print(i+1, "-", books[i] )
      input("\nAppuyez sur n'importe quelle touche pour continuer")
      
    def add(self) :

      # Function that Add a Book

      books_file_read = Function().Tool().file_to_matrix('Database/books.txt')
      books_file_append = open('Database/books.txt', 'a')
      addBook = input("Entrer le Titre : ")
      if not addBook in books_file_read :
        books_file_append.write(addBook + "\n")
      else :
        print("Livre déjà présent")
      books_file_append.close()

    def edit(self) :

      # Function that Edit a Book

      book = Function().Tool().file_to_matrix('Database/books.txt')
      bookModify = input ( "Entrer le titre du livre à modifier : " )
      x = 0
      verification = False
      for line in book :
        if line == bookModify :
          verification = True
      if verification :
        newTitle = input( "Entrer le nouveau titre pour le livre sélectionné" )
        for index in range( len(book) ) :
          if book[index] == bookModify :
            index_target = index
        book[index_target] = newTitle
        books = open( "Database/books.txt" , "w" )
        for element in book :
          books.write( element + "\n" )
        books.close()
        print ( "Le titre du livre a été modifié" )
      else:
        print( "Le livre n'est pas présent dans la bibliothèque" )
      
    def delete(self) :

      # Function that Delete a Book

      books = Function().Tool().file_to_matrix('Database/books.txt')
      booksReads = Function().Tool().file_to_matrix('Database/booksread.txt')
      print("Livres\n")
      for i in range(len(books)) :
        print(i+1, "-", books[i] )
      book_target = int( input("\nSélectionner un livre à supprimer de la bibliothèque : ") )
      while not ( book_target>=1 and book_target<=i+1 ) :
        book_target = int( input("Livre incorrect, Réessayez\nSélectionner un livre à supprimer de la bibliothèque : ") )
      for i in range(len(books)) :
        if i+1 == book_target :
          books.pop(book_target-1)
      books_file_overwrite = open('Database/books.txt', 'w')
      for element in books :
        books_file_overwrite.write( element + "\n" )
      books_file_overwrite.close()
      
      file_overwrite = []
      for line in booksReads :
        index_target = 0
        __booksReads = line.split(",")
        for i in range( 1, len( __booksReads ) ) :
          if int(__booksReads[i]) == book_target :
            index_target = i
          elif int(__booksReads[i]) > book_target :
            __booksReads[i] = str(int(__booksReads[i])- 1)
        if not index_target == 0 :
          del __booksReads[index_target]
        file_overwrite.append(__booksReads)
        
      booksReads_file_overwrite = open( 'Database/booksread.txt', 'w' )
      for line in file_overwrite :
        for index_element in range( len(line) ) :
          if not index_element == len(line)-1 :
            booksReads_file_overwrite.write(line[index_element] + "," )
          else :
            booksReads_file_overwrite.write(line[index_element])
        booksReads_file_overwrite.write("\n")
      booksReads_file_overwrite.close()
      print("\nSuppression effectuée")

  class Feature :

    # Class for Managing the Features

    def rate(self) :

      # Function that Manage the Rating of a Book

      print("Nous n'avons malheureusement pas réussi à faire la fonction noter\nEn nous excusant du désagrément occasionné")
      input("\nAppuyez sur n'importe quelle touche pour continuer")
  
    def suggest(self) :

      # Function that Suggest a Book to a Reader
    
      print("Nous n'avons malheureusement pas réussi à faire la fonction suggérer\nEn nous excusant du désagrément occasionné")
      input("\nAppuyez sur n'importe quelle touche pour continuer")
      
  class Tool :

    def file_to_matrix( self, file ) :
        __file = open(file, 'r')
        matrix = __file.read().splitlines()
        __file.close()
        return matrix

    def securised_menu( self, subject, options ) :
          
      # Input: (subject, determinant), (choice1, choice2, ...)
      
      # Function that Create a Dynamic Option Menu that Display it, and Return User Choice
      
      print("Sélectioner le statut de", subject)
      for index in range( len(options) ) :
        print( index+1 , "-" , options[index] )
      choice = input("Choix : ")
      while not ( (choice.isdigit()) and ( int(choice)>=1 and int(choice)<=len(options) ) ) :
        choice = input("Choix Incorrect, réessayer : ")
      print()
      return choice