import json
#json.dump
numbers = [2,3,4,7,11]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj);

#json.load
with open(filename) as f_obj:
    numbers1 = json.load(f_obj)
print(numbers1)
