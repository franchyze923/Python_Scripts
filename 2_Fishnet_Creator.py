# Script that creates fishnet over extent of each individual feature in a feature class
# Made by Fran
# Sometimes arc needs to be closed for it to run properly.. im not sure why but occasionally it will give a lock error

import arcpy
from arcpy import env
import os
import time
import datetime # prob could have just used the time module , but first easy way i found use datetime to dispay current time

program_start = datetime.datetime.now().time()
start_time = time.time()
print 'Program started at ', program_start

ws = env.workspace = r'F:\Files\GIS\josh_project2\Fishnet_Creator\scratch.gdb' # Path to geodatabase containing the point feature class of interest
fc = r'amtrak_station_2mi_rectangle'  # Name of feature class of interest
env.outputCoordinateSystem = arcpy.SpatialReference(3857) # I don't know why this isnt done automatically ? I've never had to do this before but without this statement, when i put the outputs in arc they are unprojected.
env.overwriteOutput = True

#if arcpy.Exists('outputs.gdb'): # I thought I needed this, i was getting already exist errors before but seems to be running fine lol ? IDK
    #arcpy.Delete_management('outputs.gdb')


output_workspace = os.path.dirname(ws)
print output_workspace
new_gdb = 'outputs.gdb'
arcpy.CreateFileGDB_management(output_workspace, new_gdb)
print 'Creating new geodatabase for outputs'

counter = 0
#airport_cursor = arcpy.da.SearchCursor(fc,["SHAPE@", "NAME"]) # Alternate way of creating a search cursor
with arcpy.da.SearchCursor(fc, ['SHAPE@', 'NAME']) as airport_cursor:  # the SHAPE@ TOKEN produces XY coordinates


    for x in airport_cursor: # For loop loops through and gets XY of each individual record in the feature class. Then it uses the NAME field to name the new output feature

        print 'Currently Processing Record #', counter
        counter += 1

        extent = x[0].extent
        Xmin = extent.XMin
        Xmax = extent.XMax
        Ymin = extent.YMin
        Ymax = extent.YMax

        print 'Xmin = ', Xmin, 'Ymin = ', Ymin, 'Xmax = ', Xmax, 'Ymax = ', Ymax

        out_feature_class = new_gdb + os.sep + str(x[1])
        out_feature_class = out_feature_class.replace(" ", "_") #the blank space was giving me errors so I had to replace all blanks with an underscore

        #MAKE VARS FOR THE SCRIPT BELOW, not necessary but the example I was looking at did it this way

        originCoordinate = str(Xmin) + " " + str(Ymin) # all these need to be converted to strings
        yAxisCoordinate = str(Xmin) + " " + str(Ymin + 10)
        cellSizeWidth = '804.672'
        cellSizeHeight = '804.672'
        numRows = '0'
        numColumns = '0'
        oppositeCorner = str(Xmax) + " " + str(Ymax)
        labels = 'NO_LABELS'
        #templateExtent = '#'
        extent_template = str(Xmin) + " " + str(Xmax) + " " + str(Ymax) + " " + str(Ymin) # Idk if this even does anything..the script produces the same thing if I just leave this field blank ?
        geometryType = 'POLYGON'

        # HERE IS THE MEAT OF THE PROGRAM.
        arcpy.CreateFishnet_management(out_feature_class, originCoordinate, yAxisCoordinate, cellSizeWidth, cellSizeHeight,
                                       numRows, numColumns, oppositeCorner, labels, extent_template, geometryType)

        print 'Created ', out_feature_class, '...moving onto next one!'
        out_feature_class_clip = new_gdb + os.sep + str(x[1] + "_clip")
        out_feature_class_clip = out_feature_class_clip.replace(" ", "_")

        arcpy.Clip_analysis(out_feature_class,fc,out_feature_class_clip,cluster_tolerance = "") # For some reason if I don't clip it, there is one extra row and one extra column ??

        print 'Created ' , out_feature_class_clip, '...moving onto next one!'

    for x in range(10):
        print 'Finished Sucessfully!!...GOOD JOB FRAN :)'

print("Program took --- %s seconds --- to complete" % (time.time() - start_time))



