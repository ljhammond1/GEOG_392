# import arcpy into VS Code window
import arcpy
print("Success")

# set workspace, assign folder path, new gdb name, and new gdb path
arcpy.env.workspace = 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\Week04'
folder_path = 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\\Week04'
gdb_name = 'MyLab04.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)
# stands for arcpy.CreateFileGDB_management('C:\\Users\\Ljhammond1996\DevSource\\Hammond_GEOG392\\Lab\Week04', 'Test.gdb')
# shortcut so you don't to include full paths in side of arguments

# assign csv garage info path (read in CSV data file), garage layer name, and garage point locations 
csv_path = 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\Week04\\04\\garages.csv'
garage_layer_name = 'garages_layer'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name, '', '')

# specify input layer as new garages points, move those points/feature class to the newly created geodatabase, specify path for new garages layer feature
input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(garages , gdb_path)
garages_layer = gdb_path + '\\' + garage_layer_name

# open campusgdb and copy building feature to my test.gdb
campus = 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\\Week04\\04\\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

#re-project the layers
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garages_layer, gdb_path + '\Garage_Points_reprojected', spatial_ref)

# garage buffer
garageBuffer = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_points_buffer', 150)

#garage buffer and buildings intersect
arcpy.Intersect_analysis([garageBuffer, buildings], gdb_path + '\Garage_building_intersect', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\Garage_building_intersect', 'C:\\Users\\Ljhammond1996\\DevSource\\Hammond_GEOG392\\Lab\Week04', 'Garages_Near_Buildings_Intersect.csv')