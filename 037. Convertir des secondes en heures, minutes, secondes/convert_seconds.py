def convert_seconds(seconde):
    """Convertit des secondes en heures, minutes, secondes
    Renvoie trois nombres entiers : heure, minute et seconde"""
    
    heure = seconde // 3600
    seconde = seconde - heure*3600
    
    minute = seconde // 60
    seconde = seconde -  minute*60

    return heure, minute, seconde
