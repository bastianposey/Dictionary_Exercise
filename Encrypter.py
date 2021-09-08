encrypted_file_content = ""
# code dictionary for encrypting
codes = {'A':'%', 'B':'@', 'C':'8', 'D':'7', 'E':'^', 'F':'5', 'G':'*', 'H':'3', 'I':')', 'J':'1', 'K':'_', 'L':'=', 'M':'?', 
         'N':'`', 'O':'~', 'P':'a', 'Q':'B', 'R':'Y', 'S':'z', 'T':'F', 'U':'j', 'V':'I', 'W':'z', 'X':'Z', 'Y':'w', 'Z':'m',
         'a':'9', 'b':'#', 'c':'$', 'd':'6', 'e':'!', 'f':'&', 'g':'4', 'h':'(', 'i':'2', 'j':'-', 'k':'+', 'l':'{', 'm':'>', 
         'n':',', 'o':'.', 'p':'Z', 'q':'M', 'r':'<', 's':'u', 't':'U', 'u':'t', 'v':'R', 'w':'T', 'x':'r', 'y':'j', 'z':'J', 
         ' ':' ', '.':'.',',':',',':':':' }
# opens, reads, and saves file contents
input_filename = "info_security.txt"
input_file = open(input_filename, 'rt')
user_file = input_file.read()
input_file.close()

# encrpyts file into codded langauge
for inlet in user_file:
    encrypted_file_content+=codes[inlet]

# writes codded message into new file
encrypted_file = open("encrypted_info_security.txt", "w")
encrypted_file.write(encrypted_file_content)
encrypted_file.close()