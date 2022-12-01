if [ $# -eq 0 ]
  then
    echo "No day supplied"
    exit 0
fi

mkdir -p ./days/$1
cp ./template.py ./days/$1/today.py
touch ./days/$1/input.txt
cd ./days/$1
code .
