from time import sleep
import heapq

N=200
skills=6

fn=[]
ln=[]
health=[]
agility=[]
charisma=[]
knowledge=[]
energy=[]
resou=[]
with open ("data.txt","r") as f:
        for line in f:
                x=line.split(",")
                fn.append(x[0]) #first name
                ln.append(x[1])#last name
                health.append(x[2])#health
                agility.append(x[3])#agility
                charisma.append(x[4])
                knowledge.append(x[5])
                energy.append(x[6])
                resou.append(x[7].strip())

value=[]
for i in range(200):
        health_score = round(6 * (int(health[i]) * 0.2)) + 10       
        agility_score = round(6 * (int(agility[i]) * 0.3)) + 10
        charisma_score = round(6 * (int(charisma[i]) * 0.1)) + 10
        knowledge_score = round(6 * (int(knowledge[i]) * 0.05)) + 10
        energy_score = round(6 * (int(energy[i]) * 0.05)) + 10
        resourcefulness_score = round(6 * (int(resou[i]) * 0.3)) + 10
        overall_value = round(5 * ((health_score * 0.18) + (agility_score * 0.20) + (charisma_score * 0.21) + (knowledge_score * 0.08) + (energy_score * 0.17) + (resourcefulness_score * 0.16)))
        value.append(overall_value)
 
     
indexed_list = list(enumerate(value))
largest_16_with_indices = heapq.nlargest(14, indexed_list, key=lambda x: x[1])
indices, largest_16_values = zip(*largest_16_with_indices)

print("The 16 largest values with their indices are:")
for index, value in largest_16_with_indices:
    #Timothy Pempleton - 94, Jimmy Jones - 92, Randolf Ray - 92
    print(f'{fn[index]} {ln[index]} - {value},', end=' ')