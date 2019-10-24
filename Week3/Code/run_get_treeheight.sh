if [ $# -eq 0 ]
  then
    Rscript get_TreeHeight.R ../Data/trees.csv
    python3 get_TreeHeight.py ../Data/trees.csv
  else
    Rscript get_TreeHeight.R $1
    python3 get_TreeHeight.py $1