# Romans Kucerenko 211RDB275 4.grupa

from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i+1))
            #print("test1")
            #pass
            
        if next in ")]}":
            # Process closing bracket, write your code here.
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next):
		return str(i+1)
		opening_brackets_stack.pop()
            #print("test2")
            #pass
    if(opening_brackets_stack):
		return opening_brackets_stack[0].position
        #print("test3")
	return "Success"
      
def main():
    text = input()
    mismatch = find_mismatch(text)
    # Process closing bracket, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
