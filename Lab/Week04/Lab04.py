# import arcpy into VS Code window aftwer logging into ArcGIS Pro
import arcpy
print("Success")

# set workspace assign folder path, new gdb name, and new gdb path
arcpy.env.workspace = 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\Week04'
folder_path = 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\\Week04'
gdb_name = 'MyLab04.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)
# create new GDB for this project, comment out after running once because it'll return an error for already existing
# stands for arcpy.CreateFileGDB_management('C:\\Users\\Ljhammond1996\DevSource\\Hammond_GEOG392\\Lab\Week04', 'MyLab04.gdb')
# shortcut so you don't to include full paths in side of arguments

# read in the garage info CSV
# assign csv garage info path, garage layer name, and garage point locations 
csv_path = 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\Week04\\04\\garages.csv'
garage_layer_name = 'garages_layer'
# create new feature layer from the garage CSV (point values/locations)
# specify which columns will count for which parameters
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name, '', '')

# specify input layer as new garages points, convert those points/feature class to the newly created geodatabase, specify path for new garages layer feature
input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(garages , gdb_path)
garages_layer = gdb_path + '\\' + garage_layer_name

# open campusgdb and copy building feature to my gdb
campus = 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\\Week04\\04\\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'
arcpy.Copy_management(buildings_campus, buildings)

#re-project the layers
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garages_layer, gdb_path + '\Garage_Points_reprojected', spatial_ref)

# create garage buffer layer
garageBuffer = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_points_buffer', 150)

# create garage buffer and buildings intersect
arcpy.Intersect_analysis([garageBuffer, buildings], gdb_path + '\Garage_building_intersect', 'ALL')

# convert to table
arcpy.TableToTable_conversion(gdb_path + '\Garage_building_intersect', 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\Week04', 'Garages_Near_Buildings_Intersect.csv')