import re
import requests


######################

ids = []
forbiddenlist= [".",'(', ')',"'","–",".",",","?", "!",'/',"[","]",'"',':',';','"','=','•','“','„','&']
replacelist= ["-",'  ']
titel = []
permalinks = []
permalinkstart = 'https://sammlungonline.muenchner-stadtmuseum.de/objekt/'
permalinkende = '.html'


#####################

def main(): 
	##open Objektdaten
	otitel = open('titel.txt', 'r')
	for line in otitel:
		titel.append(line)

	oids = open('id.txt', 'r')
	for line in oids:
		ids.append(line)

	otitel.close()
	oids.close()

	for x in range(len(titel)): 
		print(titel[x])

	for x in range(len(titel)):
		titel[x]=titel[x].lower()
		for y in range(len(forbiddenlist)): 
			titel[x]=titel[x].replace(forbiddenlist[y],"")
		for z in range(len(replacelist)): 
			titel[x]=titel[x].replace(replacelist[z]," ")
		titel[x]=titel[x].replace("ä","ae")
		titel[x]=titel[x].replace("ö","oe")
		titel[x]=titel[x].replace("ü","ue")
		titel[x]=titel[x].replace("ß","ss")
		titel[x]=titel[x].replace("è","e")
		titel[x]=titel[x].replace("é","e")
		titel[x]=titel[x].replace("ç","c")
		titel[x]=titel[x].replace("ğ","g")
		titel[x]=titel[x].replace("ı","i")
		titel[x]=titel[x].replace("â","a")
		titel[x]=titel[x].replace("ı","i")
		titel[x]=titel[x].replace("ş","s")
		titel[x]=titel[x].replace("  "," ")
		titel[x]=titel[x].replace(" ","-")
		

	for x in range(len(titel)): 
		print(titel[x])


	results = open("Titel_Permalink.txt", "a")
	for x in range(len(titel)): 
		print(titel[x], file=results)
	results.close()


	for x in range(len(titel)):
		link = "Test"
		#link = (str(permalinkstart) + str(titel[x] + str('-') + str(ids[x]) + str(permalinkende)
		link = 'https://sammlungonline.muenchner-stadtmuseum.de/objekt/{}-{}.html'.format(titel[x],ids[x])
		link = link.replace('\n','')
		#print(link)
		permalinks.append(link)


	permalinktxt = open("res_permalinks.txt", "a")
	for x in range(len(permalinks)): 
		print(permalinks[x], file=permalinktxt)
	permalinktxt.close()


	txt_404 = open("res_permalinks_404.txt", "a")
	
	for n in range(len(permalinks)):
		r=requests.get(permalinks[n])
		#print(r)
		if (n == 1000): 
			print('1000 done')
		if(str(r.status_code)=='404'):
			print(n, file=txt_404)


	txt_404.close()






	#https://sammlungonline.muenchner-stadtmuseum.de/objekt/schwabing-10162866.html


if __name__ == "__main__":
    main()