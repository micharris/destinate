import csv

with open("urls.csv") as f_obj:
	reader = csv.DictReader(f_obj, delimiter=',')
	for line in reader:
		print('@task(1)')
		print('def task1(self):')
		print('\tself.client.get("'+line["path"]+'")')