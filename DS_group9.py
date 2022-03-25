
import time
start = time.time()

with open('data.csv', 'r') as f:
    # read from csv line by line, rstrip helps to remove '\n' at the end of line
    lines = [line.rstrip() for line in f]


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

for i, line in enumerate(lines):
    if (i == 0):
        continue
    words = line.split(',')  # get each item in one line
    row_template = Template(words[0], words[1], words[2], words[3], words[4], words[5], words[6], words[7], words[8],
                            words[9], words[10])
    original_row_list.append(row_template)



def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def get_key(val, dict):
    key_list = []
    for key, value in dict.items():
        if val == value:
            key_list.append(key)
        else:
            "SOMETHING WRONG!!!!!"
    return key_list


'''def write_csv(mylist):
    with open('myfile.csv', 'w') as f:
        for i in range(len(mylist[0])):
            for j in range(len(mylist)):
                f.write(mylist[j][i] + ',')
            f.write('\n')'''


# question 1
'''blocks_by_gas = {}
tx_hashlist = []
blocks_with_blocktime = {}
for row in original_row_list:
    row.block_number = int(row.block_number)
    if(row.block_number) in list(blocks_by_gas.keys()):
        if (row.tx_hash) in (tx_hashlist):
            continue
        else:
            tx_hashlist.append(row.tx_hash)
            row.gas = int(row.gas)
            blocks_by_gas[row.block_number] = (blocks_by_gas[row.block_number]) + row.gas
    else:
        blocks_by_gas.update({int(row.block_number) : int(row.gas)})
        blocks_with_blocktime.update({int(row.block_number) : row.block_time})

sorted_gas = list(blocks_by_gas.values())

mergeSort(sorted_gas, 0, len(sorted_gas)-1)
#quickSort(sorted_gas, 0, len(sorted_gas)-1)'''

##print("Running time till sorting",time.time()-start)

'''sorted_blocks_by_gas ={}
key_list = []
for gas in sorted_gas:
    key_list = get_key(gas, blocks_by_gas)
    for key in key_list:
        sorted_blocks_by_gas.update({key : gas})

blocks = []
blocks = list(sorted_blocks_by_gas.keys())
blocks.reverse()
#print(len(blocks))   Instead of writing, you can jst check by printing
for block in blocks:
        print(block,blocks_with_blocktime.get(block),sorted_blocks_by_gas.get(block))'''

#print("Complete running time for question 1:", time.time()-start)

# question 2
# building transaction set
# question 2

block_with_time = {}

for row in original_row_list:
    block_with_time.update({int(row.block_number): row.block_time})


transaction_set = set()
for row in original_row_list:
    transaction_set.add(row.tx_hash)
transaction_set = list(transaction_set)

blocks_by_no_transactions = {}
for row in original_row_list:
    # print(type(row.block_number))
    # print(type(blocks_by_no_transactions.keys()))
    if (int(row.block_number) in blocks_by_no_transactions.keys()):
        blocks_by_no_transactions[int(row.block_number)] += 1
    else:
        blocks_by_no_transactions.update({int(row.block_number): 1})

sorted_blocks_by_no_trans = {}
sorted_no_trans = list(blocks_by_no_transactions.values())
#print("Running time before start of sorting", time.time() - start)
mergeSort(sorted_no_trans)


#sorted_q1 = sorted(blocks_by_no_transactions.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

#print("Running time after sorting", time.time() - start)

'''with open('op1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['block_number', 'Transaction_count', 'block_time']
    writer.writerow(header)
    for block in sorted_q1:
        data = [block, block_with_time.get(block[0])]
        writer.writerow(data)
f.close()'''
print("Complete Running time for question2", time.time() - start)



#question 3
# build transaction set similar to before

transaction_set =[]
for row in original_row_list:
    if(row.tx_hash not in transaction_set):
        transaction_set.append(row)

block_with_time = {}
block_number=[]

for row in original_row_list:
    block_with_time.update({int(row.block_number): row.block_time})
    block_number.append(row.block_number)

