import os
import urllib
import zipfile


def get_filename(url):
    """ Separates filename from given url """
    if url.find('/'):
        return url.rsplit('/', 1)[1]


# Directory where the files will be downloaded
outdir = r"C:\Users\Edouard\Desktop\SIGEOM_shp"

# Links to SIGEOM website to get the specific files
url_list = ['https://diffusion.mern.gouv.qc.ca/public/GESTIM/telechargements/Province_shape/TITRES_TITLES_ALL.zip'
            ]

# Create folder for files if it does not exist
if not os.path.exists(outdir):
    os.makedirs(outdir)

# Download files
for url in url_list:
    # Separate file name and join it to file directory
    fname = get_filename(url)
    outfp = os.path.join(outdir, fname)

    # if SIGEOM file already exists, remove it directly
    if os.path.exists(outfp):
        os.remove(outfp)

    # download and extract SIGEOM files in directory
    print("Downloading", fname)
    zip, headers = urllib.request.urlretrieve(url, outfp)
    with zipfile.ZipFile(zip, 'r') as zf:
        zf.extractall(outdir)

# load SIGEOM shapefiles into QGIS
filepath = "C:/Users/Edouard/Desktop/SIGEOM_shp"
for files in os.listdir(filepath):
    if files.endswith('.shp'):
        subfilepath = os.path.join(filepath, files)
        vlayer = iface.addVectorLayer(subfilepath, '', 'ogr')

print('You are good to go!')

