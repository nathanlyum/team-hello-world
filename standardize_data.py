import csv

def standardizeDict(data, dataDict, output):
    with open(data, "r") as f:
        headers = f.readlines()[0].split(',')

    with open(dataDict, "r") as f:
        with open(output, "w") as w:
            data = f.readlines()

            for line in  data:
                header = line.split(",")[0]
                if header in headers:
                    w.write(line)
                    
                    
def standardizeData(data, dataDict, output):
    with open(dataDict, "r") as f:
        headers = [line.split(",")[0] for line in f.readlines()]
        
    with open(data, "r") as f:
        with open(output, "w") as w:
            data = f.readlines()
            headLine = data[0].strip("\n").split(",")
            keep = [header for header in headLine if header in headers]
            
            for line in data:
                features = line.strip("\n").split(",")
                toWrite = [feature for i, feature in enumerate(features) if headLine[i] in keep]
                s = ','.join(toWrite)
                w.write(s + "\n")

#standardizeDict(r"{your file path}", r"{your file path}", r"{your file path}")

#standardizeData(r"{your file path}", r"{your file path}", r"{your file path}",)