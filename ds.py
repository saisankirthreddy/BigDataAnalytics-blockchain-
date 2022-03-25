import csv
import time
import gc


start = time.time()
begin = time.time()
class Template:
    def __init__(self, tx_hash, from_addr, to_addr, block_number, token_qty, block_time, block_hash, gas, gas_price,
                 tx_index_in_block, total_gas):
        self.tx_hash = tx_hash
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.block_number = block_number
        self.token_qty = token_qty
        self.block_time = block_time
        self.block_hash = block_hash
        self.gas = gas
        self.gas_price = gas_price
        self.tx_index_in_block = tx_index_in_block
        self.total_gas = total_gas

original_row_list = []
'''for i in range(0, 10):
    with open('/home/scratch1/cs5413/ethereum/transactions/tx_transfers_10-11-2020_etherum_tx_csv-00000000000' + str(i), 'r') as f:
        lines = [line.rstrip() for line in f]
        for x, line in enumerate(lines):
            if (x == 0):
                continue
            words = line.split(',')  # get each item in one line
            row_template = Template(words[0], words[1], words[2], words[3], words[4], words[5], words[6],
                                    words[7],
                                    words[8],
                                    words[9], words[10])
            original_row_list.append(row_template)'''


for i in range(10, 32):

    with open('/home/scratch1/cs5413/ethereum/transactions/tx_transfers_10-11-2020_etherum_tx_csv-0000000000' + str(i),'r') as f:
            lines = [line.rstrip() for line in f]
            for x, line in enumerate(lines):
                if (x == 0):
                    continue
                words = line.split(',')  # get each item in one line
                row_template = Template(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7],
                                        words[8],
                                        words[9], words[10])
                original_row_list.append(row_template)


print("Time for reading files",time.time() - start)

print("\n")

#question 1
print("Question 1")
start = time.time()

blocks_by_gas = {}
tx_hashlist = set()
blocks_with_blocktime = {}

for row in original_row_list:
    row.block_number = int(row.block_number)
    row.gas = int(row.gas)
    if (row.tx_hash) in tx_hashlist:
        continue
    elif row.block_number not in (blocks_by_gas.keys()):
        blocks_by_gas.update({int(row.block_number): int(row.gas)})
        blocks_with_blocktime.update({int(row.block_number): row.block_time})
        tx_hashlist.add(row.tx_hash)
    else:
        blocks_by_gas[row.block_number] = (blocks_by_gas[row.block_number]) + row.gas
        blocks_with_blocktime.update({int(row.block_number): row.block_time})
        tx_hashlist.add(row.tx_hash)

print("Q1:Running time for computations",time.time()-start)

sorted_q1 = sorted(blocks_by_gas.items(), key =lambda kv:(kv[1], kv[0]),reverse=True)

print("Q1:Running time till sorting", time.time()-start)

