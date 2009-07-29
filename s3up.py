#!/usr/local/bin/python

from boto.s3.connection import S3Connection
from boto.s3.key import Key
import settings
import sys

if len(sys.argv) < 4:
  print "Usage: <filename> <bucket> <path>"
  sys.exit(-1)
  
s3 = S3Connection(settings.S3_PUBLIC, settings.S3_PRIVATE)
bucket = s3.get_bucket(sys.argv[2])

k = Key(bucket)
k.key = "%s/%s" % (sys.argv[3].rstrip('/'), sys.argv[1])
k.set_contents_from_filename(filename=sys.argv[1], policy='private')