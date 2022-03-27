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
url_list = ['https://gq.mines.gouv.qc.ca/documents/SIGEOM/TOUTQC/FRA/SHP/SIGEOM_QC_Geologie_du_socle_SHP.zip',
            'https://gq.mines.gouv.qc.ca/documents/SIGEOM/TOUTQC/FRA/SHP/SIGEOM_QC_Activites_minieres_SHP.zip',
            'https://gq.mines.gouv.qc.ca/documents/SIGEOM/TOUTQC/FRA/SHP/SIGEOM_QC_Geochimie_SHP.zip',
            'https://gq.mines.gouv.qc.ca/documents/SIGEOM/TOUTQC/FRA/SHP/SIGEOM_QC_Geologie_du_Quaternaire_SHP.zip',
            'https://gq.mines.gouv.qc.ca/documents/SIGEOM/TOUTQC/FRA/SHP/SIGEOM_QC_Geophysique_SHP.zip',
            'https://gq.mines.gouv.qc.ca/documents/SIGEOM/TOUTQC/FRA/SHP/SIGEOM_QC_Indices_gites_mines_et_carrieres_SHP.zip'
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
for dirpath, dirnames, filenames in os.walk(filepath):
    for i in filenames:
        if i[-3:] == 'shp':
            subfilepath = os.path.join(dirpath, i)
            vlayer = iface.addVectorLayer(subfilepath, '', 'ogr')

print('You are good to go!')



