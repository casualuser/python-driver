# coding: utf-8
from cassandra.cluster import Cluster

s = Cluster().connect()

s.execute("CREATE KEYSPACE IF NOT EXISTS test WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};")
s.execute("CREATE TABLE IF NOT EXISTS test.test ( one text, two int, three text, PRIMARY KEY (one,two) );")
print(s.cluster.metadata.keyspaces['test'].export_as_string())
# s.execute(u"CREATE CUSTOM INDEX IF NOT EXISTS ON test.test (three) USING 'org.apache.cassandra.index.sasi.SASIIndex' WITH OPTIONS = { 'delimiter': '\xe2\x96\x91'};")
s.execute(u"CREATE CUSTOM INDEX IF NOT EXISTS ON test.test (three) USING 'org.apache.cassandra.index.sasi.SASIIndex' WITH OPTIONS = { 'delimiter': '░'};")
print(s.cluster.metadata.keyspaces['test'].export_as_string())
