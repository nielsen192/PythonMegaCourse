from glob import glob2
import datetime as dt

filenames = glob2.glob('*.txt') # Virker ikke, kan ikke finde ud af hvorfor..

with open(dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
