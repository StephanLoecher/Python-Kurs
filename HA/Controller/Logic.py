from Model.HelmBestand import helme

def suche_helme(groesse=None, max_preis=None, art=None, verschluss=None, material=None):
    return [helm for helm in helme.values() if 
            (groesse is None or helm.groesse == groesse) and 
            (max_preis is None or helm.preis <= max_preis) and 
            (art is None or helm.art == art) and 
            (verschluss is None or helm.verschluss == verschluss) and 
            (material is None or helm.material == material)]