gc.collect()
# writing into a CSV file
with open('op1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['block_number','block_time','block_gas']
    writer.writerow(header)
    for i in sorted_q1:
        data = [i[0],blocks_with_blocktime.get(i[0]),i[1]]
        writer.writerow(data)

f.close()

print("Q1: Complete Running time",time.time()-start)

print("\n")
del blocks_by_gas
del tx_hashlist
del sorted_q1
gc.collect()
#question 2
print("Question 2")
start = time.time()
tx_hashset = set()
blocks_by_no_transactions = {}


for row in original_row_list:
    row.block_number = int(row.block_number)
    if ((row.block_number) in blocks_by_no_transactions.keys()):
        if((row.tx_hash) in (tx_hashset)):
            continue
        else:
            blocks_by_no_transactions[row.block_number] = (blocks_by_no_transactions[row.block_number])+1
            tx_hashset.add(row.tx_hash)
    else:
        blocks_by_no_transactions.update({row.block_number: 1})
        tx_hashset.add(row.tx_hash)

print("Q2: running time for computations",time.time()-start)


sorted_q2 = sorted(blocks_by_no_transactions.items(), key =lambda kv:(kv[1], kv[0]))

print("Q2: Running time till sorting", time.time()-start)

with open('op2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['block_number','block_time','Transaction_count']
    writer.writerow(header)
    for block in sorted_q2:
        data  = [block[0],blocks_with_blocktime.get(block[0]),block[1]]
        writer.writerow(data)

f.close()
print("Q2: Complete Running time", time.time()-start)

print("\n")
del tx_hashset
del blocks_by_no_transactions
gc.collect()
#question 3
print("Question 3")
start = time.time()
tx_set = set()
blocks_by_tfee = {}
blocks_with_txhash = {}
del sorted_q2

for row in original_row_list:
    if row.tx_hash in tx_set:
        continue
    else:
        tfee = int(row.total_gas) - int(row.gas)
        blocks_by_tfee.update({row.block_number:tfee})
        blocks_with_txhash.update({row.block_number:row.tx_hash})
        tx_set.add(row.tx_hash)

sorted_q3 = sorted(blocks_by_tfee.items(), key =lambda kv:(kv[1], kv[0]))

print("Q3: Running time till sorting",time.time()-start)

data=[]
with open('op3.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['tx_hash','block_number','block_time','transaction_fee']
    writer.writerow(header)
    for i in sorted_q3:
        data = [blocks_with_txhash.get(i[0]),i[0],blocks_with_blocktime.get(i[0]),i[1]]
        writer.writerow(data)
print("Q3: Complete Running time",time.time()-start)
#f.close()
del tx_set
del blocks_by_tfee
del blocks_with_txhash
del sorted_q3
gc.collect()
print("\n")

print("Question 4")
blocks_by_gas={}
blocks_with_transactions = {}
tx_hashlist = set()
for row in original_row_list:
    row.block_number = int(row.block_number)
    row.gas_price = int(float(row.gas_price))
    if(row.tx_hash) in (tx_hashlist):
        continue
    elif row.block_number not in (blocks_by_gas.keys()):
        blocks_by_gas.update({int(row.block_number) : int(float(row.gas_price))})
        blocks_with_transactions.update({int(row.block_number) : row.tx_hash})
    else:
        blocks_by_gas[row.block_number] = (blocks_by_gas[row.block_number]) + row.gas_price
        blocks_with_transactions.update({int(row.block_number) : row.tx_hash})

print("Q4:running time for computations",time.time()-start)


trans_sorted_gas = list(blocks_by_gas.values())
sorted_q4 = sorted(blocks_by_gas.items(), key =lambda kv:(kv[1], kv[0]))

print("Q4:Running time after sorting", time.time()-start)

with open('op4.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['Tx_hash','gas_price','block_number','block_time']
    writer.writerow(header)
    for block in sorted_q4:
        data = [blocks_with_transactions.get(block[0]),block[1],block[0],blocks_with_blocktime.get(block[0])]
        writer.writerow(data)
f.close()
print("Q4:Complete Running time", time.time()-start)

print("\n")
del sorted_q4
del blocks_by_gas
del blocks_with_transactions
del tx_hashlist
del blocks_with_blocktime
gc.collect()

#question5

print("Question 5")

start = time.time()
blocks_by_frmAdd = {}
from_add_list =[]
blocks_by_toAdd={}


for row in original_row_list:
    from_add_list.append(row)


for i in from_add_list:
    blocks_by_frmAdd.update({i.block_number: str(i.from_addr)})
    blocks_by_toAdd.update({i.block_number: i.to_addr})

sorted_q5 = sorted(blocks_by_frmAdd.items(), key =lambda kv:(kv[1], kv[0]),reverse=True)
print("Q5:Running time till sorting", time.time()-start)
data=[]
with open('op5.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['from_addr','to_addr','block_number']
    writer.writerow(header)
    for i in sorted_q5:
        data = [i[1],blocks_by_toAdd.get(i[0]),i[0]]
        writer.writerow(data)
f.close()
print("Q5:Complete Running time",time.time()-start)

print("\n")
del blocks_by_frmAdd
del from_add_list
del blocks_by_toAdd
del sorted_q5
gc.collect()

#question6
print("Question 6")
start = time.time()
temp_block_number = input("Q6: Enter any block number:")
temp_block_number = int(temp_block_number)
block_transaction_list = []
for row in original_row_list:
    if(int(row.block_number) == temp_block_number):
        block_transaction_list.append(row)
        print(row.tx_hash,"  ",(int(row.total_gas) - int(row.gas)),"  ",row.tx_index_in_block,"  ",row.block_number," ",row.block_time)
print ("Q6: Complete Running time",time.time() - start)
del block_transaction_list
#question7
print("Question 7")
start = time.time()
temp_hash=input("Q7:Please enter the transaction hash:")
temp_hash=str(temp_hash)
temp_hash_list = []
for row in original_row_list:
    if(row.tx_hash == temp_hash):
	    print(row.tx_hash,"  ",(int(row.total_gas) - int(row.gas)),"  ",row.block_number," ",row.block_time)
print("Q7:Complete Running time",time.time()-start)

print("\n")
del temp_hash_list
gc.collect()

#question 8
print("Question 8")
start = time.time()
temp_from_address = input("Q8: Enter any From address:")
temp_from_address = str(temp_from_address)
from_address_list = []
somelist = []
for row in original_row_list:
    if(str(row.from_addr) == temp_from_address):
        print(row.tx_hash,"  ",(int(row.total_gas) - int(row.gas)),"  ",row.from_addr,"  ",row.block_number," ",row.block_time)
print("Q8:Complete Running time", time.time()-start)

print("\n")
del from_address_list
del somelist
gc.collect()
#question 9
print("Question 9")
temp_to_address = input("Q9: Enter any to address:")
temp_to_address = str(temp_to_address)
to_address_list = []
for row in original_row_list:
    if(str(row.to_addr) == temp_to_address):
        print(row.tx_hash,"  ",(int(row.total_gas) - int(row.gas)),"  ",row.to_addr,"  ",row.block_number," ",row.block_time)
print("Q9:Complete Running time",time.time()-start)

print("\n")
del to_address_list
gc.collect()
# question 10
print("Question 10")
start = time.time()
ip = input("Q10: please enter the input from/to addr:")
from_address_list = []
token_list = []
tx_hashlist = []
for row in original_row_list:
    if(row.from_addr == ip):
        from_address_list.append(row.from_addr)
        token_list.append(row.token_qty)
print("from_addr/To_addr","                                        ","max_token", "                 ","min_token")
print(ip,"    ",max(token_list),"    ",min(token_list))
print("Q10: Complete Running time",time.time()-start)

print("Running time for all the questions", time.time()-begin)
del from_address_list
del token_list
del tx_hashlist
gc.collect()