import pandas as pd

from .ifc_scraper import scrape_ifc
from .worldbank_scraper import scrape_world_bank
from .adb_scraper import adb_scraper
from .afdb_scraper import scrape_afdb
from .eib_scraper import scrape_eib
from .bio_scraper import scrape_bio
from .fmo_scraper import scrape_fmo
from .miga_scraper import scrape_miga
from .ebrd_scraper import scrape_ebrd
from .opic_scraper import scrape_opic
from .kfw_scraper import scrape_kfw


SELECT_ALL_NAME = 'All'

SCRAPER_MAP = {
    'IFC': scrape_ifc,
    'World Bank': scrape_world_bank,

    # NOTE: Uncomment as these are implemented.
    'MIGA': scrape_miga,
    'EIB': scrape_eib,
    'EBRD': scrape_ebrd,
    'Asian Development Bank': adb_scraper,
    'African Development Bank': scrape_afdb,
    # 'AIIB': scrape_aiib,  # deprecated
    # 'IDB': scrape_idb,
    'OPIC': scrape_opic,
    'FMO': scrape_fmo,
    # 'CDC': scrape_cdc,  # deprecated
    'BIO': scrape_bio,
    'KfW': scrape_kfw,
}


def execute_search(search_term, scraper_names):
    """
    iterate through scrapers and merge results.
    output columns: 'Project Name', 'URL', 'Status', 'DFI', 'Search Term'
    """
    df = pd.DataFrame([], columns=['Project Name', 'URL', 'Status', 'DFI'])
    print("#" * 30)
    print('Searching for Term:', search_term)

    if SELECT_ALL_NAME in scraper_names:
        scraper_names = SCRAPER_MAP.keys()

    # TODO: optional - run these asynchronously
    for name in scraper_names:
        scraper = SCRAPER_MAP.get(name)
        if not scraper:
            print(' - ERROR: scraper name {} not found'.format(name))
            print('   ... skipping scraper')
            continue

        print('Scraping:', name)
        df = df.append(scraper(search_term))

    df['Search Term'] = search_term
    return df
