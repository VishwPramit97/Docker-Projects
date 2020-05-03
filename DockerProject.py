import os
while True:

    print("""
          \n\n\n\t--------------------------------------------------------\n  
          \t\t\t### WELCOME To Docker Terminal User Interface ###\n                                            
          \t--------------------------------------------------------            
          \n\n\t\tpress the following keys to perform following actions:\n\t\t  
          press 1: For Installing Docker-CE                   
          press 2: For Docker-compose Installation                            
          press 3: For Launching Wordpress Webapplication linked to MySql database 
          press 4  For stopping the Wordpress Web application            
          press 5: For seeing docker images                                           
          press 6: For seeing containers running                                                                     
          
          
          
          
          press 0: for exit                                                     
                                                                                
                                                                                 
    
          """
          
          )
    
    choice  = int(input("Enter your choice ::"))
     
    if choice == 1:
        os.system("yum install docker-ce --nobest")
    elif choice == 2:
        os.system("firewalld-cmd --zone=public --add-masquerade --permanent")
        os.system("firewalld-cmd --zone=public --add-port=80/tcp")
        os.system("firewalld-cmd --zone=public --add-port=443/tcp")
        os.system("firewalld-cmd --reload")
        os.system("systemctl restart docker")
        printf("/n/n/tNOW your docker yum problem is solved Go and check................")
    
    
    elif choice == 3:
        os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
        os.system(" chmod +x /usr/local/bin/docker-compose")
    
    
    elif choice == 4:
        while True:
            os.system("clear")
            print("\n\nif you don't have wordpress and mysql image then follow these steps:\n\n")
            print("\n\t\tpress 1: for wordpress image ")
            print("\t\tpress 2: for mysql image")
            print("\n\n\tif you already have these images then follow to launch wordress ")
            print("\n\t\tpress 3: for launch wordpress server\n\n\n")
            print("\n\n\tpress 0: Back to main menu")
            choice1 = int(input("Enter your choice : "))
            if choice1 == 1:
                os.system("docker pull wordpress:5.1.1-php7.3-apache")
            elif choice1 == 2:
                os.system("docker pull mysql:5.1")
            elif choice1 == 3:
                os.system("docker-compose up -d")
            elif choice1 == 0:
                exit(1)
            else:
                print("Sorry Invalid Input") 
    
    elif choice == 5:
        os.system("docker images ")  
    
    
    elif choice == 6:
        os.system("docker ps")    
    
    
    
    elif choice == 0:
        exit()
    
    
    else:
        print("Sorry Invalid Input")   
        x= input("PRESS ENTER TO CONTINUE")
