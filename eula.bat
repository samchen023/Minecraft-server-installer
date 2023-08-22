@ECHO OFF
SETLOCAL EnableDelayedExpansion
set /A "times=0"


FOR /F "delims=*" %%i IN (eula.txt) DO (
	set /A "times= !times! + 1"
	echo !times! -times
	
	if "%%i" == "eula=false" ( 
		echo eula=true>> eula2.txt
	) else (
		echo %%i>> eula2.txt
		)
	

)


::break>eula.txt


:: FOR /F "delims=" %%a in (eula2.txt) do (
:: echo %%a >> eula.txt
:: )
	 
del "eula.txt"
rename "eula2.txt" "eula.txt"


pause