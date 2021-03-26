
#!/bin/bash

export PATH=/bin:/usr/bin:/usr/local/bin
TODAY=`date +"%d%m%Y"`

################################################################
################## Update below values  ########################

DB_BACKUP_PATH=$(grep DB_BACKUP_PATH .env | cut -d '=' -f2) ## Insert Backup .sql path here
DB_HOST=$(grep DB_HOST .env | cut -d '=' -f2)
DB_PORT=$(grep DB_PORT .env | cut -d '=' -f2)
DB_USERNAME=$(grep DB_USERNAME .env | cut -d '=' -f2)
DB_PASSWORD=$(grep DB_PASSWORD .env | cut -d '=' -f2)
DB_DATABASE=$(grep DB_DATABASE .env | cut -d '=' -f2)
DB_CONTAINER_NAME=$(grep DB_CONTAINER_NAME .env | cut -d '=' -f2)
DB_BACKUP_TABLE_NAME=$(grep DB_BACKUP_TABLE_NAME .env | cut -d '=' -f2)
BACKUP_RETAIN_DAYS=$(grep BACKUP_RETAIN_DAYS .env | cut -d '=' -f2)   ## Number of days to keep local backup copy
MYSQLDUMP_LOC=$(which mysqldump)
if [${MYSQLDUMP_LOC} -eq '']; then
  MYSQLDUMP_LOC="/usr/local/opt/mysql@5.7/bin/mysqldump"
fi

#################################################################

mkdir -p ${DB_BACKUP_PATH}
echo "Backup started for database - ${DB_DATABASE}"

if [${DB_PASSWORD} -eq '']; then
  ${MYSQLDUMP_LOC} -u${DB_USERNAME} \
      -h ${DB_HOST} \
      -P ${DB_PORT} \
          ${DB_DATABASE} ${DB_BACKUP_TABLE_NAME} --skip-add-drop-table  > ${DB_BACKUP_PATH}/${DB_DATABASE}-${TODAY}.sql
else 
  ${MYSQLDUMP_LOC} -u${DB_USERNAME} \
      -p${DB_PASSWORD} \
      -h ${DB_HOST} \
      -P ${DB_PORT} \
          ${DB_DATABASE} ${DB_BACKUP_TABLE_NAME} --skip-add-drop-table  > ${DB_BACKUP_PATH}/${DB_DATABASE}-${TODAY}.sql
  echo ${DB_PASSWORD}
fi

sed -i '' 's/CREATE TABLE \(.*\)/TRUNCATE TABLE \1; CREATE TABLE IF NOT EXISTS \1/g' ${DB_BACKUP_PATH}/${DB_DATABASE}-${TODAY}.sql
sed -i '' 's/ (; CREATE TABLE IF NOT EXISTS/; CREATE TABLE IF NOT EXISTS/g' ${DB_BACKUP_PATH}/${DB_DATABASE}-${TODAY}.sql

if [ $? -eq 0 ]; then
  echo "Database backup successfully completed"
else
  echo "Error found during backup"
fi


##### Remove backups older than {BACKUP_RETAIN_DAYS} days  #####

DBDELDATE=`date +"%d%m%Y" --date="${BACKUP_RETAIN_DAYS} days ago"`

if [ ! -z ${DB_BACKUP_PATH} ]; then
      cd ${DB_BACKUP_PATH}
      if [ ! -z ${DBDELDATE} ] && [ -d ${DBDELDATE} ]; then
            rm -rf ${DBDELDATE}
      fi
fi

### End of script ####