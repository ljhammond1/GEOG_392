# arcpy needed to perform geospatial tasks
import arcpy

# Composite the downloaded Landsat bands
source = r"C:\Users\Ljhammond1996\DevSource\Hammond_GEOG392\Lab\Week07\LT05_L1TP_026039_20110819_20160831_01_T1.tar"
# blue band
band1 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B1.TIF")
# green band
band2 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B2.TIF")
# red band
band3 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B3.TIF")
# Near Infrared band
band4 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B4.TIF")
# compositing method, output to new tiff file
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], source + "\combined.TIF")

# Hillshade based on another downloaded DEM file
# specify the source path, default values for azuimuth, altitude, shadows, and z-factor
source = r"C:\Users\Ljhammond1996\DevSource\Hammond_GEOG392\Lab\Week07"
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
# Hillshade method, output to new tiff file
arcpy.ddd.HillShade(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_hillshade.tif", azimuth, altitude, shadows, z_factor)

# Slope based on another downloaded DEM file
# specify the source path, default values for output measurement, z factor, method
source = r"C:\Users\Ljhammond1996\DevSource\Hammond_GEOG392\Lab\Week07"
output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"
# z_unit = "METER"
# Slope method, output to new tiff file
arcpy.ddd.Slope(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_slopes.tif", output_measurement, z_factor)