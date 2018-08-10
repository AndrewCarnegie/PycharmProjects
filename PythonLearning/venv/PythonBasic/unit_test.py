#coding = utf-8
import pyodbc

conn = pyodbc.connect(DRIVER='{SQL Server}',SERVER='fr711wdbs021.zeu.alcatel-lucent.com\\FR110NA187',DATABASE='ALLIANCE',UID='coset',PWD='coset^QWE')

cur = conn.cursor()

sql = 'select CustomerId, messageId from [dbo].[MESSAGE] where MessageId =896402'

cur.execute(sql)

for row in cur:
    print(row.CustomerId, row.messageId)
conn.close()


