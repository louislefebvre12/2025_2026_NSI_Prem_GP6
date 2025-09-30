#retrait:
#- choisisser un montant 
#si retrait fait:
#- retirer le montant au solde + noter la date dans un historique

message_billetsde200 = "Séléctionnez le nombre de billets de 200EU : "
message_billetsde100 = "Séléctionnez le nombre de billets de 100EU : "
message_billetsde50 = "Séléctionnez le nombre de billets de 50EU : "
message_billetsde10 = "Séléctionnez le nombre de billets de 10EU : "
message_billetsde5 = "Séléctionnez le nombre de billets de 5EU : "

montant_retrait = input(message_billetsde200) + input(message_billetsde100) + input(message_billetsde50) + input(message_billetsde10) + input(message_billetsde5) 
print(f"Le montant total retiré est de {montant_retrait} EU")
