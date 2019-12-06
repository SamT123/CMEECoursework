
# check if input file path passed from command line
if [ -z "$1" ]
then
  # use default if no passed file path
  echo 'Running get_Treeheight.R'
  Rscript get_TreeHeight.R ../Data/trees.csv
  echo 'Running get_Treeheight.py'
  python3 get_TreeHeight.py ../Data/trees.csv
else
  # if passed, used specified file path
  echo 'Running get_Treeheight.R'
  Rscript get_TreeHeight.R $1
  echo 'Running get_Treeheight.py'
  python3 get_TreeHeight.py $1
fi
