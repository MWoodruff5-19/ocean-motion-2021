#These .exec files store these other files so that you don't have to run code for a bunch of the file individually
#vectorq.exec file contents
#import datetime as dt
#from datetime import date
#from datetime import timedelta

#date = "03042021"
import sys
date = sys.argv[1]


vectorfile = open("vectorq.exec", "w")


vectorfile.write("#!/bin/csh" + "\n")

vectorfile.write("set dir = ./test/\n")

vectorfile.write("set dhdir = /Users/brownscholar/desktop/BridgeUp_Internship/data/dynamic_height/" + "\n")
vectorfile.write("set dendir = /Users/brownscholar/desktop/BridgeUp_Internship/data/density/" + "\n")
vectorfile.write("set auxdir = /Users/brownscholar/desktop/BridgeUp_Internship/data/aux/" + "\n")
vectorfile.write("set outdir = /Users/brownscholar/desktop/BridgeUp_Internship/data/omega/" + "\n")
vectorfile.write("set fileinfo = {$dir}info_pr.dat" + "\n")
vectorfile.write("set filedh =  {$dhdir}/dyheight_" + date + ".gr" + "\n")
vectorfile.write("set filest =  {$dendir}/density_" + date + ".gr" + "\n")
vectorfile.write("set filestm = {$auxdir}/st0/" + date +"_st0.dat" + "\n")
vectorfile.write("set filequ =  {$outdir}/u/" + date +"_qu.gr" + "\n")
vectorfile.write("set fileqv =  {$outdir}/v/" + date + "_qv.gr" + "\n")
vectorfile.write("set fileqdi = {$auxdir}/qdi/" + date + "_qdi.gr" + "\n")



vectorfile.write("./vectorq.exe << !\n")
vectorfile.write("'$fileinfo'\t#>>>>>Escribe info file info.dat:\n")
vectorfile.write("'$filedh' \t#>>>>>Escribe fichero de altura Dinamica:\n")
vectorfile.write("'$filest' \t#>>>>>Escribe fichero de densidad:\n")
vectorfile.write("'$filestm' \t#>>>>>Escribe fichero de densidad promedio:\n")
vectorfile.write("'$filequ' \t#>>>>>Escribe fichero Qu:\n")
vectorfile.write("'$fileqv'\t#>>>>>Escribe fichero Qv:\n")
vectorfile.write("'$fileqdi'\t #>>>>>Escribe fichero Qdi:\n" )


vectorfile.close()


omegafile = open("omegainv.exec", "w")


#omegainv.exec file
omegafile.write("#!/bin/csh" + "\n")
omegafile.write("set dir = ./test/" + "\n")
omegafile.write("set fileinfo = {$dir}info_pr.dat" + "\n")
omegafile.write("set outdir = /Users/brownscholar/desktop/BridgeUp_Internship/data/omega/" + "\n")
omegafile.write("set auxdir = /Users/brownscholar/desktop/BridgeUp_Internship/data/aux/" + "\n")
omegafile.write("set filestm = {$auxdir}/st0/" + date + "_st0.dat\n")
omegafile.write("set fileqdi = {$auxdir}/qdi/" + date + "_qdi.gr\n")
omegafile.write("set filew =   {$outdir}w/" +date + "_ww.gr\n")
omegafile.write("./omegainv.exe << !" + "\n")
omegafile.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:" + "\n")
omegafile.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:" + "\n")
omegafile.write("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:" + "\n")
omegafile.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):" + "\n")
omegafile.write("'$filew'	#>>>>>Escribe fichero Salida W: !" + "\n")



omegafile.close()