from django.contrib.gis.db import models


# python ../manage.py ogrinspect voies_mel.shp VoieMel --srid=4326 --mapping --multi
class VoiesMel(models.Model):
    """Les liaisons routière de France métropolitaine,
    https://www.data.gouv.fr/fr/datasets/voies-reseau-routier/#_

    Ce model représente les routes de France métroposlitaine:
        troncon[text] = Identifiant unique de tronçon
        insee[text]: Code INSEE de la commune
        commune[text]: Nom de la commune
        id_voie[int]: Identifiant de la voie
        nom_rue[text]: Nom de la voie
        code_traf[text]: Code du trafic routier moyen journalier
        trafic[text]: Libellé du trafic routier moyen journalier
        code_dome[text]: Code domanialité
        domanialit[text]: Libellé domanialité de la voie
        code_sens[text]: Code sens de circulation
        sens[text]: Libellé sens de circulation
        rivoli[text]: Code Rivoli de la voie
        genre[text]: Genre de la route
        road[LigneString]: la route
    """
    troncon = models.CharField(max_length=5)
    insee = models.CharField(max_length=4)
    commune = models.CharField(max_length=255)
    id_voie = models.CharField(max_length=7)
    nom_rue = models.CharField(max_length=255)
    code_traf = models.CharField(max_length=1, null=True)
    trafic = models.CharField(max_length=255, null=True)
    code_dome = models.CharField(max_length=1, null=True)
    domanialit = models.CharField(max_length=255, null=True)
    code_sens = models.CharField(max_length=1, null=True)
    sens = models.CharField(max_length=255, null=True)
    rivoli = models.CharField(max_length=4)
    genre = models.CharField(max_length=255, null=True)

    road = models.LineStringField(srid=4326)

    def __str__(self):
        return self.nom_rue
