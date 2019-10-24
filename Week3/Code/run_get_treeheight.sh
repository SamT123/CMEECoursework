if [ $# -eq 0 ]
then
  echo 'Running get_Treeheight.R'
  Rscript get_TreeHeight.R ../Data/trees.csv
  echo 'Running get_Treeheight.py'
  python3 get_TreeHeight.py ../Data/trees.csv
else
  echo 'Running get_Treeheight.R'
  Rscript get_TreeHeight.R $1
  echo 'Running get_Treeheight.py'
  python3 get_TreeHeight.py $1
fi