
printf "Preparing data...\n"

Rscript "data_preparation.R"

printf "Calculating initial values...\n"
python3 "initial_vals.py"

printf "Making demonstration plots...\n"
Rscript "demo_plots.R"

printf "Performing analysis...\n"
Rscript "fitting_and_analysis.R"

printf "Compiling report...\n"
bash "CompileLaTeX.sh"