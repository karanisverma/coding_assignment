import argparse
parser = argparse.ArgumentParser(description='Dehash function')

parser.add_argument('h', metavar='hash', type=int, nargs='+',
                    help='Hash value to be decrypt')
args = parser.parse_args()

# print"asdfasdf"
def decrypt(num):
    """
    reverse hashing
    """
    l = "acdegilmnoprstuw"
    dehash_val = []
    while(num > 0 and num != 7):
        pos = num % 37
        if pos < len(l):
            dehash_val.append(l[pos])
        else:
            return "[ERROR]: Invalid hash"
        num = (num - pos) / 37
    if(num == 7):
        return "".join(dehash_val)[::-1]
    else:
        return "[ERROR]: Invalid hash"

print decrypt(args.h[0])
