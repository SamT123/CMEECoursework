if [ $# -eq 0 ]
  then
    Rscript get_Treeeight.R ../Data/trees.csv
  else
    Rscript get_Treeeight.R $1
fi