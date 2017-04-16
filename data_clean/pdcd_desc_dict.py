import string

i = 0
pdcd_desc = {}
with open('define_valid_pd_cd_and_pd_desc.out','r') as f:
    for line in f:
        try:
            line = line.strip(string.punctuation).split(",", 1)
            line[0]= line[0].strip().strip(string.punctuation)
            line[1] = line[1].strip().strip(string.punctuation)
            pdcd_desc[line[0]] = line[1]
        except:
            continue

output = open('pdcd_desc_dict.txt','w')
output.write(pdcd_desc)
output.close()
print(pdcd_desc)