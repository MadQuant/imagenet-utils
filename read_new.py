from pathlib import Path
import urllib3
import os
import sys
import re

def get_imagenet(filein, start, stop):
	ctr = 0
	sin = int(start)
	sout = int(stop)
	print(type(sin))
	with open(filein,'r') as file:
		try:
			for line in file:
				if ctr > sin:
					if ctr < sout:
						try:
							string = line.split()
							url = string[1]
							wfile = 'images/'+string[0]
							if Path(wfile).exists():
								print("file there... " + wfile+ " . "+str(ctr))
								resp.release_conn()
							else:
								conn_pool = urllib3.PoolManager(timeout=2.0)
								print("Requesting... " + url)
								resp = conn_pool.request('GET',url,timeout=urllib3.Timeout(connect=1.0, read=2.0),retries=False)
								if resp.status in [200,301]:
									f = open(wfile,'wb')
									f.write(resp.data)
									f.close()
									print("done storing - " + wfile + ' . ' + str(ctr))
								else:
									print("Bad status code . " + str(resp.status))
								resp.release_conn()
						except:
							print("error on " + str(ctr))
					else:
						print("stopping...")
						break
				else:
					print("advancing... " + str(ctr))
				ctr += 1
		except:
			pass	

get_imagenet(sys.argv[1],sys.argv[2],sys.argv[3])
