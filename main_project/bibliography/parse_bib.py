from pybtex.database import parse_file

import pandas as pd

from tabulate import tabulate



# Filepath of the uploaded .bib file

bib_file_path = 'all2.bib'



try:

    bib_data = parse_file(bib_file_path)

    # Extracting references details for display

    references = [

        {"ID": entry.key, "Title": entry.fields.get('title', 'N/A'), "Authors": entry.fields.get('author', 'N/A')}

        for entry in bib_data.entries.values()

    ]



    references_df = pd.DataFrame(references)

    print("Parsed BibTeX References:")

    print(tabulate(references_df, headers='keys', tablefmt='psql'))

    print("Display completed.")

except Exception as e:

    print(f"Error parsing BibTeX file: {e}")

    references_df = f"Error parsing BibTeX file: {e}"



references_df
