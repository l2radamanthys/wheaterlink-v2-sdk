N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

help:
	@echo ""
	@echo "${B}COMANDOS DISPONIBLES"
	@echo " iniciar"
	@echo " lab"
	@echo " notebook"
	@echo ""

iniciar:
	@pipenv run pip install jupyter jupyterlab notebook tabulate

notebook:
	@pipenv run jupyter notebook --no-browser --NotebookApp.token='' --NotebookApp.password=''

lab:
	@pipenv run jupyter lab --no-browser --NotebookApp.token='' --NotebookApp.password=''