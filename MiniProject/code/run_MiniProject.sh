
printf "Install R packages if required.\n"
Rscript "install_packages.R"

printf "Preparing data.\n"
Rscript "data_preparation.R"

printf "Calculating initial values.\n"
python3 "initial_vals.py"

printf "Fitting models"
Rscript "model_fitting.R"

printf "Making demonstration plots.\n"
Rscript "demo_plots.R"


printf "Performing analysis.\n"
Rscript "analysis.R"

printf "Compiling report.\n"
bash "CompileLaTeX.sh" > junk.txt

mv write_up.pdf ../report/write_up.pdf

rm Rplots.pdf
rm *.sum
rm .write_up.pdf
rm .Rhistory
rm junk.txt