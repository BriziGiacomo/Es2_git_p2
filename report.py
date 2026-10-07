# report.py

def filtra_per_stato(apparati, stato):
    stato_normalizzato = stato.strip().lower()
    return [
        apparato for apparato in apparati 
        if apparato.get("stato", "").strip().lower() == stato_normalizzato
    ]


#filter for bus
def filtra_per_bus(apparati, bus):
    return [
        apparato for apparato in apparati 
        if apparato.get("bus") == bus
    ]