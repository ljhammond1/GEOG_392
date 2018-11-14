import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [UniqueValueRenderer_06]


class UniqueValueRenderer_06(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Unique Value Renderer 06"
        self.description = "For lab 6, will update a certain feature's display renderer to a unique value renderer"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        InProject = arcpy.Parameter(
            displayName="Input Project",
            name="InProject",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        LayerName = arcpy.Parameter(
            displayName="Layer Name",
            name="LayerName",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"
        )
        OutProject = arcpy.Parameter(
            displayName="Output Project",
            name="OutProject",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        params = [InProject, LayerName, OutProject]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #define progressor
        readTime = 2.5
        start = 0
        maximum = 100
        step = 100

        #setup progressor
        arcpy.SetProgressor("step", "Checking buildings...", start, maximum, step)
        time.sleep(readTime)
        # results message
        arcpy.AddMessage("Checking buildings...")

        # set user input vars
        InProject = str(parameters[0].value)
        LayerName = parameters[1].valueAsText
        OutProject = str(parameters[2].value)
        # Reference to our .aprx
        project = arcpy.mp.ArcGISProject(r"C:\\Users\\Ljhammond1996\\Documents\\ArcGIS\\Projects\\Lab06Project" + r"\\Lab06Project.aprx")
        # Grab the first map in the .aprx
        campus = project.listMaps('Map')[0]
        # Loop through available layers in the map

        # increment progressor and update label
        # add results message
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Checking buildings again...")
        time.sleep(readTime)
        arcpy.AddMessage("Checking buildings again...")

        for layer in campus.listLayers():
            # Check that the layer is a feature layer
            if layer.isFeatureLayer:
                # Obtain a copy of the layer's symbology
                symbology = layer.symbology
                # Makes sure symbology has an attribute "renderer"
                if hasattr(symbology, 'renderer'):
                    # Check if the layer's name is "GarageParking"
                    if layer.name == "GarageParking":
                        # Update the copy's renderer to be "UniqueValueRenderer"
                        symbology.updateRenderer('UniqueValueRenderer')
                        # Tells arcpy that we want to use "Type" as our unique value
                        symbology.renderer.fields = ["LotType"]
                        # Set the layer's actual symbology equal to the copy's
                        layer.symbology = symbology # Very important step
                    else:
                        print("NOT GarageParking")
                        
        project.saveACopy(r"C:\\Users\\Ljhammond1996\\Documents\\ArcGIS\\Projects\\Lab06Project" + r"\\Lab06Project.aprx")