#Video Fixing Robot
#By Chris Andres
#Requires Python3, ffmpeg and MediaInfo

#Importing required libarys
import os
import argparse
import subprocess
import sys
from datetime import datetime
import shutil

#Setting Timestamps

#now = datetime.now()
#timestamp2 = datetime.timestamp(now)
# = str(timestamp2)
#print("timestamp = ", timestamp)

#Passing Arguments from the command line
parser = argparse.ArgumentParser(description='A Tortual of Argparse')
parser.add_argument("-i", required=True, type=str, help="Imput file name")
parser.add_argument("-o", required=True, type=str, help="output File Name")
args = parser.parse_args()

#Basic deffinations
inputFile = args.i
outputFile = args.o

#Starting Folder
startingFolder = os.getcwd()
print(startingFolder)

print("Working on: " +inputFile)

#Creating A working folder
workingFolder = inputFile + "_Working"
os.mkdir(workingFolder)
subprocess.run(["cp", inputFile, workingFolder])

#Moving to the working folder
os.chdir(workingFolder)

#Getting Varibles
#This may not be needed, yet, but will be usefull in the future.
widthComand ="mediainfo --inform=" + "'" + "Video" +";" + "%Width%" + "'" + " " + inputFile
heightCommand ="mediainfo --inform=" + "'" + "Video" +";" + "%Height%" + "'" + " " + inputFile
fpsVarCmd2 = "mediainfo --inform=" + "'" + "Video" + ";" + "%FrameRate%" + "'" + " " + inputFile
fpsVarCmd = str(fpsVarCmd2)

#Running the MediaInfo commands
#width = os.popen(widthComand).read()
#height = os.popen(heightCommand).read()
#fpsVar = os.popen(fpsVarCmd).read()

#Printing the varibles, this is more for testing
#print("The Width is: " + width)
#print("The Height is: " + height)
#print("The Frame Rate is: " + fpsVar)


#Script used to rip frames from the video, and re render it
ffmpegInput = "ffmpeg -i " + str(inputFile) + " -r 1/1 " + "$filename%03d.bmp"

#running the ffmpeg script
os.system(ffmpegInput)

#this is more for testing
#print(ffmpegInput)

print("done")

#ffmpeg rendering script
ffmpegOutput = "ffmpeg -r 4 -i %03d.bmp -c:v libx264 -vf fps=30 -pix_fmt yuv420p " + outputFile
#print(ffmpegOutput)

#running the output script
os.system(ffmpegOutput)

#copying the output file back to the starting dir, and cleaning up the workspace
subprocess.run(["cp", outputFile, startingFolder])
os.chdir(startingFolder)
shutil.rmtree(workingFolder)

print("Done")