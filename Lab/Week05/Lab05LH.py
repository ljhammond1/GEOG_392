import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [BuildingsIntersectingBufferZone]

class BuildingsIntersectingBufferZone(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buildings Intersected by Buffer Zone"
        self.description = "Determines which buildings on TAMU campus are intersected by a buffer zone surrounding a separate feature. Determines proximity."
        self.canRunInBackground = False
        self.category = "Building Tools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Buffer Radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        param1 =  arcpy.Parameter(
            displayName="Geodatabase Folder",
            name="gdbFolderOut",
            datatype="GPString",
            parameterType= "Required",
            direction="Input"
        )
        param2 =  arcpy.Parameter(
            displayName="Garage File",
            name="garages",
            datatype="GPString",
            parameterType= "Required",
            direction="Input"
        )
        param3 =  arcpy.Parameter(
            displayName="Campus Geodatabase",
            name="gdbName",
            datatype="GPString",
            parameterType= "Required",
            direction="Input"
        )

        params = [param0, param1, param2, param3]
        return params

    def execute(self, parameters, messages):
        """The source code of the tool."""
        campus = r"C:\Users\Ljhammond1996\DevSource\Hammond_GEOG392\Lab\Week05\Campus.gdb"

        # Setup our user input variables
        bufferRadius_input = int(parameters[0].value)
        gdbFolderOut_input = str(parameters[1].value)
        garages_input = str(parameters[2].value)
        gdbName_input = str(parameters[3].value)

        try arcpy.CreateFileGDB_management()

        # Generate our where_clause
        where_clause = "garage = '%s'" % garages_input

        # Check if building entered actually exists
        garages = campus + "/GaragePoints"
        cursor = arcpy.SearchCursor(garages, where_clause=where_clause)
        shouldProceed = False

        for row in cursor:
            if row.getValue("garage") == garages_input:
                shouldProceed = True

        # If we shouldProceed do so
        if shouldProceed:
            # Name the newly generated buffer LH
            buildingBuff = "/GaragePoints_%s_buffed_%s" % (garages_input, bufferRadius_input)
            # Get reference to building LH
            buildingFeature = arcpy.Select_analysis(garages, campus + "/GaragePoints_%s" % (buildingNumber_input), where_clause)
            # Perform buffer analysis for the selected existing building LH 
            arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
            # Perform clip analysis of the structures to our buffer feature LH
            arcpy.Clip_analysis(garages, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
            # Delete the feature class we just created so it is not permanently part of the geodatabase (this step is just to check) LH
            arcpy.Delete_management(campus + "/GaragePoints_%s" % (buildingNumber_input))
        else:
            print("Seems we couldn't find the garages you entered")
        return None