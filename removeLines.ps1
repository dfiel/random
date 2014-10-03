#@author b6938236 for FitK3vin
#@date 2013.07.11
mkdir new > $null; ls *.txt| % {$file = $_; cat $file | select -skip 2 | out-file -encoding ASCII ($file.directory.fullname + "\new\" +$file.name)}
