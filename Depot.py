#depot:
#- rentrer un montant 
#si depot fait: 
#- ajouter le montant au solde + noter la date dans un historique 
import data
from data import *






# reponse_message_depot_verif 

def rep_is_yes (rep):
    return rep in yes_responses

def rep_is_no (rep):
    return not (rep_is_yes (rep)) 

def add_amount_to_account ():
    pass

def make_a_depot ():
    pass

if rep_is_yes (rep):
    add_amount_to_account ()

def propose_depot ():
    message_depot = "Choisissez un montant "
    montant_depot = input(message_depot) 
    return montant_depot

def run ():
    rep = input(message_depot_verif) 
    while rep_is_yes (rep):
        make_a_depot ()
    propose_depot ()



run ()