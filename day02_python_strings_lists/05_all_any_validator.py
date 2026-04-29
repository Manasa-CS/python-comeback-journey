if __name__ == '__main__':
    num_list=list(map(int,input("Enter a list of numbers separated by space: ").split()))
    if all(n>10 for n in num_list):
        print("All numbers are greater than 10");
    if all(n>0 for n in num_list):
        print("All numbers are positive");
    if any(n%2==0 for n in num_list):
        print("At least one number is even");

    string_list = list(input("Enter a list of strings separated by space: ").split())
    if all(len(s)>5 for s in string_list):
        print("All strings have more than 5 characters");
    if any(s.isupper() for s in string_list):
        print("At least one string is in uppercase");
    if all(s.islower() for s in string_list):
        print("All strings are in lowercase");
    if(all(s == s[::-1] for s in string_list)):
        print("All strings are palindromes");