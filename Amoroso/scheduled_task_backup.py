#!/usr/bin/python
import os
import time

db_User_Name = 'maxfischer2'
DB_User_Password = ''
DB_Name = 'maxfischer2database'
backupDir = '/home/maxfischer2/database_backups/'

datetime = time.strftime('%Y%m%d-%H%M%S')
datetimeBackupDir = backupDir + datetime

print "creating backup folder"
if not os.path.exists(datetimeBackupDir):
    os.makedirs(datetimeBackupDir)


mysqldump_cmd = "mysqldump --skip-lock-tables -u maxfischer2 -h maxfischer2.mysql.pythonanywhere-services.com 'maxfischer2database' >" + datetimeBackupDir + "/" + DB_Name + ".sql"
os.system(mysqldump_cmd)


