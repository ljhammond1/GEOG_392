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
            name="gdbFolder",
            # datatype="DEFile",
            parameterType= "Required",
            direction="Input"
        )
        param2 =  arcpy.Parameter(
            displayName="Garage Layer CSV File",
            name="garageCSV",
            # datatype="DEFile",
            parameterType= "Required",
            direction="Input"
        )
        param3 =  arcpy.Parameter(
            displayName="Campus Geodatabase",
            name="gdbName",
            # datatype="DEFile",
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
        gdbFolder_input = parameters[1].valueAsText
        garageCSV_input = parameters[2].valueAsText
        gdbName_input = parameters[3].valueAsText

        # Generate our where_clause
        where_clause = "Bldg = '%s'" % buildingNumber_input

        # Check if building entered actually exists
        structures = campus + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        for row in cursor:
            if row.getValue("Bldg") == buildingNumber_input:
                shouldProceed = True

        # If we shouldProceed do so
        if shouldProceed:
            # Name the newly generated buffer LH
            buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferRadius_input)
            # Get reference to building LH
            buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
            # Perform buffer analysis for the selected existing building LH 
            arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
            # Perform clip analysis of the structures to our buffer feature LH
            arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
            # Delete the feature class we just created so it is not permanently part of the geodatabase (this step is just to check) LH
            arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
        else:
            print("Seems we couldn't find the building you entered")
        return None
