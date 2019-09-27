#!/bin/bash
# This script will take a name as input and create a .py file with a starting template for my mac

file_name=$1
[ -e ${file_name} ]&&{ echo "file already exists"; exit 1; }
[ -e ${file_name} ]||{
touch $file_name;
echo "#!$(which python3)" >> ${file_name}
echo >> ${file_name}
echo "# $USER" >> ${file_name}
echo "def main():" >> ${file_name}
echo >> ${file_name}
echo "if __name__ == '__main__':" >> ${file_name}
echo "    main()" >> ${file_name}
exit 1;
}
