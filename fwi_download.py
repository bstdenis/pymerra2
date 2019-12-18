import logging
from pathlib import Path
from pymerra2 import download

# Download Fire Weather indices from the public https NCCS portal.
# Filenames and path are quite different than the MERRA2 products, thus the different file.

url_template = "https://portal.nccs.nasa.gov/datashare/GlobalFWI/v2.0/fwiCalcs.{data_source}/Default/{prcp_source}/{year:04d}/FWI.{prcp_source}.{freq_str}.Default.{date}.nc"

# Source of tas, rh, ws and snowdepth, either "MERRA2" or "GEOS-5"
data_source = "MERRA2"
# Source of precipitation data one of:
# "CPC", "GPCP", "GPM.EARLY.v5", "GPM.EARLY", "GPM.FINAL.v5", "GPM.FINAL", "GPM.LATE.v5", "MERRA2.CORRECTED", "MERRA", "Sheff", "TRMM"
prcp_source = "MERRA2.CORRECTED"
# Wanted frequency either "Daily" or "Monthly"
freq_str = "Daily"

output_dir = None

for yyyy in range(2017, 2019):
    for mm in range(1, 13):
        download.download_from_url(
            url_template=url_template,
            var_name="FWI",
            freq=freq_str.casefold(),
            initial_year=yyyy,
            final_year=yyyy,
            initial_month=mm,
            final_month=mm,
            initial_day=1,
            output_dir="/home/pbourgault/Documents/",
            delete_temp_dir=True,
            merra2_names_map={
                "{0}_{1}".format(prcp_source, ind): ind
                for ind in ["DC", "DMC", "FFMC", "ISI", "BUI", "FWI", "DSR"]
            },
            verbose=True,
            # All below are kwargs for the url_template or the final attrs
            data_source=data_source,
            freq_str=freq_str,
            prcp_source=prcp_source,
            Source="GFWED",
            Title="Global Fire WEather Database",
            References="https://data.giss.nasa.gov/impacts/gfwed",
            cell_methods="",
        )
