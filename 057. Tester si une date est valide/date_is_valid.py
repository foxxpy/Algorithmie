def bissextile(annee):
    """Teste si une année est bissextile ou non."""
    if((annee%4==0 and annee%100!=0) or annee%400==0):
        return True
    else:
        return False



def date_is_valid(jour, mois, annee):
    """Teste si une date est valide, et donc, si elle peut exister dans le calendrier"""
    fevrier = 29 if bissextile(annee) else 28
    jour_dans_le_mois = {1 : 31,
                         2 : fevrier,
                         3 : 31,
                         4 : 30,
                         5: 31,
                         6 : 30,
                         7 : 31,
                         8 : 31,
                         9 : 30,
                         10 : 31,
                         11 : 30,
                         12 : 31}

    #Si la valeur du mois est compris entre 1 et 12
    #Et que le nombre de jour est compris entre 1 et le nombre de jours dans ce mois
    if 1<= mois <=12 and \
    1 <= jour <= jour_dans_le_mois[mois]:
        return True

    else:
        return False