transaction_fee = {}
for row in transaction_set:
    transaction_fee.update({row.tx_hash : (int(row.total_gas) - int(row.gas))})

#sorted_q3 = sorted(transaction_fee.items(), key =lambda kv:(kv[1], kv[0]),reverse=True)


# writing into a CSV file
#data=[]
'''with open('op1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['tx_hash','block_number','block_time','transaction_fee']
    writer.writerow(header)
    for i in sorted_q3:
        data = [i[0],block_number[i],block_with_time.get(i[0].block_time),i[1]]
        writer.writerow(data)

f.close()'''

print("Complete Running time",time.time()-start)

# question 4
transaction_by_gas = {}
for row in original_row_list:
    if (row.tx_hash in transaction_by_gas.keys()):
        transaction_by_gas[row.tx_hash] += row.gas
    else:
        transaction_by_gas.update({row.tx_hash: int(row.gas)})

trans_sorted_gas = list(transaction_by_gas.values())
mergeSort(trans_sorted_gas, 0, len(trans_sorted_gas) - 1)

sorted_transaction_by_gas = {}
for gas in trans_sorted_gas:
    key_list = get_key(gas, transaction_by_gas)
    for key in key_list:
        sorted_transaction_by_gas.update({key: gas})

#print(*sorted_transaction_by_gas,row.gas_price, row.block_number, row.block_time)
print("Complete Running time4",time.time()-start)


#question 5
block_no_list = {}
for row in original_row_list:
    block_no_list.append(int(row.block_number))


mergeSort(block_no_list, 0, len(block_no_list)-1)
#print(block_no_list)
question_5_res = []
#print("from_addr","                              ","to_addr","                               ","tx_hash","                                ","block_number","      ","block_time")
for b_n in block_no_list:
    for row in original_row_list:
        if b_n == int(row.block_number):
            
print("Complete Running time4",time.time()-start)
#question6
temp_block_number = input("Enter any block number:")
temp_block_number = int(temp_block_number)
block_transaction_list = []
somelist = []
for row in original_row_list:
    if(int(row.block_number) == temp_block_number):
        block_transaction_list.append(row)
        #print(row.tx_hash,"  ",(int(row.total_gas) - int(row.gas)),"  ",row.tx_index_in_block,"  ",row.block_number," ",row.block_time)
print ("Running time6",time.time() - start)


# question 7
temp_hash=input("Please enter the transaction hash:")
temp_hash=str(temp_hash)
temp_hash_list = []
somelist = []
for row in original_row_list:
    if(row.tx_hash == temp_hash):
        this_fee = int(row.total_gas) - int(row.gas)
        this_idx = row.tx_index_in_block
        this_block_no = row.block_number
        this_block_time = row.block_time
#print(this_fee, this_idx, this_block_no, this_block_time)
print ("Running time7",time.time() - start)

#question 8
temp_from_address = input("Enter any From address:")
temp_from_address = str(temp_from_address)
from_address_list = []
somelist = []
for row in original_row_list:
    if(str(row.from_addr) == temp_from_address):
        print(row.tx_hash,"  ",(int(row.total_gas) - int(row.gas)),"  ",row.from_addr,"  ",row.block_number," ",row.block_time)
print("Running time8:", time.time()-start)


#question 9
temp_to_address = input("Enter any to address:")
temp_to_address = str(temp_to_address)
to_address_list = []
for row in original_row_list:
    if(str(row.to_addr) == temp_to_address):
                print(row.tx_hash,"  ",(int(row.total_gas) - int(row.gas)),"  ",row.to_addr,"  ",row.block_number," ",row.block_time)
print("Running time9",time.time()-start)

# question 10 part-1 & part-2

ip = input("please enter the input from/to addr:")
from_address_list = []
token_list = []
tx_hashlist = []
for row in original_row_list:
    if(row.from_addr == ip):
        from_address_list.append(row.from_addr)
        token_list.append(row.token_qty)
#print("from_addr/To_addr","                                     ","max_token", "                ","min_token")
#print(ip,"   ",max(token_list),"   ",min(token_list))
print("Total Running time10:",time.time()-start)


