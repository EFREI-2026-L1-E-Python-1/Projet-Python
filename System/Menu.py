from System.Function import Function

class Menu :

  # Class for Menus
  
  class Display :

    # Class for Displaying the Menus
    
    def main(self) :

      # Function that Display the Main Menu
      
      Menu().Tool().clear()
      Menu().Tool().Constructor().normal(
        "Menu Principal", (
          ("Aide",self.help_), 
          ("Gestion des Lecteurs", self.Reader().main), 
          ("Gestion des Livres", self.Book().main), 
          ("Fonctionnalités", self.Feature().main), 
          ("Quitter", Menu().Tool().exit_) ) )
      
    def help_(self) :

      # Function that Display the Help Menu

      Menu().Tool().clear()
      Menu().Tool().Separation().long()
      print("Aide\n")
      print("Ce fichier d'aide est situé dans readme.txt\n")
      help_file = open("README.txt", "r")
      print(help_file.read())
      help_file.close()
      input("\nAppuyez sur n'importe quelle touche pour continuer")
      Menu().Tool().Constructor().end()
  
    class Reader :

      # Class for Reader Menus
      
      def main(self):

        # Function that Display the Reader Main Menu

        Menu().Tool().clear()
        title = "Gestion des Lecteurs"
        next = Menu().Tool().Constructor().normal(
          title, (
            ("Afficher", self.display), 
            ("Ajouter", self.add), 
            ("Modifier", self.edit), 
            ("Supprimer", self.delete), 
            ("Retour", "break") ) )
        if not next=="break" :
          Menu().Tool().Constructor().end(
            title, 
            self.main, 
            "de la", 
            "à la" )
        else :
          Menu().Display().main()
      
      def display(self) :

        # Function that Call the Reader Display Function 
        
        Menu().Tool().format(Function().Reader().display)
    
      def add(self) :

        # Function that Call the Reader Adding Function
        
        Menu().Tool().format(Function().Reader().add)
    
      def edit(self) :

        # Function that Call the Reader Editing Function
        
        Menu().Tool().format(Function().Reader().edit)
    
      def delete(self) :

        # Function that Display the Reader Deletion Menu
        
        Menu().Tool().format(Function().Reader().delete)
  
    class Book :

      # Class for Book Menus
      
      def main(self) :

        # Function that Display the Book Main Menu

        Menu().Tool().clear()
        title = "Gestion des Livres"
        next = Menu().Tool().Constructor().normal(
          title, (
            ("Afficher", self.display),
            ("Ajouter", self.add),
            ("Modifier", self.edit),
            ("Supprimer", self.delete),
            ("Noter", Menu().Display().Feature().rate),
            ("Se faire Suggérer", Menu().Display().Feature().suggest), 
            ("Retour", "break") ) )
        if not next=="break" :
          Menu().Tool().Constructor().end(
            title,
            self.main,
            "de la",
            "à la" )
        else :
          Menu().Display().main()
      
      def display(self) :

        # Function that Display the Book Display Menu
        
        Menu().Tool().format(Function().Book().display)
        
      def add(self) :

        # Function that Display the Book Adding Menu
        
        Menu().Tool().format(Function().Book().add)

      def edit(self) :

        # Function that Display the Book Editing Menu

        Menu().Tool().format(Function().Book().edit)
        
      def delete(self) :
        
        # Function that Display the Book Deletion Menu
      
        Menu().Tool().format(Function().Book().delete)

    class Feature :

      # Class for Feature Menus
      
      def main(self) :

        # Function that Display the Feature Main Menu

        Menu().Tool().clear()
        title = "Fonctionnalités"
        next = Menu().Tool().Constructor().normal(
          title, (
            ("Noter", self.rate),
            ("Se faire Suggérer", self.suggest), 
            ("Retour", "break") ) )
        if not next=="break" :
          Menu().Tool().Constructor().end(
            title,
            self.main,
            "des",
            "aux" )
        else :
          Menu().Display().main()
        
      def rate(self) :

        # Function that Display the Book Rating Menu
        
        Menu().Tool().format(Function().Feature().rate)
  
      def suggest(self) :
  
        # Function that Display the Book Suggestion Menu

        Menu().Tool().format(Function().Feature().suggest)

  class Tool :

     # Class for Tool for all Menu Constructors

    def format(self, method) :

      # Function that Format Function Menus
    
      self.Separation().medium()
      method()

    class Constructor :
      
      # Class for Menu Constructor
      
      def normal(self, *content) :
          
        # Input: Title, ( (Choice1, PathToChoice1), (Choice2, PathToChoice2), ... )
        
        # Function that Create a Dynamic Option Menu that Display it, and Take User Choice to Return its Correct Path
        
        Menu().Tool().Separation().long()
        print( content[0] + "\n" )
        number = 0
        for element in content[1] :
          number += 1
          print( number , "-" , element[0] )
        choice = input("\nChoix : ")
        while not ( (choice.isdigit()) and ( int(choice)>=1 and int(choice)<=number ) ) :
          choice = input("Choix Incorrect, réessayer : ")
        try :
          return content[1][int(choice)-1][1]()
        except TypeError :
          return content[1][int(choice)-1][1]

      def end(self, *args ) :

        # Input: Optional Title

        # Function that Create a Dynamic End Menu
        
        if len(args)==0 :
          Menu().Tool().Constructor().normal(
            "Fin du Programme", (
              ("Revenir au Menu Principal", Menu().Display().main),
              ("Quitter Programme", Menu().Tool().exit_) ) )
        elif len(args)==4 :
          title = args[0]
          path = args[1]
          determinant_1 = args[2]
          determinant_2 = args[3]
          Menu().Tool().Constructor().normal(
          "Fin " + determinant_1 + " " + title, (
            ("Revenir au Menu Principal", Menu().Display().main),
            ("Revenir " + determinant_2 + " " + title, path),
            ("Quitter Programme", Menu().Tool().exit_) ) )
        else :
          raise ValueError("Function End require 0 or 4 arguments")
      
    class Separation :

      # Class for Menu Separators
      
      def __init__(self) :
        
        # Init for the Class for Menu Separators
        
        self.lengh = 50

      def __calculation(self, number) :
        
        # Function that Calculate the Separator Lengh
        
        return print("\n" + "-"*(self.lengh//number) + "\n")
      
      def long(self) :
      
        # Function that Display a Long Horizontal Separator
      
        self.__calculation(1)

      def medium(self) :

        # Function that Display a Medium Horizontal Separator
      
        self.__calculation(2)
    
    def clear(self) :

      # Function that Clear the Menus (dynamically to the OS)
      
      from os import system, name
      system('cls' if name=='nt' else 'clear')
      
    def exit_(self) :

      # Function that Exit the Program Menus

      self.Separation().long()
      print("À bientôt")