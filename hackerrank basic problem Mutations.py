'''Task 
Read a given string, change the character at a given index and then print the modified string.

Input Format 
The first line contains a string,S . 
The next line contains an integer , denoting the index location and a character  separated by a space.

Output Format 
Using any of the methods explained above, replace the character at index  with character .

Sample Input

abracadabra
5 k
Sample Output

abrackdabra'''


#CODE BEGINS

a=input()
i,c=list(input().split(" "))
n=int(i)
a=a[:n]+c+a[n+1:]
print(a)
