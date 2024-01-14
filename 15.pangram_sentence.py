alpha=("abcdefghijklmnopqrstuvwxyz")
inp=(input("Enter the sentence:").lower()).replace(" ","")
if sorted(set(alpha)) == sorted(set(inp)):
    print("Pangram!")
else:
    print("Not a Pangram")