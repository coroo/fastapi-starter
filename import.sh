#!/bin/bash

############################################################################
################## Update below values in .env file ########################

DB_BACKUP_PATH=$(grep DB_BACKUP_PATH .env | cut -d '=' -f2) ## Insert Backup .sql path here
DB_HOST=$(grep DB_HOST .env | cut -d '=' -f2)
DB_PORT=$(grep DB_PORT .env | cut -d '=' -f2)
DB_USERNAME=$(grep DB_USERNAME .env | cut -d '=' -f2)
DB_PASSWORD=$(grep DB_PASSWORD .env | cut -d '=' -f2)
DB_DATABASE=$(grep DB_DATABASE .env | cut -d '=' -f2)
DB_CONTAINER_NAME=$(grep DB_CONTAINER_NAME .env | cut -d '=' -f2)
DB_BACKUP_TABLE_NAME=$(grep DB_BACKUP_TABLE_NAME .env | cut -d '=' -f2)

#############################################################################

echo "Restore backup started for database - ${DB_DATABASE}"

mysql -u${DB_USERNAME} -p${DB_PASSWORD} -h ${DB_CONTAINER_NAME} ${DB_DATABASE} < ${DB_BACKUP_PATH}/init.sql

if [ $? -eq 0 ]; then
  echo "Database restore successfully completed"
else
  echo "Error found during restore"
fi