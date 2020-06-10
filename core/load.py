import os

from django.contrib.gis.utils import LayerMapping

from .models import VoiesMel

voiemel_mapping = {
    'troncon': 'troncon',
    'insee': 'insee',
    'commune': 'commune',
    'id_voie': 'id_voie',
    'nom_rue': 'nom_rue',
    'code_traf': 'code_traf',
    'trafic': 'trafic',
    'code_dome': 'code_dome',
    'domanialit': 'domanialit',
    'code_sens': 'code_sens',
    'sens': 'sens',
    'rivoli': 'rivoli',
    'genre': 'genre',
    'road': 'LINESTRING',
}
world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'voies_mel', 'voies_mel.shp'),
)


def run(verbose=True):
    lm = LayerMapping(VoiesMel, world_shp, voiemel_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)
