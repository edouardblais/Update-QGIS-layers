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

# Select layer from which we want to delete features
layers = QgsProject.instance().mapLayersByName('TITRES_TITLES')
layer = layers[0]

# Save the layer capabilities to a variable (to make sure we can actually delete features from this layer)
caps = layer.dataProvider().capabilities()

# Make a list of all the features in the layer
feats = layer.getFeatures()

# Make an empty list to which we will add the features to be deleted
dfeats = []

# The if statement makes sure our layer has the capability to delete features.
# If not, this line prevents an error or file corruption.
# Then loop through the features. If the feature 'STI_DES_FR' isn't associated to 'Actif', it is added to the list of features to be deleted.
if caps & QgsVectorDataProvider.DeleteFeatures:
    for feat in feats:
        if feat['STI_DES_FR'] != 'Actif':
            dfeats.append(feat.id())
    # Delete the list of features added to the list. We can check the result if we want.
    res = layer.dataProvider().deleteFeatures(dfeats)
    # Once the deleting is done, the layer is repainted with the remaining elements.
    layer.triggerRepaint()

print("Only the active claims remain, you are good to go!")





