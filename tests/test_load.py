import tempfile

from .context import merra2


def test_merra2():
    var_names = ['tasmin', 'tasmax', 'prmax']
    delete_temp_dir = True
    download_dir = tempfile.mkdtemp()
    merra2_server = 'https://goldsmr4.gesdisc.eosdis.nasa.gov/data/'

    for yyyy in range(1980, 2017):
        merra2.daily_download_and_convert(
            merra2_server, var_names, merra2_var_dicts=None, initial_year=yyyy,
            final_year=yyyy, initial_month=1, final_month=12, initial_day=1,
            final_day=None, output_dir=download_dir,
            delete_temp_dir=delete_temp_dir)

    shutil.rmtree(download_dir)


if __name__ == "__main__":
    pass
