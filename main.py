from scholarly import *
import time
# Search for papers related to a specific topic
search_query = scholarly.search_pubs("Stroke Segmentation")
for i in range(3):
    try:
        paper = next(search_query)
        print("Started...")
        print(f"Paper of {paper['bib']['title']} title has {paper['num_citations']}")
        time.sleep(0.5)
    except Exception as e:
        print(f"ERROR: {e}")
