import nltk, sys


def makebi(liste):
 if(len(liste)<3):
  return [(liste[0], liste[1]), (liste[1], liste[0])]
 else:
  res=[]
  first=liste[0]
  for e in liste[1:]:
   res=res+ [(first,e), (e,first)]
  return res+ makebi(liste[1:])     


if len(sys.argv)<2:
 sys.exit("Oppsss!: You need to give two or three parameters; given: 0 or 1 \n command usage:\n python lines2co.py inputfile.txt  out.csv\n min-frequency")


filename=sys.argv[1]
outfile= sys.argv[2]

freq=0
if(len(sys.argv)>3):
 freq=int(sys.argv[3])

all=[]

f=open(filename,"r")
bi=[]
for line in f:
 if line.strip():
  q=line.split(",") 
  q2=[e.strip().lower() for e in q]
  q2=[e for e in q2 if len(e)>0]
  all=all+q2
  bi=bi + makebi(q2)

fdterms=nltk.FreqDist(all)


fd=nltk.FreqDist(bi)

keys=fd.keys()
terms=[]
for key in keys:
 terms.append(key[0])
 terms.append(key[1])

terms=list(set(terms))
terms= [t for t in terms if fdterms[t]>freq]

out=open(outfile,"w")



for t in terms:
 out.write(";"+t.replace(" ","_"))

out.write("\n")

for t1 in terms:
 out.write(t1.replace(" ","_"))
 for t2  in terms:
  out.write(";"+ str(fd[(t1,t2)]))
 out.write("\n")

out.close()

