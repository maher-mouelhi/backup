import re

def main():
    # Your code goes here
    find_members = []
    for member in dir(re):
        if "find" in member:
            find_members.append(member)

    print(sorted(find_members))


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()

